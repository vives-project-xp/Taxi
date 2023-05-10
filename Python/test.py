import serial
import time
ser = serial.Serial('COM6', 115200)  # Replace with the appropriate serial port and baud rate for your driver

time.sleep(2)

y_distance = 11
feed_rate = 1000
y_distance2 = 0

g_code = "G21 ; Set units to millimeters\n"
g_code += "G91 ; Use relative coordinates\n"
g_code += "G1 F{} Y{} ; Move the Y-axis by the specified distance at the specified feed rate\n".format(feed_rate, y_distance)

g_code2 = "G21 ; Set units to millimeters\n"
g_code2 += "G91 ; Use relative coordinates\n"
g_code2 += "G1 F{} Y{} ; Move the Y-axis by the specified distance at the specified feed rate\n".format(feed_rate, y_distance2)

ser.write(g_code.encode())
time.sleep(0.01)
ser.write(g_code2.encode())

ser.close()