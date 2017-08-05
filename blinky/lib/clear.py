import pigpio

RED = 13
GREEN = 19
BLUE = 26
timer = .01
MAX = 240

pz = pigpio.pi()
pz.set_mode(RED, pigpio.OUTPUT)
pz.set_mode(GREEN, pigpio.OUTPUT)
pz.set_mode(BLUE, pigpio.OUTPUT)

pz.set_PWM_dutycycle(RED, 0)
pz.set_PWM_dutycycle(GREEN, 0)
pz.set_PWM_dutycycle(BLUE, 0)
