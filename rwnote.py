class RWnote():
    """Класс работы с записями умеет r - читать, w - записывать(перезаписывать заново), добавлять в файл"""

    def __init__(self, mode):
        self.mode = mode
        self.filename = input('Укажите название файла: \n')
    pass

    def readNote(self):
        file = open(self.filename, 'r', encoding='utf8')
        print(file.read())
        file.close()
        return

    def writeNote(self):
        text = ''
        tmp = str(input())
        while tmp != '!сохранить':
            text = text + tmp + '\n'
            tmp = str(input())
        file = open(self.filename, 'w', encoding='utf8')
        file.write(text)
        file.close()
        return

    def addNote(self):
        text = ''
        tmp = str(input())
        while tmp != '!сохранить':
            file = open(self.filename, 'a', encoding='utf8')
            file.write(tmp + '\n')
            tmp = str(input())
        return

    def canNote(self):
        # filename = input('Укажите название файла: \n')
        print(self.filename + '    ' + self.mode)
        if self.mode == '!прочитать':
            self.readNote()
        elif self.mode == '!создать':
            self.writeNote()
        elif self.mode == '!дописать':
            self.addNote()
        else:
            print('Ошибка! Неизвестная команда.')
        print('Завершение работы')
        return

