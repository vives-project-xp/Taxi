/*
  Reading a serial ASCII-encoded string.

  This sketch demonstrates the Serial parseInt() function.
  It looks for an ASCII string of comma-separated values.
  It parses them into ints, and uses those to fade an RGB LED.

  Circuit: Common-Cathode RGB LED wired like so:
  - red anode: digital pin 3 through 220 ohm resistor
  - green anode: digital pin 5 through 220 ohm resistor
  - blue anode: digital pin 6 through 220 ohm resistor
  - cathode: GND

  created 13 Apr 2012
  by Tom Igoe
  modified 14 Mar 2016
  by Arturo Guadalupi

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/ReadASCIIString
*/

void setup() {
  // initialize serial:
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // if there's any serial available, read it:
  if (Serial.available() > 0) {

    char input = Serial.read();
    Serial.print("Received: ");
    Serial.println(input);
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
    delay(200);                      // wait for a second
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    delay(200);        
  }
}
