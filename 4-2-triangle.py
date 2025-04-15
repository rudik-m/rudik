import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

inc_flag = 1
t = 0 
x = 0

try:
    period = float(input("Введите период сигнала: "))

    while True:
        GPIO.output(dac, decimal2binary(x))

        if   x == 0:    inc_flag = 1
        elif x == 255:  inc_flag = 0

        voltage = float(x) / 256.0 * 3.3
        print(f"Входное напряжение составляет примерно {voltage:.4} вольт")

        x = x + 1 if inc_flag == 1 else x - 1

        sleep(period/512)
        t += 1

except ValueError:
    print("Некорректный период")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP") 