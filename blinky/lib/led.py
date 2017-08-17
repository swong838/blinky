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

    def __init__(self):
        self.pz = pigpio.pi()
        for pin in self.pins.values():
            self.pz.set_mode(pin, pigpio.OUTPUT)

    def test_cycle(self):
        def effect(killsignal):
            pairs = (
                (self.pins['RED'], self.pins['GREEN']),
                (self.pins['GREEN'], self.pins['BLUE']),
                (self.pins['BLUE'], self.pins['RED'])
            )
            for pair in pairs:
                val1 = self.max_power
                val2 = 0
                while val2 < self.max_power and val1 > 0:
                    self._set(pair[0], val1)
                    self._set(pair[1], val2)
                    val2 += 1
                    val1 -= 1
                    sleep(self.rate)
                    if killsignal.is_set():
                        return
        self._animate('pulsing test cycle', effect)

    def setrgb(self, r=0, g=0, b=0):
        red = clamp(0, int(r), self.max_power)
        green = clamp(0, int(g), self.max_power)
        blue = clamp(0, int(b), self.max_power)

        self.killsignal.set()
        self._set(self.pins['RED'], red)
        self._set(self.pins['GREEN'], green)
        self._set(self.pins['BLUE'], blue)

    def _animate(self, name, effect):
        self.killsignal.set()
        self.killsignal = threading.Event()
        runner = Animation(name, effect, self.killsignal)
        runner.start()

    def _set(self, pin, val):
        self.pz.set_PWM_dutycycle(pin, val)

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
