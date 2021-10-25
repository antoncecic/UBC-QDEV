# FastDAC Spectrum Analyzer
# by Anton Cecic

import time
import serial
import numpy as np

s = serial.Serial('COM3', 1750000, timeout=1)
#s = serial.Serial('COM6', 57600, timeout=1)

def Query(command):

    if not s.is_open:
        s.open()
    s.write(command)
    data = s.readline()
    data = data.decode('ascii', errors='ignore').rstrip('\r\n')
    s.close()
    return data

FastDAC_ID = Query(b"*IDN?\r")
print(FastDAC_ID)
