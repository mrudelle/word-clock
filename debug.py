import datetime

from src.utils.terminal_clock import day_loop

def main():
    #t = datetime.datetime.now()
    #display_time(t)

    # times that violate the rules

    # minuit trois quarts: shares the T
    #show('0:46')
    
    # une heure moins ... : une and moins form one word
    #show('12:37')
    #show('12:42')
    #show('12:57')

    day_loop()

if __name__ == '__main__':
    main()