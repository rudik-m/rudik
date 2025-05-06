import RPi.GPIO as GPIO
import time


dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

for pin in dac:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

try:
    while True:
        for i in range(256):
            for bit_position in range(8):
                bit = (i >> bit_position) & 1
                GPIO.output(dac[bit_position], bit)

            time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()