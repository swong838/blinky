import threading


class Animation(threading.Thread):

    name = ''

    def __init__(self, name, effect, killsignal):
        super(Animation, self).__init__()
        self.name = name
        self.killsignal = killsignal
        self.effect = effect

    def run(self):
        while not self.killsignal.is_set():
            self.effect()
