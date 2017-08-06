import pigpio
from time import sleep
from copy import deepcopy
from .constants import Constants


class Led():

	pins = deepcopy(Constants.PINS)
	max_power = Constants.MAX
	rate = Constants.RATE

	def __init__(self):
		self.pz = pigpio.pi()
		for pin in self.pins.values():
			self.pz.set_mode(pin, pigpio.OUTPUT)

	def pulse(self, pins):
		val = 0
		while val <= self.max_power:
			for pin in self.pins.values():
				self.pz.set_PWM_dutycycle(pin, val)
				print(pin, val)
			val += 1
			sleep(self.rate)
		while val > 0:
			for pin in self.pins.values():
				self.pz.set_PWM_dutycycle(pin, val)
				print(pin, val)
			val -= 1
			sleep(self.rate)

	def test_cycle(self):
		self.clearall()
		for pin in self.pins.values():
			self.pz.set_PWM_dutycycle(pin, self.max_power)
			sleep(1)
			self.pz.set_PWM_dutycycle(pin, 0)
		self.clearall()

	def clearall(self):
		for pin in self.pins.values():
		    self.pz.set_PWM_dutycycle(pin, 0)


if __name__ == '__main__':
	l = Led()
	l.clearall()
