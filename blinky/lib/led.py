import pigpio
import threading
from time import sleep
from random import random, randint
from copy import deepcopy
from pytweening import easeInOutExpo as ease

try:
    from .constants import Constants
    from .utils import clamp
except SystemError:
    from constants import Constants
    from utils import clamp


class Led():

    pins = deepcopy(Constants.PINS)
    max_power = float(Constants.MAX)
    rate = Constants.RATE
    killsignal = threading.Event()

    _colors = {
        'RED': 0.0,
        'GREEN': 0.0,
        'BLUE': 0.0
    }

    def __init__(self):
        self.pz = pigpio.pi()
        for pin in self.pins.values():
            self.pz.set_mode(pin, pigpio.OUTPUT)

    @property
    def red(self):
        return self._colors['RED']

    @property
    def green(self):
        return self._colors['GREEN']

    @property
    def blue(self):
        return self._colors['BLUE']

    # directly set RGB, killing any running animations
    def setrgb(self, r=None, g=None, b=None):
        self.killsignal.set()
        self._set('RED', r)
        self._set('GREEN', g)
        self._set('BLUE', b)

    def _animate(self, name, effect, expire_after=None):
        self.killsignal.set()
        self.killsignal = threading.Event()
        runner = Animation(name, effect, self.killsignal)
        runner.start()
        return runner

    # primitive for setting a single color
    def _set(self, color, val):
        clamped_value = clamp(0.0, float(val), self.max_power)
        self._colors[color] = round(clamped_value, 2)
        self.pz.set_PWM_dutycycle(self.pins[color], round(self._colors[color]))



    def clearall(self):
        # terminate any running animations
        self.killsignal.set()

        # power down pins
        for pin in self.pins.values():
            self.pz.set_PWM_dutycycle(pin, 0)

    # how many milliseconds should we spend in a subphase of an animation?
    def _get_phase_length(self, range):
        return randint(*range)

    # how much should the brightness value change per tick?
    def _get_step(self, start_power, end_power, ticks):
        return -(start_power - end_power) / ticks

    def _ease_to(self, duration=2000, r=0, g=0, b=0):
        red = {
            'start': self.red,
            'target': r,
            'diff': -(self.red - r)
        }
        green = {
            'start': self.green,
            'target': g,
            'diff': -(self.green - g)
        }
        blue = {
            'start': self.blue,
            'target': b,
            'diff': -(self.blue - b)
        }

        def effect(killsignal):
            ticks = 0
            while ticks < duration:
                progress = ticks / duration
                self._set('RED', red['start'] + (red['diff'] * ease(progress)))
                self._set('GREEN', green['start'] + (green['diff'] * ease(progress)))
                self._set('BLUE', blue['start'] + (blue['diff'] * ease(progress)))
                ticks += 1
                if killsignal.is_set():
                    return
                sleep(.001)
            killsignal.set()
        self._animate('candle', effect)

    def _flicker_factory(self, color_ranges, pulse_ranges):
        def effect(killsignal):
            duration = self._get_phase_length(pulse_ranges)
            red = {
                'start': self.red,
                'end': randint(*color_ranges['RED'])
            }
            green = {
                'start': self.green,
                'end': randint(*color_ranges['GREEN'])
            }
            blue = {
                'start': self.blue,
                'end': randint(*color_ranges['BLUE'])
            }

            red['step'] = self._get_step(red['start'], red['end'], duration)
            green['step'] = self._get_step(green['start'], green['end'], duration)
            blue['step'] = self._get_step(blue['start'], blue['end'], duration)

            tick = 0
            while tick < duration:
                self._set('RED', self.red + red['step'])
                self._set('GREEN', self.green + green['step'])
                self._set('BLUE', self.blue + blue['step'])
                tick += 1
                sleep(.001)
                if killsignal.is_set():
                    return
        return effect


class Animation(threading.Thread):

    def __init__(self, name, effect, killsignal):
        super(Animation, self).__init__()
        self.name = name
        self.killsignal = killsignal
        self.effect = effect

    def run(self):
        while not self.killsignal.is_set():
            self.effect(self.killsignal)


if __name__ == '__main__':
    l = Led()
    l.clearall()
    print('Shutting down; terminating LED output.')
