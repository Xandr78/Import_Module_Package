import re

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

text =  "Что такое регулярные  выражения?\ Говоря просто, регулярное выражение - это последовательность символов, для поиска и замены."
pattern = '\w+'
result = re.findall(pattern, text)
print(result)

pattern2 = '[?.]'
result = re.split(pattern2, text)
print(result)
print(f'количество {len(result)}')

pattern3 = 'регулярн[а-яё]+\s+выражен[а-яё]+'
result = re.findall(pattern3, text)
print(result)

#удалить все дубликаты
first_list = [1, 2, 2, 5]
second_list = [2, 5, 7, 9]
result = list(set(first_list + second_list))
print(result)

# удалить элементы из второго списка, которые есть в первом
first_list = [1, 2, 2, 5]
second_list = [2, 2, 5, 7, 9]
result = first_list + list(set(second_list) - set(first_list))
print(result)

