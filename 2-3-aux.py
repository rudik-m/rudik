import RPi.GPIO as GPIO
import time

aux = [21, 20, 26, 16, 19, 25, 23, 24]
leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setmode(GPIO.BCM)

for pin in leds:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

for pin in aux:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        for i in range(len(aux)):
            if GPIO.input(aux[i]) == 0:  
                GPIO.output(leds[i], True)
            else:
                GPIO.output(leds[i], False)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()