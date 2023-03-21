def Data_input(data1, data2, data3, data4):
    with open('file.txt', 'a', encoding = 'utf-8') as file:
        file.write(f'{data1}\t')
        file.write(f'{data2}\t')
        file.write(f'{data3}\t')
        file.write(f'{data4}\t \n')
    file.close()