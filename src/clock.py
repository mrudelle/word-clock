import uasyncio
import time
import machine
import math

from src.board.led_matrix import LEDMatrix
from src.rendering.screen_buffer import ScreenBuffer, scale_rgb_filter
from src.board.light_sensor import BH1750_I2C
from src.board.pcf8523 import PCF8523
from src.board.ds3231 import DS3231
from src.utils.timezone_light import utc_to_cet
from src.rendering.matrix_code import MatrixCode

i2c_bus = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26))

REFRESH_RATE = 5  # FPS
CLOCK_COLOR = (211, 211, 255)
LUMINOSITY_COEF = 40

class Clock:

    def __init__(self, i2c_bus, clock_face, led_strip_pin=28) -> None:

        w = len(clock_face.FACE[0])
        h = len(clock_face.FACE)

        self.lmatrix = LEDMatrix(w, h, led_strip_pin)
        self.buff = ScreenBuffer(w, h)

        self.lmatrix.brightness = 0.2
        self.target_brightness = 0.2

        # self.rtc_module = PCF8523(i2c_bus)
        self.rtc_module = DS3231(i2c_bus)
        self.light_module = BH1750_I2C(i2c_bus)

        self.w = w
        self.h = h

        self.fps = REFRESH_RATE

        self.clock_face = clock_face

    async def refresh_screen(self):

        while True:
            
            weight = self.fps * 2
            self.lmatrix.brightness = (self.lmatrix.brightness * weight + self.target_brightness) / (weight + 1)
            self.lmatrix.write(self.buff.buffer)

            await uasyncio.sleep(1/self.fps)

    async def refresh_time(self):

        while True:

            # print(self.rtc_module.datetime)
            print(self.rtc_module.get_time())

            # with PCF8523 module:
            # (_, _, _, hours, minutes, seconds, _, _) = time.localtime(utc_to_cet(self.rtc_module.datetime))
            (_, _, _, hours, minutes, seconds, _, _) = time.localtime(
                utc_to_cet(time.mktime(self.rtc_module.get_time()))
            )

            # comment that part if you don't want an animation at 10pm
            if hours == 22 and minutes == 0:
                await self.matrix_code(duration_s=60)
                (_, _, _, hours, minutes, seconds, _, _) = time.localtime(
                    utc_to_cet(time.mktime(self.rtc_module.get_time()))
                )
            
            lines = self.clock_face.get_lines_for_time(hours, minutes)
            self.buff.clear()
            self.buff.draw_lines(lines, CLOCK_COLOR)

            # wait until next minute to refresh
            await uasyncio.sleep(61-seconds)
    
    async def matrix_code(self, duration_s=60):

        end = time.ticks_add(time.ticks_ms(), duration_s * 1000)
        m_code = MatrixCode(self.w, self.h, self.buff)
        frequency_ms = 5
        self.fps = 1000/frequency_ms

        while time.ticks_diff(end, time.ticks_ms()) > 0:
            
            m_code.refresh(frequency_ms)

            await uasyncio.sleep(frequency_ms/1000)
        
        self.fps = REFRESH_RATE

    async def get_luminosity_target(self):
        lux = await self.light_module.async_lux()
        return min(1.0, max(0.01, math.log2(lux+1) / LUMINOSITY_COEF))

    async def sample_brightness(self):

        while True:

            self.target_brightness = await self.get_luminosity_target()

            await uasyncio.sleep(1)

    async def main(self):

        uasyncio.create_task(self.refresh_screen())
        uasyncio.create_task(self.sample_brightness())

        await self.matrix_code(duration_s=5)

        uasyncio.create_task(self.refresh_time())

        while True:
            await uasyncio.sleep(1)
    
    def run(self):
        uasyncio.run(self.main())

    async def debug(self):

        m = 0
        h = 0
        
        while True:
            lines = self.clock_face.get_lines_for_time(h, m)
            self.buff.clear()
            self.buff.draw_lines(lines, CLOCK_COLOR)

            m = m+1
            if m > 59:
                h = (h+1)%24
                m = 0

            await uasyncio.sleep(.3)

    async def debug_task(self):

        uasyncio.create_task(self.refresh_screen())
        #uasyncio.create_task(self.sample_brightness())
        uasyncio.create_task(self.debug())

        while True:
            await uasyncio.sleep(1)

    def run_debug(self):
        uasyncio.run(self.debug_task())

