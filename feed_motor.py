import RPi.GPIO as GPIO
import sys
from time import sleep

# Define numbering scheme and channels used
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
motor_channel = [16,18,22,36]
motor_channel.reverse() # Reverse list to make the direction correct

steps = 60 # Around 60 is good number for the wheel used to make it rotate one hole
step_sleep = 0.02 # Interval is fast enough for the use of this motor

GPIO.setup(motor_channel, GPIO.OUT) # Set channels as output
try:
    for i in range(steps):
        print("step:", (i + 1))
        GPIO.output(motor_channel, (1,1,0,0))
        sleep(step_sleep)
        GPIO.output(motor_channel, (0,1,1,0))
        sleep(step_sleep)
        GPIO.output(motor_channel, (0,0,1,1))
        sleep(step_sleep)
        GPIO.output(motor_channel, (1,0,0,1))
        sleep(step_sleep)
    GPIO.cleanup()
    sys.exit(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(1)
