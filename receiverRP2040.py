from machine import Pin, PWM, UART
import time

# Setup
servo = PWM(Pin(15))  # Servo connected to GP15
servo.freq(50)

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))  # UART0 again

buffer = ''

while True:
    if uart.any():
        data = uart.read(1)  # read 1 byte at a time
        if data:
            char = data.decode()
            if char == '\n':
                # full message received
                try:
                    duty = int(buffer)
                    servo.duty_u16(duty)
                except ValueError:
                    pass  # ignore bad messages
                buffer = ''  # reset buffer
            else:
                buffer += char

    time.sleep(0.01)  # small delay
