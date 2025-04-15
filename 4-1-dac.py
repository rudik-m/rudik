import RPi.GPIO as GPIO
import time

DAC_PINS = [10, 9, 11, 5, 6, 13, 19, 26]  
LED_PIN = 17  

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC_PINS, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:
        try:
            num = int(input("Введите число от 0-255: "))
            if num < 0 or num > 255:
                print("Число должно быть от 0-255")
                continue
                
            GPIO.output(DAC_PINS, dec2bin(num))
            
            GPIO.output(LED_PIN, GPIO.HIGH if num > 127 else GPIO.LOW)
            
            voltage = 3.3 * num / 255
            print(f"Выходное напряжение: {voltage:.2f}V")
            
        except ValueError:
            print("Введите целое число")

finally:
    GPIO.output(DAC_PINS + [LED_PIN], 0)
    GPIO.cleanup()