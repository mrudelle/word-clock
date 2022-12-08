import machine
from time import ticks_ms, ticks_add, ticks_diff, sleep_ms


def _wait_until(some_ticks):
    sleep_ms(ticks_diff(some_ticks, ticks_ms()))


DCF77_COEF = [1, 2, 4, 8, 10, 20, 40, 80] 


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
    
    def count_until(self, start_ms, end_ms, resolution_ms):
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

    def record_one_minute(self, minute_start, resolution_ms=50):

        seconds = []

        record_start = ticks_add(minute_start, 500)
        _wait_until(record_start)

        for s_i in range(59):

            record_end = ticks_add(record_start, 1000)
            seconds += [self.count_until(record_start, record_end, resolution_ms)]
            record_start = record_end
            
            print(f'    {s_i}: {seconds[s_i]}')
        
        return seconds
    
    def parse_minute(self, data, threshold):

        data_bin = [d >= threshold for d in data]

        def decode_int(bin):
            res = 0
            for i, b in enumerate(bin):
                if b:
                    res += DCF77_COEF[i]
        
        def check_parity(bin):
            res = 0
            for b in bin:
                if b:
                    res += 1
            return res % 2 == 0

        d_a1 = data_bin[16]
        d_cet = data_bin[17]
        d_cest = data_bin[18]
        d_a2 = data_bin[19]

        d_s = data_bin[20]

        minutes = decode(data_bin[21:28])
        hours = decode(data_bin[29:35])

        day = decode(data_bin[36:42])
        weekday = decode(data_bin[42:45])
        month = decode(data_bin[45:50])
        year = decode(data_bin[50:58]) + 2000  # safe bet

        m_check = check_parity(data_bin[21:29])
        h_check = check_parity(data_bin[29:36])
        date_check = check_parity(data_bin[36:59])

        checks = [m_check, h_check, date_check, d_s, d_cet != d_cest]  # not d_a1, not d_a2,

        return (checks, year, month, day, weekday, hours, minutes)
    
    def get_time(self):

        sync_tick = self.wait_for_sync()
        print('got a sync second')
        seconds = self.record_one_minute(sync_tick, resolution_ms=5)
        (checks, year, month, day, weekday, hours, minutes) = self.parse_minute(seconds, threshold=30)

        if False in checks:
            print(f'Extended checks failed: {checks}')
        
        if False in checks[0:2]:
            print(f'Failed time checks')
        else:
            print(f'Time: {hours}:{minutes} {day}.{month}.{year} ({weekday})')
