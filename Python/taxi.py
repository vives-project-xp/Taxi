import serial
import time


ser = serial.Serial('COM6', 115200)


time.sleep(2)


command = input("Enter a command: ")


if command == "hello world":
  ser.write(command.encode())
  time.sleep(1)
  ser.write(b'off') 

ser.close()