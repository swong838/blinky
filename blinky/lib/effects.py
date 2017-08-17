from time import sleep

try:
    from .led import Led
except SystemError:
    from led import Led


class Effects(Led):

    @property
    def test_cycle(self):
        def effect(killsignal):
            pairs = (
                ('RED', 'GREEN'),
                ('GREEN', 'BLUE'),
                ('BLUE', 'RED')
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

    @property
    def candle(self):
        ranges = {
            'RED': (175, 240),
            'GREEN': (121, 142),
            'BLUE': (33, 39)
        }

        def effect(killsignal):
            pass

        self._animate('candle', effect)
