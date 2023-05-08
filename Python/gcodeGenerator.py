import serial
import time

ser = serial.Serial('COM6', 115200)


time.sleep(2)

y_pos = -11
feed_rate = 1000
y_pos2 = 0

g_code = "G21 \n"
g_code += "G90 \n"
g_code += "G01 F{} Y{} \n".format(feed_rate, y_pos)

g_code2 = "G21 \n"
g_code2 += "G90 \n"
g_code2 += "G01 F{} Y{} \n".format(feed_rate, y_pos2)

for i in range (3):
    ser.write(g_code.encode())
    ser.write(g_code2.encode())

ser.close()

