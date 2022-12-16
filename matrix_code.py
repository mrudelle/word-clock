import random
from collections import namedtuple
from time import ticks_ms, ticks_add, ticks_diff, sleep_ms
from led_matrix import LEDMatrix
from screen_buffer import ScreenBuffer, rgb_scale_offset

Letter = namedtuple('Letter', 'x y pace')

def generate_new_letters():
    pass

def draw_letters(letters, buff: ScreenBuffer):
    for letter in letters:
        buff.draw_pixel(int(letter.x), int(letter.y), (255, 150, 150))

def shift_letter(letter: Letter, frequency_ms):
    return Letter(letter.x, letter.y + frequency_ms / letter.pace, letter.pace)

def new_letters(w, h):
    if random.randint(0, 1000) < 300:
        return [Letter(random.randint(0, w-1), random.randint(0, h-1), random.randint(5, 50))]
    else: 
        return []

def matrix_code(w=10, h=10, leds_pin=12, frequency_ms=5):

    lmatrix = LEDMatrix(w, h, leds_pin)
    lmatrix.brightness = .3
    buff = ScreenBuffer(w, h)

    lmatrix.write(buff.buffer)

    next_frame = ticks_ms()
    
    letters = [
        Letter(0, 0, 30),
    ]

    while(True):

        # maybe add letter
        letters.extend(new_letters(w, h))

        # fade screen
        buff.filter(rgb_scale_offset((0, 0.9, 0), (0,0,0)))
        
        # draw letters
        draw_letters(letters, buff)

        # shift letters
        for i, _ in enumerate(letters):
            letters[i] = shift_letter(letters[i], frequency_ms=frequency_ms)
        
        # prune letters
        letters = list(filter(lambda letter: letter.y < h, letters))

        # render screen
        lmatrix.write(buff.buffer)

        # sleep until next frame
        next_frame = ticks_add(next_frame, frequency_ms) 
        sleep_ms(ticks_diff(next_frame, ticks_ms()))


matrix_code()