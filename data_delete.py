def Data_delete(index):
    with open('file.txt', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        file.close
        lines.pop(index-1)
        with open('file.txt', "w", encoding = 'utf-8') as file:
            file.writelines(lines)
            file.close()
            print('Удаление прошло успешко!!!') 
