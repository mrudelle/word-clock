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

IL_EST =        [[(0,0), (4,0)]]

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
    SIX_HEURES, SEPT_HEURES, HUIT_HEURES, NEUF_HEURES, DIX_HEURES, ONZE_HEURES,
    MIDI, UNE_HEURE, DEUX_HEURES, TROIS_HEURES, QUATRE_HEURES, CINQ_HEURES, 
    SIX_HEURES, SEPT_HEURES, HUIT_HEURES, NEUF_HEURES, DIX_HEURES, ONZE_HEURES,
]
FULL_SUBHOURS = [
    [], CINQ, DIX, ET_QUART, VINGT, VINGT_CINQ, ET_DEMI,
    MOINS_VINGT_CINQ, MOINS_VINGT, TROIS_QUARTS, MOINS_DIX, MOINS_CINQ
]

def minute_remainder(val):
    if val == 0:
        return []
    return [[(4, 9), (val+3, 9)]]


def get_lines_for_time(h, m):
    minute = int((m - m%5)/5)
    hour_bump = 1 if minute in [7, 8, 10, 11] else 0
        
    hour = (h + hour_bump) % 24

    hour_lines = FULL_HOURS[hour]
    sub_hour_lines = FULL_SUBHOURS[minute]
    sub_5_minutes = minute_remainder(m%5)

    return IL_EST + hour_lines + sub_hour_lines + sub_5_minutes