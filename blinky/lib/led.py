import pigpio
from time import sleep
from constants import Constants

pz = pigpio.pi()

def initialize():
	for pin in Constants.PINS.values():
		pz.set_mode(pin, pigpio.OUTPUT)


def pulse(pins):
	val = 0
	while val <= MAX:
		for pin in pins:
			pz.set_PWM_dutycycle(pin, val)
			print(pin, val)
		val += 1
		sleep(timer)
	while val > 0:
		for pin in pins:
			pz.set_PWM_dutycycle(pin, val)
			print(pin, val)
		val -= 1
		sleep(timer)


def clearall():
	initialize()
	for pin in Constants.PINS.values():
	    pz.set_PWM_dutycycle(pin, 0)

if __name__ == '__main__':
    clearall()
