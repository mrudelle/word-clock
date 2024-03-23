import machine
from src.clock import Clock
from src.clock_face.word_clock import WordClockV1FR
from src.clock_face.word_clock_v2 import WordClockV2FR

IC2_SCL = 27
IC2_SDA = 26
LED_STRIP = 28

# Config Matt
CLOCK_FACE = WordClockV2FR()

# Config Pierre
# CLOCK_FACE = WordClockV1FR()


i2c_bus = machine.I2C(1, scl=machine.Pin(IC2_SCL), sda=machine.Pin(IC2_SDA))
clock = Clock(i2c_bus, CLOCK_FACE, led_strip_pin=LED_STRIP)
clock.run()