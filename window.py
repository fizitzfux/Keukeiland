import os

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
    
def out(content=''):
    print(u'\u001b[1B \u001b[9999D' + '|' + '\u001b[1C' + content, end='')
    
def out_new(content=''):
    print(' ' + u'\u001b[1B \u001b[9999D' + '|' + '\u001b[2C \u001b[4B' + content, end='')
    
'''def out_add(content=''):'''
    
def menu(terminal_height, terminal_width, username='Default '):
    clear()
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
    print(' Keukeiland alpha-2.0.0  -  ' + username)
    print(u'\u001b[9999A \u001b[9999D \u001b[1B \u001b[1C', end='')
