def Data_output_all():
    with open('file.txt', 'r', encoding = 'utf-8') as file:
        for line in file:
            print(line)
    file.close()

def Search(surname):
    with open('file.txt', 'r', encoding = 'utf-8') as file:
        for line in file:
            if surname in line:
                print(line)
    file.close()
