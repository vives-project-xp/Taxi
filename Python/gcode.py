y_pos = 1000
feed_rate = 100


g_code = "G21 ; Set units to millimeters\n"
g_code += "G90 ; Use absolute coordinates\n"
g_code += "G1 F{} Y{} ; Move the Y-axis by the specified distance at the specified feed rate\n".format(feed_rate, y_pos)

print(g_code)