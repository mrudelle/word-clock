import neopixel
import machine

class LEDMatrix:
    """ Origin: Top Left """

    def __init__(self, w, h, pin_number):
        self.w = w
        self.h = h
        self.brightness = 1.0
        self.pin = machine.Pin(pin_number, machine.Pin.OUT)
        self.n = neopixel.NeoPixel(self.pin, w * h)
    
    def write(self, data):

        for y, r in enumerate(data):
            for x, l in enumerate(r):
                # print(f'({x},{y}) -> {self.led_index(x, y)}')
                self.n[self.led_index(x, y)] = [int(l_c * self.brightness) for l_c in l]
        
        self.n.write()
    
    def led_index(self, x, y):
        # Horizontal lines starting top left
        return y * self.w + (x if y%2 == 0 else self.w-(x+1))
