import time

MONTH_KEY = ['na', 1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

def weekday_for(year, month, day):
    """ Sunday = 1, Monday = 2, ... """
    return ((year % 100) + int((year % 100) / 4) + day + MONTH_KEY[month] - 1) % 7

def dst_switch_days(year):
    # calculate "last Sunday of March"
    w_day_mar_31 = weekday_for(year, 3, 31)
    last_sunday_mar = 31 - (w_day_mar_31 + 6) % 7

    # calculate "last Sunday of October"
    w_day_oct_31 = weekday_for(year, 10, 31)
    last_sunday_oct = 31 - (w_day_oct_31 + 6) % 7

    return (last_sunday_mar, last_sunday_oct)

def utc_to_cet(t_utc):
    (year, month, day, _, _, _, weekday, yearday) = time.localtime(t_utc)
    
    (last_sunday_mar, last_sunday_oct) = dst_switch_days(year)

    # is in dst?
    is_cest = (month == 3 and day >= last_sunday_mar) or \
        (month > 3 and month < 10) or \
        (month == 10 and day < last_sunday_oct)
    
    return t_utc + 3600 * (2 if is_cest else 1)
    