def Data_change(index):
    with open('file.txt', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        file.close
        
        spisok = lines[index-1].split('\t')

        action = int(input('Выберите номер желаемой процедуры:'
                                '\n 1. Изменить фамилию'
                                '\n 2. Изменить имя'
                                '\n 3. Изменить Отчество'
                                '\n 4. Изменить номер телефона'
                                '\n для завершения программы введите любую другую цифру'
                                '\n Введите номер операции:'))

        if action == 1:
            spisok[0] = input('Введите новую фамилию:')
        else:
            if action == 2:
                spisok[1] = input('Введите новое имя:')
            else:
                if action == 3:
                    spisok[2] = input('Введите новое отчество:')
                else:
                    if action == 4:
                        spisok[3] = input('Введите новый номер телефона:')
                    else:
                        return
        
        lines[index-1] = '\t'.join(spisok)
        print(lines[index-1])

        with open('file.txt', "w", encoding = 'utf-8') as file:
            file.writelines(lines)
            file.close() 
  