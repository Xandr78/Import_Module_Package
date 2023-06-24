# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


employees = ['John Gray', 'Tom Clancy', 'Garry Potter']

class Bookkeeper:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def calculate_salary(self):
       sum1 = 3+2
       print(sum1)

    def get_employees(self):
        employ = input('Введите имя: ')
        count = 0
        for i in employees:
            if employ in i:
                print(i)
                break
            count += 1
            if count == 3:
                print('такого имени не существует!')


def main():
    bookkeeper_1 = Bookkeeper('Nadejda', '12345')
    bookkeeper_1.calculate_salary()
    bookkeeper_1.get_employees()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
