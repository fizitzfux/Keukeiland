#version 1.0.1
#https://github.com/jippie13/Keukeiland

try: import os # needed for reliable rendering of terminal, external
except: _os_module_imported = False
else: _os_module_imported = True

try: from time import sleep # only needed when using alert with timeout, external
except: _time_module_imported = False
else: _time_module_imported = True

try: from getkey import wait_key # only needed when using interactive elements, local
except: _getkey_module_imported = False
else: _getkey_module_imported = True

class Window:
    def __init__(self):
        if _os_module_imported:
            terminalSize = os.get_terminal_size()
            self.height = terminalSize.lines
            self.width = terminalSize.columns
            if os.name in('nt', 'dos'):
                os.system('color')
                self._clear = 'cls'
            else:
                self._clear = 'clear'
        else:
            self.height = 24
            self.width = 80

        self.theme = {
        "theme_0":      "\u001b[7m",
        "theme_1":      "",
        "background_0": "",
        "selected":     "\u001b[7m",
        "clear":        "\u001b[0m"
        }
        self.info = {"name":"keukeiland DEMO",}
        self._active = {}

        self.clear()


    def clear(self):
        if _os_module_imported:
            os.system(self._clear)
        else:
            print("\033[2J")
        self._align()


    def _align(self, x=0, y=0, align="top-left"):
        if align == "top-left":

            if x == 0 and y == 0:
                print("\u001b[9999A\u001b[9999D",end="")

            elif x != 0 and y == 0:
                if x > 0:
                    print("\u001b[9999A\u001b[9999D",end="")
                    print("\u001b[" + str(x) + "C",end="")
                elif x < 0:
                    print("\u001b[9999A\u001b[9999D",end="")
                    print("\u001b[" + str(self.width + x) + "C",end="")

            elif x == 0 and y != 0:
                if y > 0:
                    print("\u001b[9999A\u001b[9999D",end="")
                    print("\u001b[" + str(y) + "B",end="")
                elif y < 0:
                    print("\u001b[9999A\u001b[9999D",end="")
                    print("\u001b[" + str(self.height + y) + "B",end="")

            elif x > 0 and y != 0:
                if y > 0:
                    print("\u001b[9999A\u001b[9999D",end="")
                    print("\u001b[" + str(x) + "C\u001b[" + str(y) + "B",end="")
                elif y < 0:
                    print("\u001b[9999A\u001b[9999D",end="")
                    print("\u001b[" + str(x) + "C\u001b[" + str(self.height + y) + "B",end="")

            elif x < 0 and y != 0:
                if y > 0:
                    print("\u001b[9999A\u001b[9999D",end="")
                    print("\u001b[" + str(self.width + x) + "C\u001b[" + str(y) + "B")
                elif y < 0:
                    print("\u001b[9999A\u001b[9999D",end="")
                    print("\u001b[" + str(self.width + x) + "C\u001b[" + str(self.height + y) + "B")

        elif align == "center":
            print("\u001b[9999A\u001b[9999D",end="")
            print("\u001b[" + str(int(self.width / 2 + x)) + "C\u001b[" + str(int(self.height / 2 + y)) + "B",end="")


    def refresh(self):
        self.clear()

        for i in range(self.height):
            print(self.theme["background_0"] + " "*self.width + "\u001b[0m",end="")
        self._align()

        for x in self._active:
            func = getattr(self, x.strip("#1234567890"))
            args = "self._active[x][{}],"*len(self._active[x])
            args = args.format(*[str(i) for i in range(0,len(self._active[x]))])
            func(*eval(args))

        print("")


    def unload(self, toRemove=""):
        if toRemove == "":
            self._active.clear()
        else:
            self._active.pop(toRemove)


    def infobar(self, content="", spacer=" - ", offset=0, elementName="infobar"):
        self._active[elementName] = (content,spacer,offset,elementName)
        self._align(0,offset)
        if content == "":
            for x in self.info:
                content = content + spacer + self.info[x]
            print(self.theme["theme_0"] + content[len(spacer):].center(self.width) + self.theme["clear"],end="")
        else:
            print(self.theme["theme_0"] + content.center(self.width) + self.theme["clear"],end="")


    def alert(self, message, option_1="OK", option_2="", option_3="", selected=1):
        self._align(int(-len(message)/2-2),-3,"center")
        print(self.theme["theme_1"] + "="*(len(message)+4))
        self._align(int(-len(message)/2-2),-2,"center")
        print("| " + " "*len(message) + " |")
        self._align(int(-len(message)/2-2),-1,"center")
        print("| " + message + " |")
        self._align(int(-len(message)/2-2),0,"center")
        print("| " + " "*len(message) + " |")
        self._align(int(-len(message)/2-2),1,"center")

        if str(type(option_1)) == "<class 'str'>":
            if selected == 1:
                options = self.theme["selected"] + option_1 +self.theme["clear"]+self.theme["theme_1"]+ " " + option_2 + " " + option_3
            elif selected == 2:
                options = option_1 + " " + self.theme["selected"] + option_2 +self.theme["clear"]+self.theme["theme_1"]+ " " + option_3
            elif selected == 3:
                options = option_1 + " " + option_2  + " " + self.theme["selected"] + option_3 +self.theme["clear"]+self.theme["theme_1"]
            print("| " + options.center(len(message)+17) + " |")
        else:
            print("| " + " "*len(message) + " |")

        self._align(int(-len(message)/2-2),2,"center")
        print("| " + " "*len(message) + " |")
        self._align(int(-len(message)/2-2),3,"center")
        print("="*(len(message)+4) + self.theme["clear"])

        if str(type(option_1)) != "<class 'str'>":
            sleep(option_1)
            return

        pressed = wait_key()
        #if user pressed right arrow
        if pressed == "\xe0\x4d":
            selected += 1
            if option_2 == "" and selected >= 2:
                selected = 1
            elif option_3 == "" and selected >= 3:
                selected = 1
            elif selected >= 4:
                selected = 1
            return self.alert(message, option_1, option_2, option_3, selected)
        #if user pressed left arrow
        elif pressed == "\xe0\x4b":
            selected -= 1
            if option_2 == "" and selected <= 0:
                selected = 1
            elif option_3 == "" and selected <= 0:
                selected = 2
            elif selected <= 0:
                selected = 3
            return self.alert(message, option_1, option_2, option_3, selected)
        #if user pressed enter/return or space
        elif pressed == "\x0d" or pressed == "\x20":
            return selected
        else:
            return self.alert(message, option_1, option_2, option_3, selected)
