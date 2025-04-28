from machine import Pin, ADC, UART
import time

# Setup
potentiometer = ADC(Pin(26))  # ADC0
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))  # UART0 on GP0 and GP1

while True:
    pot_value = potentiometer.read_u16()
    angle = (pot_value / 65535) * 180
    min_duty = 1000
    max_duty = 9000
    duty = int(min_duty + (max_duty - min_duty) * angle / 180)

    # Send duty over UART
    uart.write(str(duty) + '\n')  # send duty as a line of text

    time.sleep(0.02)  # short delay
