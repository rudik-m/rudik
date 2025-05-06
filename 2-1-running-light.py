import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pins = [2, 3, 4, 17, 27, 22, 18, 9]

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

try:
    while True:
        for pin in led_pins:

            for p in led_pins:
                GPIO.output(p, False)

            GPIO.output(pin, True)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()