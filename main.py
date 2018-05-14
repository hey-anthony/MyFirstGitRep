# тестовое приложение
print('Эта простая записная книжка. \nВыберете !создать !редактировать !прочитать \n')

answer = input()
if answer == '!создать':
    mode = 'w'
    filename = input('Укажите название файла: \n')
    # filename = 'file.txt'
    print('Введите текст который нужно сохранить в файле. Чтобы закончить ввод введите !сохранить.\n Введите текст: \n')
    text = ''
    tmp = str(input())
    while tmp != '!сохранить':
        text = text + tmp + '\n'
        tmp = str(input())

    f1 = open(filename, 'w', encoding='utf8')
    f1.write(text)
    f1.close()

elif answer == '!прочитать':
    mode = 'r'
    filename = input('Укажите название файла: \n')
    f1 = open(filename, 'r', encoding='utf8')
    print(f1.read())
    f1.close()
elif answer == '!редактировать':
    mode = 'a'
    filename = input('Укажите название файла: \n')
    # filename = 'file.txt'
    print('Введите текст который нужно сохранить в файле. Чтобы закончить ввод введите !сохранить.\n Введите текст: \n')
    tmp = str(input())
    while tmp != '!сохранить':
        f1 = open(filename, 'a', encoding='utf8')
        f1.write(tmp + '\n')
        f1.close()
        tmp = str(input())
else:
    print('Ошибка! Неизвестная команда.')

print('Завершение работы')