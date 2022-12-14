def rgb_scale_offset(scale, offset):
    (s_r, s_g, s_b) = scale
    (o_r, o_g, o_b) = offset

    def scale_rgb_pixel(pixel):
        (r, g, b) = pixel
        return (
            r * s_r + o_r, 
            g * s_g + o_g, 
            b * s_b + o_b,
        )
    return scale_rgb_pixel

def scale_rgb_filter(scale):
    return rgb_scale_offset((scale, scale, scale), (0,0,0))

class ScreenBuffer:

    def __init__(self, w, h, default=None):

        if default == None:
            default = (0, 0, 0)
        
        self.w = w
        self.h = h
        self.buffer = []
        self.default = default

        self.clear()
    
    def clear(self):
        self.buffer = [[self.default for _ in range(self.w)] for _ in range(self.h)]
    
    def draw_pixel(self, x, y, value):
        self.buffer[y][x] = value
    
    def draw_line(self, line, value):
        [(x, y), (x_max, y_max)] = line
        self.draw_pixel(x, y, value)
        while x != x_max or y != y_max:
            x = min(x+1, x_max)
            y = min(y+1, y_max)
            self.draw_pixel(x, y, value)

    def draw_lines(self, lines, value):
        for line in lines:
            self.draw_line(line, value)
    
    def filter(self, filter):
        for x in range(self.w):
            for y in range(self.h):
                self.buffer[y][x] = filter(self.buffer[y][x])