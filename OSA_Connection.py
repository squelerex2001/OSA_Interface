"""
This program communicate with the AQ6315A OSA
It uses the GP-IB VISA port with a PROLOGIX GPIB/USB adaptator
the port is then considered to be a COM Serial port
"""
import serial
import time

def write(cmd):
    OSA.write((cmd + '\n').encode())
def read():
    return OSA.read_all().decode()
def query(cmd):
    write(cmd)
    write('++read eoi')
    time.sleep(0.5)
    return read()
def initializePrologix() -> None:
    write('++mode 1')
    write('++auto 0')
    write('++addr 2')
    write('++eoi 1')
    write('++eos 3')

# Osa port
OSA_PORT = "COM5"
# Opening the OSA port
OSA = serial.Serial(OSA_PORT, timeout=1)

initializePrologix()
# Communication test
print("Start WL:", query('STAWL?'))
print("Stop WL:", query('STPWL?'))

# Closing the serial port
OSA.close()
