import os
import data
import effect

def clear():
    print('\u001b[9999A \u001b[9999D', end='')
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    try:
        os.system(command)
    except:
        print('\033c', end='')

def getHeight():
    try:
        terminalSize = os.get_terminal_size()
        terminalHeight = terminalSize.lines
        return terminalHeight
    except:
        return 30

def getWidth():
    try:
        terminalSize = os.get_terminal_size()
        terminalWidth = terminalSize.columns
        return terminalWidth
    except:
        return 100

def topBar(page = None):
    terminalWidth = getWidth()
    username = data.read('keukeiland.cfg', 'username')
    if username == False:
        username = 'Default'
    """color = data.read('keukeiland.cfg', 'color')
    if color == False:
        colorcode = effect.reverse()
    else:
        colorcode = '\u001b[48;5;' + color + 'm'"""
    version = data.read('keukeiland.cfg', 'version')
    if version == False:
        version = 'DEMO'
    clear()
    if page == None:
        topBar = 'Keukeiland ' + version + ' - ' + username
    else:
        topBar = 'Keukeiland ' + version + ' - ' + username + ' - ' + page
    print(effect.bold() + effect.background() + topBar.center(terminalWidth) + effect.clear(), end='')

def menu():
    topBar('Main Menu')
    
