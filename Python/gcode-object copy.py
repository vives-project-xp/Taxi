import mecode
import time

g = mecode.G(
    direct_write=True,
    two_way_comm=False,
    direct_write_mode="serial",
    printer_port="COM6",
    setup=False,
    baudrate=115200)

# g.absolute()
# g.setup()
g.write("G21 ", resp_needed=False)
g.write("G90 ", resp_needed=False)
g.write("G1 F1000 Y10 ", resp_needed=False)
# g.abs_move(x=0,y=10,z=0, F=1000)
g.teardown()  