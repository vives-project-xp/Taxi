# Fake-Taxi 
<h1> Content</h1>
<ul>
<li> What's our goal</li>
<li> How does it work?</li>
<li> The programs we used (and how to install them)</li>
<li> How do we send code to the motor?</li>
<li> How to use the programs?</li>
<li> Problem we experienced</li>
<li> Parts</li>
<li> How to set up the dev environment</li>
<li> How to ship a change</li>
<li> Change log</li>
<li> License and author info</li>
<li> GIT Pushes</li>
</ul>
<h1>What your project does</h1>
With this project we created a taxi that will go up on it's backwheels so it'll jump up and down. We also made a speaker system to output some noises. This taxi will then later be implemented in an escape room.
<br></br>
<img src="./fotoTaxi.png" alt="taxifoto" width=600px>
<h1>How does it work?</h1>
To lift the taxi we use a mechanical system made with some maker beams, supported by a stepping motor (42BYG-40015-22B). The motor has a 3D print attached to it. The 3D goes up for 90 degrees and then goes down to it original location, it does this movement for about 5 times. The print pushes against an U-form profile at the back of the taxi, this makes the taxi go up and down. The motor is connected to the Gshield V5b which is connected to an arduino uno microcontroller. Using specific software we're able to lift the taxi from the ground.
<br></br>
<img src="./controller.jpg" alt="controllerfoto" width=350px> <img src="./opstelling.jpg" alt="opstellingfoto" width=350px>
<h1>The programs we used (and how to install them)</h1>
Used program links:
<ul>
<li>Tinkercad (for our 3D print): https://www.tinkercad.com/</li>
<li>Universal gcode: https://universalgcodesender.com/download/</li>
<li>Arduino IDE: https://www.arduino.cc/en/software</li>

</ul>
<h1>How do we send code to the motor?</h1>
We use a gshield v5b as a motor driver (it has 3 drivers, we used Y). With the GRBL library this Gshield can communicate with an Arduino Uno which is attatched to it.
With serial data input from TX to RX we can send our code to make the motor run to the Arduino, using GCODE. Below this you see a code snippet from our code in Python.
Initially, we used Universal gcode to let the motor turn around, later on we programmed this ourself in Python.

<h1>How does the speaker work?</h1>
To drive our speaker, we use Velleman's MP3 player. (WMAH202N).

This player immediately plays the sound signal when the power supply voltage is applied through the audio cables (left neutral right). These voltages can be compared to the normal voltages from a telephone. Of course, this signal needs to be amplified if we were to simply connect this to a box. 

For that I use a BC547 coupling transistor amplifier. This is made as simple as possible to reduce the cost and all parts are commonly available. 

The amplifier consists of:
2x one microfarad capacitors 
1x 10k Ohm potentiometer
2x BC547 transistor

The 2 capacitors are placed in parallel this way we can add up the values and reach a capacitor value of about 2.2 microfarad which is expected.

The potentiometer allows us to control the sound.

The transistors allow us to place the supply voltage and the input signal amplified on the box.

In our speaker setup, we only want the speaker to play 1 sound when desired.

However, the applications of our MP3 player are much more than that. Besides the usual pulse light, indicating whether the player is working or not, we can also pause the sound, take next sound or return to the previous song.
To accomplish this, the creator suggests a push button.
However, this causes dender with most inexpensive switches. A phenomenon where multiple presses are accomplished because the contact vibrates or thunders. However, this is not desirable with us because we only want to move forward one song, also we wish to have everything automated and in this application immediate human input is needed to realize this. Therefore, it is better to use a transistor. This way we are sure that the signal will be passed only once.
It can then be controlled by a microcontroller or PLC, for example.

We can get dender from the PLC though this we can solve with a Schmitt Trigger or low pass filter.
Juxebox: https://whadda.com/product/mp3-jukebox-module-wmah202n/ 
<br></br>
<img src="./bord.jpg" alt="juxebox" width=400px> 
<img src="./datasheet.png" alt="datasheet" width=400px> 
<img src="./tekening.png" alt="tekening" > 
<img src="./tekening2.png" alt="tekening2"> 

