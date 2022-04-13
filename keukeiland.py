#import external modules
import os
#import local modules
import data
import config
import window
import getkey
#set global variables
version = 'a2.1.0'

def left_corner():
    print(u'\u001b[9999A \u001b[9999D \u001b[1B \u001b[1C', end='')

#function for exiting the script
def exit_program():
    window.topBar()
    print('Press any key to quit.')
    while True:
        if getkey.key_pressed():
            window.clear()
            print('Done.')
            exit()

#check if the os is windows, if so enable VT100
if os.name in('nt', 'dos'):os.system('color')

#to be replaced with a welcome-screen
"""
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

#check if ESC is pressed, if so open setup-screen
    if getkey.key_pressed("\x1b"):
        config.debug()
        break
    break"""

if data.read('keukeiland.cfg', 'version') != version:
    if not config.create(version):
        exit_program()

window.menu()

exit_program()
