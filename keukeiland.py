#import modules
import os
import sys
import time
import setup #local
import getkey #local

#check if the os is windows, if so enable VT100
if os.name =='nt':os.system('color')
#display an percentage loading thingy
while True:
    print ("Loading...")
    for i in range(0, 100):
        time.sleep(0.01)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print()
#check if ESC is pressed, if so open debug screen
    if getkey.key_pressed("\x1b"):
        setup.initiate()
        break
    break
print("Done.")
