import window
from time import sleep

def initiate():
    print('This is the debug screen')
    print('At this moment this feature is still in dev')

def config_create(terminal_height, terminal_width):
    window.menu(terminal_height, terminal_width)
    window.out('Thank you for using Keukeiland')
    window.out('I will ask you a few questions to')
    window.out('continue the setup\n\n')
    config = open('keukeiland.cfg', 'at')
    name = input(u'\u001b[1C' + 'Please enter a username [max 8 chars]: ')
    if name == '':name = 'Default '
    config.write('name=' + name.ljust(8) + ';')
    config.close()
    window.menu(terminal_height, terminal_width)
    #window.out()
    window.out_new('This were all the questions,')
    #window.out('the program will now crash to complete the setup')
    #window.out('Please restart the program after closing.')
    sleep(3)
    
