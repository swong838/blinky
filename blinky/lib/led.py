import pigpio
import threading
from time import sleep
from copy import deepcopy

try:
    from .constants import Constants
    from .utils import clamp
except SystemError:
    from constants import Constants
    from utils import clamp


class Led():

    pins = deepcopy(Constants.PINS)
    max_power = Constants.MAX
    rate = Constants.RATE
    killsignal = threading.Event()

    _colors = {
        'RED': 0,
        'GREEN': 0,
        'BLUE': 0
    }

    def __init__(self):
        self.pz = pigpio.pi()
        for pin in self.pins.values():
            self.pz.set_mode(pin, pigpio.OUTPUT)

    def setrgb(self, r=None, g=None, b=None):
        self.killsignal.set()
        self._set('RED', r)
        self._set('GREEN', g)
        self._set('BLUE', b)

    def _animate(self, name, effect):
        self.killsignal.set()
        self.killsignal = threading.Event()
        runner = Animation(name, effect, self.killsignal)
        runner.start()

    # primitive for setting a single color
    def _set(self, color, val):
        self._colors[color] = clamp(0, int(val), self.max_power)
        self.pz.set_PWM_dutycycle(self.pins[color], self._colors[color])

    @property
    def red(self):
        return self._colors['RED']

    @property
    def green(self):
        return self._colors['GREEN']

    @property
    def blue(self):
        return self._colors['BLUE']

    def clearall(self):
        # terminate any running animations
        self.killsignal.set()

        # power down pins
        for pin in self.pins.values():
            self.pz.set_PWM_dutycycle(pin, 0)


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
