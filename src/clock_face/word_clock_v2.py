FACE = [
    ['I', 	'L', 	'R', 	'E', 	'S', 	'T', 	'D', 	'U', 	'N', 	'E', 	'U', 	'F',],
    ['T', 	'E', 	'M', 	'P', 	'H', 	'A', 	'P', 	'P', 	'Y', 	'O', 	'L', 	'I',],
    ['S', 	'E', 	'P', 	'T', 	'I', 	'H', 	'U', 	'I', 	'T', 	'N', 	'S', 	'N',],
    ['M', 	'I', 	'D', 	'I', 	'X', 	'D', 	'E', 	'U', 	'X', 	'Z', 	'I', 	'K',],
    ['O', 	'C', 	'I', 	'N', 	'Q', 	'U', 	'A', 	'T', 	'R', 	'E', 	'X', 	'L',],
    ['M', 	'I', 	'N', 	'U', 	'I', 	'T', 	'R', 	'O', 	'I', 	'S', 	'H', 	'E',],
    ['H', 	'E', 	'U', 	'R', 	'E', 	'S', 	'U', 	'M', 	'O', 	'I', 	'N', 	'S',],
    ['O', 	'B', 	'I', 	'R', 	'T', 	'H', 	'D', 	'A', 	'Y', 	'E', 	'T', 	'R',],
    ['V', 	'I', 	'N', 	'G', 	'T', 	'R', 	'O', 	'I', 	'S', 	'Q', 	'P', 	'U',],
    ['D', 	'C', 	'I', 	'N', 	'Q', 	'U', 	'A', 	'R', 	'T', 	'S', 	'Z', 	'R',],
    ['A', 	'Y', 	'A', 	'N', 	'O', 	'K', 	'M', 	'A', 	'T', 	'T', 	'O', 	'U',],
    ['D', 	'E', 	'M', 	'I', 	'D', 	'I', 	'X', 	'↗', 	'↘', 	'↙', 	'↖', 	'N',],
]

IL_EST =        [[(0,0), (1,0)], [(3,0), (5,0)]]

# HOUR:
HEURES =        [[(0,6), (5,6)]]
MINUIT =        [[(0,5), (5,5)]]
MIDI =          [[(0,3), (3,3)]]
UNE_HEURE =     [[(7,0), (9,0)], [(0,6), (4,6)]]
DEUX_HEURES =   [[(5,3), (8,3)]] + HEURES
TROIS_HEURES =  [[(5,5), (9,5)]] + HEURES
QUATRE_HEURES = [[(4,4), (9,4)]] + HEURES
CINQ_HEURES =   [[(1,4), (4,4)]] + HEURES
SIX_HEURES =    [[(10,2), (10,4)]] + HEURES
SEPT_HEURES =   [[(0,2), (3,2)]] + HEURES
HUIT_HEURES =   [[(5,2), (8,2)]] + HEURES
NEUF_HEURES =   [[(8,0), (11,0)]] + HEURES
DIX_HEURES =    [[(2,3), (4,3)]] + HEURES
ONZE_HEURES =   [[(9,1), (9,4)]] + HEURES

# MINUTES:
ET =            [[(9,7), (10,7)]]
MOINS =         [[(7,6), (11,6)]]

CINQ =              [[(1,9), (4,9)]]
DIX =               [[(4,11), (6,11)]]
ET_QUART =          ET +            [[(4,9), (8,9)]]
VINGT =             [[(0,8), (4,8)]]
VINGT_CINQ =        VINGT + CINQ
ET_DEMI =           ET +            [[(0,11), (3,11)]]
MOINS_VINGT_CINQ =  MOINS + VINGT + CINQ
MOINS_VINGT =       MOINS + VINGT
TROIS_QUARTS =      [[(4,8), (8,8)], [(4,9), (9,9)]]
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
    return [[(7, 11), (val+6, 11)]]


def get_lines_for_time(h, m):
    minute = int((m - m%5)/5)
    hour_bump = 1 if minute in [7, 8, 10, 11] else 0
        
    hour = (h + hour_bump) % 24

    hour_lines = FULL_HOURS[hour]
    sub_hour_lines = FULL_SUBHOURS[minute]
    sub_5_minutes = minute_remainder(m%5)

    return IL_EST + hour_lines + sub_hour_lines + sub_5_minutes