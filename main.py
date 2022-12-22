import machine
from src.clock import Clock

i2c_bus = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26))

clock = Clock(i2c_bus)
#clock.run()