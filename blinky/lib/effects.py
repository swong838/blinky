from time import sleep
from random import random, randint

try:
    from .led import Led
except SystemError:
    from led import Led


class Effects(Led):

    @property
    def test_cycle(self):
        pairs = (
            ('RED', 'GREEN'),
            ('GREEN', 'BLUE'),
            ('BLUE', 'RED')
        )

        def effect(killsignal):
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

    @property
    def candle(self):
        pulse_range = (45, 75)          # milliseconds
        ranges = {                      # brightness range
            'RED': (215, 240),
            'GREEN': (31, 62),
            'BLUE': (13, 29)
        }

        def effect(killsignal):
            duration = self.get_phase_length(pulse_range)
            red = {
                'start': self.red,
                'end': randint(*ranges['RED'])
            }
            green = {
                'start': self.green,
                'end': randint(*ranges['GREEN'])
            }
            blue = {
                'start': self.blue,
                'end': randint(*ranges['BLUE'])
            }

            red['step'] = self.get_step(red['start'], red['end'], duration)
            green['step'] = self.get_step(green['start'], green['end'], duration)
            blue['step'] = self.get_step(blue['start'], blue['end'], duration)

            tick = 0
            while tick < duration:
                self._set('RED', self.red + red['step'])
                self._set('GREEN', self.green + green['step'])
                self._set('BLUE', self.blue + blue['step'])
                tick += 1
                sleep(.001)
                if killsignal.is_set():
                    return

        self._animate('candle', effect)
