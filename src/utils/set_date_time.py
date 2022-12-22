import machine
import time

from src.board.pcf8523 import PCF8523

i2c_bus = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26))
rtc = PCF8523(i2c_bus)

#### Set the date here as UTC ####
year = 2022
month = 12
day = 22

hours = 22
minutes = 13
seconds = 0
#### Set the date here as UTC ####


rtc.datetime = (year, month, day, hours, minutes, seconds, 0, 0)

time.sleep(1)

(year, month, day, hours, minutes, seconds, weekday, yearday) = time.localtime(rtc.datetime)
print(f"Time set to {year}.{month}.{day} {hours}:{minutes}:{seconds} weekday: {weekday}, yearday: {yearday}" )


