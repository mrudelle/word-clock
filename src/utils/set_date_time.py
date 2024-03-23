import machine
import time

from src.board.pcf8523 import PCF8523
from src.board.ds3231 import DS3231

i2c_bus = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26))

#### Set the date here as UTC ####
year = 2024
month = 3
day = 23

hours = 14
minutes = 47
seconds = 00
#### Set the date here as UTC ####


# rtc = PCF8523(i2c_bus)
# rtc.datetime = (year, month, day, hours, minutes, seconds, 0, 0)
# time.sleep(1)
# (year, month, day, hours, minutes, seconds, weekday, yearday) = time.localtime(rtc.datetime)


rtc = DS3231(i2c_bus)
rtc.set_time([year, month, day, hours, minutes, seconds, 0, 0])
time.sleep(1)
print(rtc.get_time())
(year, month, day, hours, minutes, seconds, weekday, yearday) = rtc.get_time()

print(f"Time set to {year}.{month}.{day} {hours}:{minutes}:{seconds} weekday: {weekday}, yearday: {yearday}" )


