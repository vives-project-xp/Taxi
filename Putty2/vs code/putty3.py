import serial 

arduinoData = serial.Serial('com6', 115200)

def led_on():
    arduinoData.Write('1') 

    def led_off():
        arduinoData.Write('0')

t=0
while (t<2000):
    if(t %10 == 0):
        print(t)
    t+=1

led_on()

print("Done")

