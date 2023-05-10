# Importeer de seriële bibliotheek voor het communiceren met de motorcontroller
import serial

# Configureer de seriële poort voor communicatie met de motorcontroller
ser = serial.Serial('COM3', 115200)

# Configureer de beweging van de motor
beweging = "G1 X100 Y100" # Ga naar de positie X=100, Y=100
stappen_per_mm = 200 # Aantal stappen per millimeter van de motor

# Bereken het aantal stappen dat nodig is voor de beweging
x_steps = int(float(beweging.split("X")[1].split(" ")[0]) * stappen_per_mm)
y_steps = int(float(beweging.split("Y")[1]) * stappen_per_mm)

# Genereer de G-code
gcode = "G21\n" # Zet de eenheid naar millimeters
gcode += "G90\n" # Zet de modus naar absolute positionering
gcode += "G1 X{} Y{} F2000\n".format(x_steps, y_steps) # Beweeg de motor naar de opgegeven positie met een snelheid van 2000 mm/min

# Verzend de G-code naar de motorcontroller
ser.write(gcode.encode())