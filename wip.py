import machine
import time
import math

from src.board.led_matrix import LEDMatrix
from src.rendering.screen_buffer import ScreenBuffer, scale_rgb_filter
from src.clock_face.word_clock import get_lines_for_time
from src.board.light_sensor import BH1750_I2C
from src.board.pcf8523 import PCF8523
from src.clock import Clock

lmatrix = LEDMatrix(10, 10, 28)
lmatrix.brightness = 0.2
buff = ScreenBuffer(10, 10)

i2c_bus = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26))


#dcf = machine.Pin(11, machine.Pin.IN) # No pull-up for now

rtc_module = PCF8523(i2c_bus)
light_module = BH1750_I2C(i2c_bus)

(year, month, day, hours, minutes, seconds, weekday, yearday) = time.localtime(rtc_module.datetime)
print(f"It is {year}.{month}.{day} {hours}:{minutes}:{seconds} weekday: {weekday}, yearday: {yearday}" )

# set pi pico rtc time based on the rtc module's time
#time.time.localtime(rtc.datetime)

CLOCK_COLOR = (255, 255, 255)


def refresh_screen():
    lmatrix.write(buff.buffer)

def get_luminosity_target():
    lux = light_module.lux()
    return min(1.0, max(0.01, math.log2(lux+1) / 20.0))

def refresh_luminosity():

    while True:
        lux = light_module.lux()
        
        lmatrix.brightness = (lmatrix.brightness * 20 + get_luminosity_target()) / 21

        new_brightness = min(1.0, max(0.01, math.log2(lux+1) / 20.0))
        lmatrix.brightness = (lmatrix.brightness * 20 + new_brightness) / 21

        print(f'luminosity {lmatrix.brightness}')
        refresh_screen()

        time.sleep(0.5)
    


def refresh_time():

    (_, _, _, hours, minutes, seconds, _, _) = time.localtime(rtc_module.datetime)

    # TODO: adjust for DST
    
    lines = get_lines_for_time(hours, minutes)
    buff.clear()
    buff.draw_lines(lines, CLOCK_COLOR)
    refresh_screen()

    # TODO: wait til next minute to refresh
    #time.sleep(61-seconds)


def amps_test():
    x = 0
    y = 0 

    while True:
        buff.draw_pixel(x, y, (100, 100, 100))
        lmatrix.write(buff.buffer)
        time.sleep(0.2)
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
        time.sleep(1)

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
        time.sleep(1)

        m = m+1
        if m == 60:
            h = (h+1) % 24
            m = 0



#amps_test()
#hour_test()

#refresh_time()


