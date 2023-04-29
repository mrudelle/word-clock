import machine
from src.clock import Clock
from src.clock_face.word_clock_v2 import WordClockV2FR

i2c_bus = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26))

clock = Clock(i2c_bus, WordClockV2FR(), led_strip_pin=28)
clock.run()