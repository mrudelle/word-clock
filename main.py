import machine
import utime

from led_matrix import LEDMatrix
from screen_buffer import ScreenBuffer
from word_clock import get_lines_for_time
from light_sensor import BH1750_I2C

lmatrix = LEDMatrix(10, 10, 12)
buff = ScreenBuffer(10, 10)

i2c_bus = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))
l_sens = BH1750_I2C(i2c_bus)

print(i2c_bus.scan())


def amps_test():
    x = 0
    y = 0 

    while True:
        buff.draw_pixel(x, y, (255, 255, 255))
        lmatrix.write(buff.buffer)
        utime.sleep(0.2)
        x = x+1
        if x==10:
            y = (y+1) % 10
            x = 0


h = 0
m = 0

lmatrix.brightness = 0.1

while True:
    buff.clear()
    lines = get_lines_for_time(h, m)
    buff.draw_lines(lines, (12, 100, 34))
    lmatrix.write(buff.buffer)
    utime.sleep(1)

    m = m+1
    if m == 60:
        h = (h+1) % 24
        m = 0