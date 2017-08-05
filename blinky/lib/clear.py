import pigpio
from constants import Constants


pz = pigpio.pi()
pz.set_mode(RED, pigpio.OUTPUT)
pz.set_mode(GREEN, pigpio.OUTPUT)
pz.set_mode(BLUE, pigpio.OUTPUT)

def clearall():
    pz.set_PWM_dutycycle(RED, 0)
    pz.set_PWM_dutycycle(GREEN, 0)
    pz.set_PWM_dutycycle(BLUE, 0)

if __name__ == '__main__':
    clearall()
