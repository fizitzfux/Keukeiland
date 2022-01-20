#import external modules
import os
import sys
import time
#import local modules
import setup
import getkey

#check if the os is windows, if so enable VT100
if os.name =='nt':os.system('color')

#get the width and height of the terminal
terminal_something = os.get_terminal_size()
terminal_string = str(terminal_something).strip('os.terminal_z(cu=)')
terminal_width_end = terminal_string.find(',')
terminal_width = terminal_string[:terminal_width_end]
terminal_height = terminal_string[terminal_width_end:].strip(', lines=')
print(terminal_width + 'x' + terminal_height)

#display an rainbow loading thingy
while True:
    print ("Loading all 256 colors...")
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j + 1)
            color = u"\u001b[38;5;" + code + "m" + code.ljust(4)
            time.sleep(0.0025)
            sys.stdout.write(u"\u001b[1000D" + color + "/256")#str(int(u / 10000)) + "%")
            sys.stdout.flush()
    print()

#check if ESC is pressed, if so open first-time setup / debug screen
    if getkey.key_pressed("\x1b"):
        setup.initiate()
        break
    break

def main_menu():
    for height in range(0, int(terminal_height)):
        print('|' + u'\u001b[' + terminal_width + 'C' + '|')
main_menu()

#function for exiting the script
def exit_program():
    print('Press any key to quit.')
    while True:
        if getkey.key_pressed():
            print('Done.')
            exit()
exit_program()
print('EOF')
print('Quitting...')
