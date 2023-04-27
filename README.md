# Fake-Taxi 

<h1>What your project does</h1>
The project concerning the taxi will lift the taxi on it's backwheels using a mechanical system supported by a motor (42BYG-40015-22B). The motor has a 3D print attached to it.
This motor is connected to the Gshield V5b which is alo connected to the arduino uno microcontroller. Using specific software we're able to lift the taxi from the ground.
<br></br>
<img src="./fotoTaxi.png" alt="taxifoto" width=600px>


<h1>How to install it</h1>
Used program links:
<p>- Tinkercad (for controlling the engine): https://www.tinkercad.com/ </p>
<p>- Universal gcode: https://universalgcodesender.com/download/ </p>
<p>- Arduino IDE: https://www.arduino.cc/en/software </p>
<p>- Serial import in Python (commands): conda create --name helloworld ,
conda activate helloworld ,
conda env list (om alle environments te zien)</p>

<h1>How do we send code to the motor?</h1>
We use a gshield v5b as a motor driver (it has 3 drivers, we used Y). With GRBL this Gshield can communicate with an Arduino Uno which is attatched to it.
With serial data input from TX to RX we can send our code to make the motor run to the Arduino, using GCODE. Below this you see a code snippet from our code in Python.



<h1>Example usage</h1>
<p>- Tinkercad: </p>
<p>- Universal gcode: </p>
<p>1. Open Arduino IDE --> file --> examples --> grbl --> grblUpload: execute</p>
<p>2. UGS: open and connect</p>
<p>3. Now use the GUI at the left to make the motor turn</p>
<p>- Arduino IDE: </p>

<b>(in te vullen door Colin)</b>

<p>-Arduino test code Hello World:</p>
<img src= "./codeArduino.PNG" alt="code" width=600px>

<p>-Python code for sending Hello world to Arduino Uno and get a blinking rgb led:</p>
<img src= "./codePython.PNG" alt="code" width=600px>


<h1>How to set up the dev environment</h1>

<h1>How to ship a change</h1>

<h1>Change log</h1>

<h1>License and author info</h1>
Made by Esteban Desmet, Colin Bossuyt, Xander Vyvey and Alberiek Depreytere in 2023 for VIVES.