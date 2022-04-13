import data

def reverse():
    return '\u001b[7m' 
    
def bold():
    return '\u001b[1m'
    
def clear():
    return '\u001b[0m'
    
def resetLine():
    return '\u001b[9999D'
    
def foreground(color = 'config', shift = 0):
    if color == 'config':
        color = data.read('keukeiland.cfg', 'forecolor')
        if color == False:
            return ''
    code = '\u001b[38;5;' + str(int(color) + shift) + 'm'
    return code

def background(color = 'config', shift = 0):
    if color == 'config':
        color = data.read('keukeiland.cfg', 'backcolor')
        if color == False:
            return ''
    code = '\u001b[48;5;' + str(int(color) + shift) + 'm'
    return code
