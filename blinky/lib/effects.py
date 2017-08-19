from time import sleep
from random import randint
from pytweening import easeInOutExpo as ease

try:
    from .led import Led
except SystemError:
    from led import Led


class Effects(Led):

    @property
    def pulsered(self):

        self._ease_to(r=self.max_power)
        sleep(2)

        pulse_width = 1500

        def dopulse(killsignal):
            ticks = 0
            while ticks < pulse_width:
                progress = ticks / pulse_width
                self._set('RED', self.max_power - (self.max_power * ease(progress)))
                ticks += 1
                if killsignal.is_set():
                    return
                sleep(.001)
            sleep(2)
            ticks = 0
            while ticks < pulse_width:
                progress = ticks / pulse_width
                self._set('RED', self.max_power * ease(progress))
                ticks += 1
                if killsignal.is_set():
                    return
                sleep(.001)
            sleep(.5)

        self._animate('pulse_red', dopulse)

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
    def flare(self):
        pulses = (12, 45)
        colors = {
            'RED': (115, 215),
            'GREEN': (45, 51),
            'BLUE': (25, 115)
        }
        self._animate('flare', self._flicker_factory(colors, pulses))

    @property
    def candle(self):
        pulses = (45, 75)
        colors = {
            'RED': (215, 240),
            'GREEN': (51, 65),
            'BLUE': (23, 45)
        }
        self._animate('candle', self._flicker_factory(colors, pulses))

    @property
    def lamp_orange(self):
        self._ease_to(r=115, g=40, b=4)
        sleep(2)
        pulses = (45, 75)
        colors = {
            'RED': (115, 130),
            'GREEN': (40, 45),
            'BLUE': (4, 8)
        }
        self._animate('orange lamp', self._flicker_factory(colors, pulses))
