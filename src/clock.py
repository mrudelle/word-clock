import uasyncio
import time
import machine
import math

from src.board.led_matrix import LEDMatrix
from src.rendering.screen_buffer import ScreenBuffer, scale_rgb_filter
from src.clock_face.word_clock import get_lines_for_time
from src.board.light_sensor import BH1750_I2C
from src.board.pcf8523 import PCF8523

i2c_bus = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26))

REFRESH_RATE = 5  # FPS
CLOCK_COLOR = (255, 255, 255)
LUMINOSITY_COEF = 40

class Clock:

    def __init__(self, i2c_bus, w=10, h=10, led_strip_pin=28) -> None:

        self.lmatrix = LEDMatrix(w, h, led_strip_pin)
        self.buff = ScreenBuffer(w, h)

        self.lmatrix.brightness = 0.2
        self.target_brightness = 0.2

        self.rtc_module = PCF8523(i2c_bus)
        self.light_module = BH1750_I2C(i2c_bus)

    async def refresh_screen(self):

        while True:
            
            weight = REFRESH_RATE * 2
            self.lmatrix.brightness = (self.lmatrix.brightness * weight + self.target_brightness) / (weight + 1)
            self.lmatrix.write(self.buff.buffer)

            await uasyncio.sleep(1/REFRESH_RATE)

    async def refresh_time(self):

        while True:

            (_, _, _, hours, minutes, seconds, _, _) = time.localtime(self.rtc_module.datetime)

            # TODO: adjust for DST
            
            lines = get_lines_for_time(hours, minutes)
            self.buff.clear()
            self.buff.draw_lines(lines, CLOCK_COLOR)

            # wait until next minute to refresh
            await uasyncio.sleep(61-seconds)

    def get_luminosity_target(self):
        lux = self.light_module.lux()
        return min(1.0, max(0.01, math.log2(lux+1) / LUMINOSITY_COEF))

    async def sample_brightness(self):

        while True:

            self.target_brightness = self.get_luminosity_target()

            await uasyncio.sleep(1)

    async def main(self):

        uasyncio.create_task(self.refresh_screen())
        uasyncio.create_task(self.refresh_time())
        uasyncio.create_task(self.sample_brightness())

        while True:
            await uasyncio.sleep(1)
    
    def run(self):
        uasyncio.run(self.main())
