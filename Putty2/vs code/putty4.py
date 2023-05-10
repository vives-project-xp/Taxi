import serial 
import time

ser = serial.Serial('COM6', 115200, timeout=1)
time.sleep(2)

while True:
    message = input("Enter a message to send to the Arduino: ")
    ser.write(message.encode())
    for i in range(len(message)):
        ser.write(b'1')
        time.sleep(0.1)
        ser.write(b'0')
        time.sleep(0.1)
    print(f"Sent: {message}")
    response = ser.readline().decode().rstrip()
    print(f"Received: {response}")