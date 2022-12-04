import utime

class BH1750_I2C:
    """ Taken from https://github.com/PinkInk/upylib/tree/master/bh1750 """

    PWR_OFF = 0x00
    PWR_ON = 0x01
    RESET = 0x07

    # modes
    CONT_LOWRES = 0x13
    CONT_HIRES_1 = 0x10
    CONT_HIRES_2 = 0x11
    ONCE_HIRES_1 = 0x20
    ONCE_HIRES_2 = 0x21
    ONCE_LOWRES = 0x23

    def __init__(self, bus, addr=0x23) -> None:
        self.bus = bus
        self.addr = addr
        self.off()
        self.reset()
    
    def set_mode(self, mode):
        self.mode = mode
        self.bus.writeto(self.addr, bytes([mode]))

    def off(self):
        self.set_mode(self.PWR_OFF)

    def on(self):
        self.set_mode(self.PWR_ON)
    
    def reset(self):
        self.on()
        self.set_mode(self.RESET)
    
    def luminance(self, mode):
        # continuous modes
        if mode & 0x10 and mode != self.mode:
            self.set_mode(mode)
        # one shot modes
        if mode & 0x20:
            self.set_mode(mode)
        # earlier measurements return previous reading
        utime.sleep_ms(24 if mode in (BH1750_I2C.ONCE_LOWRES, BH1750_I2C.CONT_LOWRES) else 180)
        data = self.bus.readfrom(self.addr, 2)
        factor = 2.0 if mode in (BH1750_I2C.CONT_HIRES_2, BH1750_I2C.ONCE_HIRES_2) else 1.0
        return (data[0]<<8 | data[1]) / (1.2 * factor)
    
    def lux(self):
        return self.luminance(BH1750_I2C.ONCE_HIRES_2)