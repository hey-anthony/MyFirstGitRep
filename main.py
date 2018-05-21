# тестовое приложение записной книжки
from rwnote import *
print('Эта простая записная книжка. \nВыберете !создать !редактировать !прочитать \n')

answer = str(input())
note = RWnote(answer)
note.canNote()

