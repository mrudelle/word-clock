import machine
from time import ticks_ms, ticks_add, ticks_diff, sleep_ms


def _wait_until(some_ticks):
    sleep_ms(ticks_diff(some_ticks, ticks_ms()))


class DCF77:

    def __init__(self, pin_number):
        self.pin = machine.Pin(pin_number, machine.Pin.IN)
    
    def wait_for_sync(self):
        """ 
        returns when a 59th second of sync is detected 
        returned value is the tick_ms at the start of the minute
        """

        check_period_ms = 50
        last_chirp = ticks_ms()
        next_check = ticks_add(last_chirp, check_period_ms)

        while True:
            _wait_until(next_check)
            
            if self.pin.value() == 1:
                last_chirp = ticks_ms()
                print('chirp')
            else:
                print('.', end='')
            
            if ticks_diff(ticks_ms(), last_chirp) > 1000:
                return ticks_ms()
            
            next_check = ticks_add(next_check, check_period_ms)
    
    def count_until(self, start_ms, end_ms, resolution_ms=10):
        count = 0
        next_check = ticks_add(start_ms, resolution_ms)

        while ticks_diff(end_ms, ticks_ms()) > 0:
            _wait_until(next_check)
            
            if self.pin.value() == 1:
                count += 1
                print('#', end='')
            else:
                print('.', end='')

            next_check = ticks_add(next_check, resolution_ms)
        
        return count

    def record_one_minute(self, minute_start):

        seconds = []

        record_start = ticks_add(minute_start, 500)
        _wait_until(record_start)

        for s_i in range(59):

            record_end = ticks_add(record_start, 1000)
            seconds += [self.count_until(record_start, record_end)]
            record_start = record_end
            
            print(f'    {s_i}: {seconds[s_i]}')
        
        return seconds
    
    
    def get_time(self):

        sync_tick = self.wait_for_sync()
        print('got a sync second')
        seconds = self.record_one_minute(sync_tick)



            





    