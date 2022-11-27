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