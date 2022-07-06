import os

class Window:
    def __init__(self):
        terminalSize = os.get_terminal_size()
        self.height = terminalSize.lines
        self.width = terminalSize.columns
        self.theme = ("\u001b[7m",)
        self.info = {"name":"keukeiland DEMO",}
        self._active = []

        if os.name in ('nt', 'dos'): self._clear = 'cls'
        else: self._clear = 'clear'
        self.clear()

    def clear(self):
        print('\u001b[9999A \u001b[9999D', end='')
        os.system(self._clear)

    def refresh(self):
        self.clear()
        for i in range(len(self._active)):
            foo = getattr(self, self._active[i])
            foo()

    def unload(self, toRemove=""):
        if toRemove == "":
            self._active.clear()
        else:
            self._active.remove(toRemove)

    def topbar(self, spacer=" - "):
        self._active.append("topbar")
        content = ""
        for x in self.info:
            content = content + spacer + self.info[x]
        print('\u001b[9999A\u001b[9999D' + self.theme[0] + content[len(spacer):].center(self.width) + '\u001b[0m')
    # def clear(self):
    #     print('\u001b[9999A \u001b[9999D', end='')
    #     os.system(self.clear)
    #
    # def topBar(self, page = None):
    #     terminalWidth = self.terminalWidth
    #     username = data.read('keukeiland.cfg', 'username')
    #     if username == False:
    #         username = 'Default'
    #     """color = data.read('keukeiland.cfg', 'color')
    #     if color == False:
    #         colorcode = effect.reverse()
    #     else:
    #         colorcode = '\u001b[48;5;' + color + 'm'"""
    #     version = data.read('keukeiland.cfg', 'version')
    #     if version == False:
    #         version = 'DEMO'
    #         clear()
    #         if page == None:
    #             topBar = 'Keukeiland ' + version + ' - ' + username
    #         else:
    #             topBar = 'Keukeiland ' + version + ' - ' + username + ' - ' + page
    #         print(effect.bold() + effect.background() + topBar.center(terminalWidth) + effect.clear(), end='')
    #
    # def menu(self):
    #     topBar('Main Menu')
