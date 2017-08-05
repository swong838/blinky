import pigpio
from time import sleep

RED = 13
GREEN = 19
BLUE = 26
timer = .0025
MAX = 225

pz = pigpio.pi()
pz.set_mode(RED, pigpio.OUTPUT)
pz.set_mode(GREEN, pigpio.OUTPUT)
pz.set_mode(BLUE, pigpio.OUTPUT)


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


if __name__ == "__main__":
	groups = (
	{RED, GREEN, BLUE},
	#	{RED},
	#	{RED, GREEN},
	#	{GREEN},
	#	{GREEN, BLUE},
	#	{BLUE},
	#	{BLUE, RED}
	)
	index = 0
	while True:
		index = index % len(groups)
		pulse(groups[index])
		index += 1
