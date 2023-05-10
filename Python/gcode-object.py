import serial
import time
from mecode import G

# ser = serial.Serial('COM6', 115200)

time.sleep(2)

g_code = G(direct_write=True, 
    direct_write_mode="serial", 
    printer_port="COM6", 
    baudrate=115200)
move_string = str(g_code.move(0, 100,0))
g_code.move(x=0, y=10, z=0, F=1000)


bits = ''.join(format(ord(c)) for c in move_string)
ser.write(bits.encode())

ser.close()