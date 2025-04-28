"""
Note:
Use this code to test onto one RP2040 with the potentiometer and servo both on the ONE board
"""
from machine import Pin, ADC, PWM
import time

# --- Setup pins ---
potentiometer = ADC(Pin(26))  # potentiometer is connected to GP26 (ADC0)
servo = PWM(Pin(15))          # Servo signal connected to GP15

# --- Configure PWM for servo ---
servo.freq(50)  # Standard 50 Hz for servo motors

def set_servo_angle(angle):
    # Servo expects a duty cycle between ~3% and ~12%
    #RP2040 can take duty of 65535 but we put a min and max to stop it from going further
    min_duty = 1000  # corresponds to 0 degrees (in microseconds)
    max_duty = 9000  # corresponds to 180 degrees (in microseconds)
    duty = int(min_duty + (max_duty - min_duty) * angle / 180)
    servo.duty_u16(duty)

while True:
    pot_value = potentiometer.read_u16()  # Read potentiometer duty (0-65535)
    angle = (pot_value / 65535) * 180      # Map to 0–180 degrees
    set_servo_angle(angle)
    time.sleep(0.02)  # Short delay
