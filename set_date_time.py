import machine
import time

from src.board.pcf8523 import PCF8523

i2c_bus = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26))
rtc = PCF8523(i2c_bus)

year = 2022
month = 12
day = 21

hours = 22
minutes = 58
seconds = 0

weekday = 2  # monday: 0

rtc.datetime = (year, month, day, hours, minutes, seconds, weekday, 0)

time.sleep(1)

(year, month, day, hours, minutes, seconds, weekday, yearday) = rtc.datetime
print(_time)
print(f"Time set to {year}.{month}.{day} {hours}:{minutes}:{seconds} weekday: {weekday}, yearday: {yearday}" )


