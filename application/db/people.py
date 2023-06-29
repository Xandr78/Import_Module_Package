employees = ['John Gray', 'Tom Clancy', 'Garry Potter']
def get_employees(employ):
        # employ = input('Введите имя: ')
        count = 0
        for i in employees:
            if employ in i:
                print(i)
                break
            count += 1
            if count == 3:
                print('такого имени не существует!')