<h1>How to use the programs?</h1>
<ul>
<li>Universal gcode (to let the motor turn): 
<ol>
<li>Open Arduino IDE --> file --> examples --> grbl --> grblUpload: execute</li>
<li>UGS: open and connect</li>
<li>Now use the GUI at the left to make the motor turn </li>
</ol></li>
<br></br>
<li>Arduino IDE: 
1. Code to implement the gcode to Arduino:
<br></br>

```pt

File>Examples>grbl>grblUpload

This sketch compiles and uploads Grbl to your 328p-based Arduino! 

To use:
- First make sure you have imported Grbl source code into your Arduino
  IDE. There are details on our Github website on how to do this.

- Select your Arduino Board and Serial Port in the Tools drop-down menu.
  NOTE: Grbl only officially supports 328p-based Arduinos, like the Uno.
  Using other boards will likely not work!

- Then just click 'Upload'. That's it!

For advanced users:
  If you'd like to see what else Grbl can do, there are some additional
  options for customization and features you can enable or disable. 
  Navigate your file system to where the Arduino IDE has stored the Grbl 
  source code files, open the 'config.h' file in your favorite text 
  editor. Inside are dozens of feature descriptions and #defines. Simply
  comment or uncomment the #defines or alter their assigned values, save
  your changes, and then click 'Upload' here. 

Copyright (c) 2015 Sungeun K. Jeon
Released under the MIT-license. See license.txt for details.


#include <grbl.h>

// Do not alter this file!

```
</li>
<li>Python code (programmed in Visual Studio Code)
<ol>
<li>Code for the communication between arduino. When the input is hello world the led of the arduino turns on. We used this as a first test to see if everything works.
<br></br>

```pt

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

```
</li>
<li>Gcode generator code:
<br></br>

```pt

mport serial
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


Test met library mecode die niet werkt:
import mecode
import time

g = mecode.G(
    direct_write=True,
    two_way_comm=False,
    direct_write_mode="serial",
    printer_port="COM6",
    setup=False,
    baudrate=115200)

(#) g.absolute()
(#) g.setup()
g.write("G21 ", resp_needed=False)
g.write("G90 ", resp_needed=False)
g.write("G1 F1000 Y10 ", resp_needed=False)
(#) g.abs_move(x=0,y=10,z=0, F=1000)
g.teardown()

```

</li>
</ol>
<li>Serial import in Python (commands):
<br></br>

```pt
conda create --name helloworld
conda activate helloworld 
conda env list 

```

</li></li><li>
<p>Arduino test code Hello World (screenshot):</p>
<img src= "./codeArduino.PNG" alt="code" width=600px>
</li>
</ul>

<h1>Problem we experienced</h1>

Because we only use a simple stepping motor, the real taxi (weight is more than 2.5kg) can't lift up. To show the system itself does work, we used a taxi in cardboard. But if you have a heavier motor, it should have to work perfectly.

<h1>Parts</h1>
<ul>
<li>Stepping motor, datasheet: https://media.digikey.com/pdf/Data%20Sheets/Makeblock%20PDFs/81042_Web.pdf</li>
<li>Arduino Uno</li>
<li>Gshield v5b</li>
</ul>
<h1>GIT Pushes</h1>
<ul>
<li>Code</li>
<li>Powerpoint</li>
<li>Video</li>
<li>Pictures</li>
<li>Planning</li>
</ul>

<h1>Link to video and powerpoint</h1>
https://vivesonline-my.sharepoint.com/:f:/g/personal/r0929537_student_vives_be/EhgBkyU8gPBFs8h8WDk01EUBaExMeiYeV6tWr5XbjaU0Lg?e=gprzPR


<h1>License and author info</h1>

Made by Esteban Desmedt, Colin Bossuyt, Xander Vyvey and Alberiek Depreytere in 2023 for VIVES.
Contact (email Xander): xander.vyvey@student.vives.be