#import external modules
import os
#import local modules
import data
import config
import screen
import getkey
#set global variables
version = "a2.1.0"

#function for exiting the program
def exit_program():
    win.unload()
    win.info["page"] = "Exit"
    win.infobar()
    win.refresh()
    win.alert("Quitting...",1)
    win.clear()
    exit()

if data.read("keukeiland.cfg", "version") != version:
    if not config.create(version):
        exit_program()

username = data.read("keukeiland.cfg", "username")
theme_location = data.read("keukeiland.cfg", "theme")
if str(type(theme_location)) != "<class 'dict'>":
    theme = data.read(theme_location, dict = True)
else:
    theme = theme_location

win = screen.Window()
win.theme.update(theme)
win.info = {"name":"Keukeiland " + version,"user":username,"page":"Menu"}
win.infobar(offset=-2,spacer="69 =",elementName="infobar#695")
win.infobar(content="",offset=5)
win.refresh()
getkey.wait_key()
win.unload("infobar#695")
win.refresh()
getkey.wait_key()

exit_program()
