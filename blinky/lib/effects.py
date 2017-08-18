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
        duration = 2000
        pulse_width = 1500
        red = {
            'start': self.red,
            'target': self.max_power,
            'diff': self.max_power - self.red
        }
        green = {
            'start': self.green,
            'target': 0,
            'diff': -self.green
        }
        blue = {
            'start': self.blue,
            'target': 0,
            'diff': -self.blue
        }

        # phase 1 - ease to red over 2 seconds
        def phase1(killsignal):
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

        def dopulse(killsignal):
            ticks = 0
            while ticks < pulse_width:
                progress = ticks / duration
                self._set('RED', self.max_power - (self.max_power * ease(progress)))
                ticks += 1
                if killsignal.is_set():
                    return
                sleep(.001)

            ticks = 0
            while ticks < pulse_width:
                progress = ticks / duration
                self._set('RED', self.max_power * ease(progress))
                ticks += 1
                if killsignal.is_set():
                    return
                sleep(.001)

            pass

        self._animate('pulse_red_in', phase1)
        sleep(2)
        self._set('RED', self.max_power)
        self._set('GREEN', 0)
        self._set('BLUE', 0)
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
        effect = self._flicker_factory(colors, pulses)
        self._animate('flare', effect)

    @property
    def candle(self):
        pulses = (45, 75)
        colors = {
            'RED': (215, 240),
            'GREEN': (51, 65),
            'BLUE': (23, 45)
        }
        effect = self._flicker_factory(colors, pulses)
        self._animate('candle', effect)

    def _flicker_factory(self, color_ranges, pulse_ranges):
        def effect(killsignal):
            duration = self.get_phase_length(pulse_ranges)
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
        return effect
