from screen_buffer import ScreenBuffer
import datetime
from word_clock import get_lines_for_time, FACE

class bcolors:
    ENDC = '\033[0m'
    GREY = '\033[38;5;235m'
    WHITE = '\033[38;5;255m'

    @classmethod
    def grey(cls, text):
        return f'{cls.GREY}{text}{cls.ENDC} '

    @classmethod
    def white(cls, text):
        return f'{cls.WHITE}{text}{cls.ENDC} '



def print_face(face, mask):
    for row_i, row in enumerate(face):
        for l_i, l in enumerate(row):
            print(bcolors.white(l) if mask[row_i][l_i] else bcolors.grey(l), end='')
        print('')


def display_time(t):
    print(f'{t.hour}:{t.minute}')

    buffer = ScreenBuffer(len(FACE), len(FACE[0]), False)
    buffer.draw_lines(get_lines_for_time(t.hour, t.minute), True)

    print_face(FACE, buffer.buffer)


def show(time_str):
    t = datetime.datetime.strptime(time_str, '%H:%M')
    display_time(t)


def day_loop():
    """ Display all possible time values """
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