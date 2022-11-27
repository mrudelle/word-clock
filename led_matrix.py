import neopixel

# 32 LED strip connected to X8.
p = machine.Pin.board.X8
n = neopixel.NeoPixel(p, 32)

# Draw a red gradient.
for i in range(32):
    n[i] = (i * 8, 0, 0)

# Update the strip.
n.write()

class LEDMatrix:
    """ Origin: Top Left """

    def __init__(self, w, h, pin_number):
        self.w = w
        self.h = h
        self.pin = machine.Pin(pin_number, machine.Pin.OUT)
        self.n = neopixel.NeoPixel(self.pin, w * h)
    
    def write(self, data):

        for y, r in enumerate(data):
            for x, l in enumerate(r):
                self.n[led_index(x, y)] = l
        
        self.n.write()
    
    def led_index(self, x, y):
        # Horizontal lines starting top left
        return y * self.w + (x if y%2 == 0 else self.h-(x+1))
