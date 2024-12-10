import RPi.GPIO as GPIO
import sys
from time import sleep

# Define numbering scheme and channels used
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
motor_channel = [7,11,13,15]
motor_channel.reverse()

# Define number of steps and time between steps
step_sleep = 0.0025
steps = 150

GPIO.setup(motor_channel, GPIO.OUT) # Set channels as output
try:
    for i in range(steps):
        print("step:", (i + 1))
        GPIO.output(motor_channel, (1,0,0,0))
        sleep(step_sleep)
        GPIO.output(motor_channel, (0,1,0,0))
        sleep(step_sleep)
        GPIO.output(motor_channel, (0,0,1,0))
        sleep(step_sleep)
        GPIO.output(motor_channel, (0,0,0,1))
        sleep(step_sleep)
    GPIO.cleanup()
    sys.exit(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(1)
