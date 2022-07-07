#import external modules
import os
#import local modules
import data
import config
import screen
import getkey
#set global variables
version = 'a2.1.0'

#function for exiting the program
def exit_program():
    win.unload()
    win.refresh()
    win.info["page"] = "Exit"
    win.infobar()
    win.refresh()
    win.alert("Quitting...",1)
    win.clear()
    print('Done.')
    exit()

if data.read('keukeiland.cfg', 'version') != version:
    if not config.create(version):
        exit_program()

username = data.read("keukeiland.cfg", "username")

win = screen.Window()
win.theme.update({"theme_0":"\u001b[48;5;169m","theme_1":"\u001b[48;5;1m","background_0":"\u001b[48;5;6m"})
win.info = {"name":"Keukeiland " + version,"user":username,"page":"Menu"}
win.infobar()
win.refresh()
# win.unload("topbar")
# win.refresh()
getkey.wait_key()

exit_program()
