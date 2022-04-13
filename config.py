import data
import window
import effect
import getkey

def debug():
    print('This is the debug screen')
    print('At this moment this feature is still in dev')

def create(version):
    def intro(page = '0'):
        window.topBar('Config Setup ' + page + '/4')
        print('Thank you for installing Keukeiland version: ' + version)
        print('Please answer the following questions.\n')
    
    def name():
        intro('1')
        username = input('Enter a username [max 8 chars]: ')
        username = username.strip()
        username = username[:8]
        if username == '':
            print('Invalid input, please try again')
            if getkey.wait_key():
                name()
        else:
            if not data.append('keukeiland.cfg', 'username', username):
                window.topBar('ERROR')
                print('An error occurred when trying to store your config.')
                if getkey.wait_key():
                    return False
        return True
    
    def background():
        intro('2')
        print('Enter your favorite background color')
        for i in range(0,256):
            if i in range(0,256,16):
                print()
            i = str(i)
            color = effect.background(i)
            print(color + i.ljust(4), end='')
        print(effect.clear())
        backcolor = input(':')
        try:
            int(backcolor)
            if not data.append('keukeiland.cfg', 'backcolor', backcolor):
                window.topBar('ERROR')
                print('An error occurred when trying to store your config.')
                if getkey.wait_key():
                    return False
        except:
            print('Invalid input, please try again')
            if getkey.wait_key():
                background()
        return True

    if not name():
        return False
    
    if not background():
        return False
    
    print(version)
    if not data.append('keukeiland.cfg', 'version', version):
        window.topBar('ERROR')
        print('An error occurred when trying to store your config.')
        if getkey.wait_key():
            return False
            
    window.topBar('Config Setup')
    print('Your config has been saved.\n')
    print('Press any key to continue')
    if getkey.wait_key():
        return True
