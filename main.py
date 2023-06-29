# from application.salary import calculate_salary
# from application.db.people import get_employees
import application.salary
import application.db.people
import datetime
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# class Bookkeeper:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password
#
#     def calculate_salary(self):
#        sum1 = 3+2
#        print(sum1)
#
#     def get_employees(self):
#         employ = input('Введите имя: ')
#         count = 0
#         for i in employees:
#             if employ in i:
#                 print(i)
#                 break
#             count += 1
#             if count == 3:
#                 print('такого имени не существует!')
# def main():
#     bookkeeper_1 = Bookkeeper('Nadejda', '12345')
#     bookkeeper_1.calculate_salary()
#     bookkeeper_1.get_employees()

# def main():
#     calculate_salary()
#     employ = input('Введите имя: ')
#     get_employees(employ)

def main():
    application.salary.calculate_salary()
    employ = input('Введите имя: ')
    application.db.people.get_employees(employ)

if __name__ == '__main__':
    # print_hi('PyCharm')
    # print(datetime.datetime.now())
    print(datetime.date.today())
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Не получается установить библиотеку в конкретный проект!
#у меня не срабатывает в терминале : source venv/bin/activate
#ссылка на скрин: disk.yandex.ru...Gd3f9RuWYg
