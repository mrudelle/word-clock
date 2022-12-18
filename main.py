import machine
import utime

from src.board.led_matrix import LEDMatrix
from src.rendering.screen_buffer import ScreenBuffer, scale_rgb_filter
from src.clock_face.word_clock import get_lines_for_time
from src.board.light_sensor import BH1750_I2C

lmatrix = LEDMatrix(10, 10, 12)
buff = ScreenBuffer(10, 10)

# i2c_bus = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))
# l_sens = BH1750_I2C(i2c_bus)

dcf = machine.Pin(11, machine.Pin.IN) # No pull-up for now

# print(i2c_bus.scan())


def amps_test():
    x = 0
    y = 0 

    while True:
        buff.draw_pixel(x, y, (100, 100, 100))
        lmatrix.write(buff.buffer)
        utime.sleep(0.2)
        x = x+1
        if x==10:
            y = (y+1) % 10
            x = 0


def hour_test():
    h = 0
    m = 0

    lmatrix.brightness = 1.0

    while True:
        buff.clear()
        lines = get_lines_for_time(h, m)
        buff.draw_lines(lines, (12, 100, 34))
        buff.filter(scale_rgb_filter(0.2))
        lmatrix.write(buff.buffer)
        utime.sleep(1)

        m = m+1
        if m == 60:
            h = (h+1) % 24
            m = 0

def trail_hour_test():
    h = 0
    m = 0

    lmatrix.brightness = .5
    buff.clear()

    while True:
        buff.filter(scale_rgb_filter(0.8))
        lines = get_lines_for_time(h, m)
        buff.draw_lines(lines, (12, 100, 34))
        lmatrix.write(buff.buffer)
        utime.sleep(1)

        m = m+1
        if m == 60:
            h = (h+1) % 24
            m = 0



#amps_test()
#hour_test()