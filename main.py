import datetime
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[38;5;235m'
    WHITE = '\033[38;5;255m'

    @classmethod
    def grey(cls, text):
        return f'{cls.GREY}{text}{cls.ENDC} '

    @classmethod
    def white(cls, text):
        return f'{cls.WHITE}{text}{cls.ENDC} '

FACE = [
    ['I',	'L',	'E',	'S',	'T',	'_',    'O',	'N',	'Z',	'E',],
    ['M',	'C',	'T',	'R',	'O',	'I',	'S',	'E',	'P',	'T',],
    ['I',	'I',	'D',	'E',	'U',	'X',	'I',	'U',	'H',	'U',],
    ['N',	'N',	'M',	'I',	'D',	'I',	'X',	'F',	'U',	'N',],
    ['U',	'Q',	'U',	'A',	'T',	'R',	'E',	'_',	'I',	'E',],
    ['I',	'H',	'E',	'U',	'R',	'E',	'S',	'_',	'T',	'M',],
    ['T',	'R',	'O',	'I',	'S',	'E',	'T',	'_',	'_',	'O',],
    ['_',	'V',	'I',	'N',	'G',	'T',	'D',	'E',	'M',	'I',],
    ['C',	'I',	'N',	'Q',	'U',	'A',	'R',	'T',	'S',	'N',],
    ['D',	'I',	'X',	'_',	'*',	'*',	'*',	'*',	'_',	'S',],
]

C_EST =         [[(0,0), (4,0)]]

# HOUR:
HEURES =        [[(1,5), (6,5)]]
MINUIT =        [[(0,1), (0,6)]]
MIDI =          [[(2,3), (5,3)]]
UNE_HEURE =     [[(9,2), (9,4)], [(1,5), (5,5)]]
DEUX_HEURES =   [[(2,2), (5,2)]] + HEURES
TROIS_HEURES =  [[(2,1), (6,1)]] + HEURES
QUATRE_HEURES = [[(1,4), (6,4)]] + HEURES
CINQ_HEURES =   [[(1,1), (1,4)]] + HEURES
SIX_HEURES =    [[(6,1), (6,3)]] + HEURES
SEPT_HEURES =   [[(6,1), (9,1)]] + HEURES
HUIT_HEURES =   [[(8,2), (8,5)]] + HEURES
NEUF_HEURES =   [[(7,0), (7,3)]] + HEURES
DIX_HEURES =    [[(4,3), (6,3)]] + HEURES
ONZE_HEURES =   [[(6,0), (9,0)]] + HEURES

# MINUTES:
ET =            [[(5,6), (6,6)]]
MOINS =         [[(9,5), (9,9)]]

CINQ =              [[(0,8), (3,8)]]
DIX =               [[(0,9), (2,9)]]
ET_QUART =          ET +            [[(3,8), (7,8)]]
VINGT =             [[(1,7), (5,7)]]
VINGT_CINQ =        VINGT + CINQ
ET_DEMI =           ET +            [[(6,7), (9,7)]]
MOINS_VINGT_CINQ =  MOINS + VINGT + CINQ
MOINS_VINGT =       MOINS + VINGT
TROIS_QUARTS =      [[(0,6), (4,6)], [(3,8), (8,8)]]
MOINS_DIX =         MOINS + DIX
MOINS_CINQ =        MOINS + CINQ



FULL_HOURS = [
    MINUIT, UNE_HEURE, DEUX_HEURES, TROIS_HEURES, QUATRE_HEURES, CINQ_HEURES, 
    SIX_HEURES, SEPT_HEURES, HUIT_HEURES, DIX_HEURES, ONZE_HEURES,
    MIDI, UNE_HEURE, DEUX_HEURES, TROIS_HEURES, QUATRE_HEURES, CINQ_HEURES, 
    SIX_HEURES, SEPT_HEURES, HUIT_HEURES, DIX_HEURES, ONZE_HEURES,
]
FULL_SUBHOURS = [
    [], CINQ, DIX, ET_QUART, VINGT, VINGT_CINQ, ET_DEMI,
    MOINS_VINGT_CINQ, MOINS_VINGT, TROIS_QUARTS, MOINS_DIX, MOINS_CINQ
]

def minute_remainder(val):
    if val == 0:
        return []
    return [[(4, 9), (val+3, 9)]]

def init_led_mask(face):
    h = len(face)
    w = len(face[0])

    return [
        [False for _ in range(h)] for _ in range(w)
    ]


def sub_hour():
    return [
        'cinq',
        'dix',
        'et quart',
        'vingt',
        'vingt cinq',
        'et demi',
        'moins vingt cinq',
        'moins vingt',
        'trois quarts',
        'moins dix',
        'moins cinq'
    ]

def hour():
    [
        'minuit',
        'une heure',
        'deux heures',
        'trois heures',
        'quatre heures',
        'cinq heures',
        'six heures',
        'sept heures',
        'huit heures',
        'neuf heures',
        'dix heures',
        'onze heures',
        'midi',
    ]

def print_face(face, mask):
    for row_i, row in enumerate(face):
        for l_i, l in enumerate(row):
            print(bcolors.white(l) if mask[row_i][l_i] else bcolors.grey(l), end='')
        print('')

def activate_mask(mask, x, y):
    mask[y][x] = True

def mask_draw_line(mask, line):
    [(x, y), (x_max, y_max)] = line
    activate_mask(mask, x, y)
    while x != x_max or y != y_max:
        x = min(x+1, x_max)
        y = min(y+1, y_max)
        activate_mask(mask, x, y)

def mask_draw_lines(mask, lines):
    for line in lines:
        mask_draw_line(mask, line)

def fill_gaps(face):

    for r_i, r in enumerate(face):
        for l_i, l in enumerate(r):
            if l == '_':
                pass

def display_time(t):
    minute = int((t.minute - t.minute%5)/5)
    hour_bump = 1 if minute in [7, 8, 10, 11] else 0
        
    hour = (t.hour + hour_bump) % 24
    hour = hour if hour <= 12 else (hour-12)

    hour_lines = FULL_HOURS[hour]
    sub_hour_lines = FULL_SUBHOURS[minute]

    print(f'{t.hour}:{t.minute}')

    face = FACE
    mask = init_led_mask(face)
    mask_draw_lines(mask, C_EST + hour_lines + sub_hour_lines + minute_remainder(t.minute%5))

    print_face(face, mask)

def show(time_str):
    t = datetime.datetime.strptime(time_str, '%H:%M')
    display_time(t)

def day_loop():
    t = datetime.datetime.strptime('0:0', '%H:%M')
    
    display_time(t)

    while t.day < 2:
        time.sleep(.2)
        t = t + datetime.timedelta(minutes=1)
        print("\033[F"*11, end='')
        display_time(t)

def main():
    t = datetime.datetime.now()
    display_time(t)

    # times that violate the rules

    # minuit trois quarts: shares the T
    #show('0:46')
    
    # une heure moins ... : une and moins form one word
    #show('12:37')
    #show('12:42')
    #show('12:57')

    # day_loop()

if __name__ == '__main__':
    main()