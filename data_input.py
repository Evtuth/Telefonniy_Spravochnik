surname = input('Введите Фамилию: ')
name = input('Введите Имя: ')
patronymic = input('Введите Отчество: ')
number = input('Введите номер телефона: ')

def Data_input(data1, data2, data3, data4):
    with open('file.txt', 'a', encoding = 'utf-8') as file:
        file.write(f'{surname}\t')
        file.write(f'{name}\t')
        file.write(f'{patronymic}\t')
        file.write(f'{number}\t \n')
    file.close()