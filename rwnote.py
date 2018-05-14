class RWnote():
    """Класс работы с записями"""

    def __init__(self, mode, name):
        self.mode = mode
        self.name = name
    pass

    def readNote(self):
        file = open(self.name, 'r', encoding='utf8')
        file.read()
        file.close()
        return