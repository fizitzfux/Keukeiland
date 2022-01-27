import os

terminal_height = str(21)
terminal_width = str(45)

def clear_screen():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def initiate():
    print('This is the first-time setup / debug screen')
    print('At this moment this feature is still in dev')

def config_create():
    clear_screen()
    for height in range(0, int(terminal_height)-1):
        if height in range(1, int(terminal_height)-3):
            print('|' + u'\u001b[' + terminal_width + 'C' + '|')
        if height == 0:
            for width in range(0, int(terminal_width)-1):
                print('-', end='')
            print(' ', end='')
        if height == int(terminal_height)-2:
            print('|', end='')
            for width in range(0,  int(terminal_width)-2):
                print('_', end='')
            print('|', end='')
    print(u'\u001b[9999A \u001b[9999D \u001b[1B \u001b[3C', end='')
    print('\nThank you for using Keukeiland\nI will ask you a few questions to\ncontinue the setup\n\n')
    config = open('keukeiland.cfg', 'at')
    name = input('Please enter a username [max 8 chars]: ')
    config.write('name=' + name.ljust(8) + ';')
    config.close()
    print(u'\u001b[9999A \u001b[9999D \u001b[1B \u001b[1C\nThis were all the questions,\nthe program will now crash to complete the setup\nPlease restart the program after closing.')
