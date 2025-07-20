import serial
import time
import bitmap_utils
import numpy as np

# Adjust this to match your Arduino's port (e.g. COM3 on Windows or /dev/ttyUSB0 on Linux/Mac)
SERIAL_PORT = "/dev/cu.usbmodem101"
BAUD_RATE = 9600              # must match Arduino's Serial.begin()

def read_serial(ser):
    if ser.in_waiting:
        try:
            line = ser.readline().decode("utf-8").strip()
            return line
        except Exception as e:
            print(f"Error: {e}")
    return None
