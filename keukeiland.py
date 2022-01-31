#import external modules
import os
from sys import stdout
from time import sleep
#import local modules
import setup
import window
import getkey

def left_corner():
    print(u'\u001b[9999A \u001b[9999D \u001b[1B \u001b[1C', end='')

#function for exiting the script
def exit_program():
    print('Press any key to quit.')
    while True:
        if getkey.key_pressed():
            print(u'\u001b[' + str(int(terminal_height)-2) + 'B')
            print('Done.')
            exit()

def clear_screen():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#check if the os is windows, if so enable VT100
if os.name in('nt', 'dos'):os.system('color')

#get the width and height of the terminal in characters
terminal_something = os.get_terminal_size()
terminal_string = str(terminal_something).strip('os.terminal_z(cu=)')
terminal_width_end = terminal_string.find(',')
terminal_width = terminal_string[:terminal_width_end]
terminal_height = terminal_string[terminal_width_end:].strip(', lines=')
print(terminal_width + 'x' + terminal_height)
sizeerror = 0
if int(terminal_width) <  45:
    print('Your terminal-window is too thin, the minimum is 45x21')
    sizeerror = 1
if int(terminal_height) < 21:
    print('Your terminal-window is too short, the minimum is 45x21')
    sizeerror = 1
if sizeerror != 0:exit_program()

#display an rainbow loading thingy
while True:
    print ("Loading all 256 colors...")
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j + 1)
            color = u"\u001b[38;5;" + code + "m" + code.ljust(4)
            sleep(0.0025)
            stdout.write(u"\u001b[1000D" + color + "/256")
            stdout.flush()
    print()

#check if ESC is pressed, if so open first-time setup / debug screen
    if getkey.key_pressed("\x1b"):
        setup.initiate()
        break
    break

def load_config():
    try:
        config_test = open('keukeiland.cfg', 'rt')
        config_test.close
    except:
        setup.config_create(terminal_height, terminal_width)
    else:
        config = open('keukeiland.cfg', 'rt')
        username = str(config.read()[5:13])
        return username
        config.close()
username = str(load_config())

window.menu(terminal_height, terminal_width, username)

exit_program()
print('EOF')
print('Quitting...')
