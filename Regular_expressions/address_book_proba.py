from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
text = """lastname,firstname,surname,organization,position,phone,email
Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,+7 (495) 913-04-78,opendata@nalog.ru
Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037,
Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168,
Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,,
Лукина Ольга Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru
Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru
Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792),
Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru"""

text2 = "Мартиняхин, Виталий Геннадьевич,,,ФНС,,+74959130037 (доб. 0792)"

## Необходимо:
# Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
# Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
# Объединить все дублирующиеся записи о человеке в одну.

##text
#lastname,firstname,surname,organization,position,phone,email
# Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,+7 (495) 913-04-78,opendata@nalog.ru
# Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037,
# Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168,
# Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,,
# Лукина Ольга Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru
# Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru
# Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792),
# Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru

with open("phonebook_raw.csv", encoding = 'utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
## Ваш код
#поиск и преобразование телефонов
def phone(a):
  pattern_phone = r'(\+7|8)\s*\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{2})[- ]?(\d{2})\s*(\(?([а-яё]{3}\.)[ ](\d{4})\)?)?'
  new_pattern_phone = r'+7(\2)\3-\4-\5 \7\8'
  result = re.sub(pattern_phone, new_pattern_phone, a)
  return result
# print(phone(text))

# поиск ФИО
def FIO(f):
  pattern_FIO = r'(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё]\w+[А-яЁё –]*\–*\s*)*\,*(\+*\d\s*\(*\d+\)*\-*\s*\d+\-*\d+\-*\d+\s*\(*\w*\.*\s*\d*\)*)*\,*(\w+\.*\w*\@\w+\.\w+)*'
  result_FIO = re.search(pattern_FIO, f)
# result_FIO_sub = re.sub(pattern_FIO, pattern_FIO_sub, text)
  return result_FIO
# print(result_FIO_sub)
# print(FIO(text))

# поиск организации и должности
# pattern_ORG = r'[ ,]'

##### основной блок
new_list_book = list()
# for i in contacts_list:
#   new_list1 = list()
#   result_name = ' '.join(i[:3])
#   result_name_re = FIO(result_name)
#   # new_list1 = [result_name_re, i[3], i[4], phone(i[5]), i[6]]
#   new_list1 += result_name_re
#   new_list1.append(i[3])
#   new_list1.append(i[4])
#   new_list1.append(phone(i[5]))
#   new_list1.append(i[6])
#   # print(new_list1)
#   new_list_book.append(new_list1)
# print(new_list_book)

for i in range(len(contacts_list)):
    if i == 0:
        new_list_book.append(contacts_list[i])
    else:
        line = ','.join(contacts_list[i])
        # result = re.search(pattern_words, line)
        result = FIO(line)
        new_list_book.append(list(result.groups()))
        if new_list_book[i][5] != None:
            new_list_book[i][5] = phone(new_list_book[i][5])
print(new_list_book)


# # #Объединить все дублирующиеся записи о человеке в одну
# new_list_book2 = new_list_book.copy()
# # print(new_list_book2)
# new_list_book3 = list()

# for i in range(len(new_list_book)):
#   if new_list_book[i][0] == new_list_book[i+1][0]:
#     result =  new_list_book[i] + list(set(new_list_book[i+1]) - set(new_list_book[i]))
#     new_list_book3.append(result)
#   else:
#     new_list_book3.append(new_list_book[i])
#   print(new_list_book3)

# #ВАРИАНТ1 - Лагунцов не убирается
# for name in new_list_book:
#   for name2 in new_list_book2:
#     if name not in new_list_book3 and name[0] == name2[0]:
#       result =  name + list(set(name2) - set(name))
#       new_list_book3.append(result)
#       new_list_book2.pop(new_list_book2.index(name2))
#     elif name in new_list_book3 and name[0] == name2[0]:
#       new_list_book3.remove(name)
#       result =  name + list(set(name2) - set(name))
#       new_list_book3.append(result)
#       new_list_book2.pop(new_list_book2.index(name2))
# print(new_list_book3)

#ВАРИАНТ2 -
new_list_book5 = []
for i in range(len(new_list_book)):
  for j in range(len(new_list_book)):
    if new_list_book[i][0] == new_list_book[j][0]:
      new_list_book[i] = [x or y for x, y in zip(new_list_book[i], new_list_book[j])]
  if new_list_book[i] not in new_list_book5:
    new_list_book5.append(new_list_book[i])
print(new_list_book5)


# dict_book = {x[0]:x[1:] for x in new_list_book}
# print(dict_book)


# for key, value in dict_book.items():
#   for name in new_list_book:
#     if name[0] == key:
#       # dict_book[key] = name[1:]
#       # result = value + list(set(name[1:]) - set(value))
#       result = set(value + name[1:])
#       dict_book2[key] = result
#
# print(dict_book2)

# for key, value in dict_book.items():
#   for name in new_list_book:
#     if name[0] == key:
#       # dict_book[key] = name[1:]
#       # result = value + list(set(name) - set(value))
#       result = set(value + name)
#       new_list_book3.append(result)
#
# print(new_list_book3)

# a = [1, 2, 2]
# c = [2, 3]
# z = a + c
# b = set(a)
# print(b)
# print(z)

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook2.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_list_book5)

# #удалить все дубликаты
# first_list = [1, 2, 2, 5]
# second_list = [2, 5, 7, 9]
# result = list(set(first_list + second_list))
# print(result)
#
# # удалить элементы из второго списка, которые есть в первом
# first_list = [1, 2, 2, 5]
# second_list = [2, 2, 5, 7, 9]
# result = first_list + list(set(second_list) - set(first_list))
# print(result)

# #Есть 2 списка, которые я хотел бы объединить вместе. Поскольку большинство значений равны в соответствующих строках, я хотел бы создать один столбец с уникальным значением из каждой строки.
# #Здесь мы можем использовать or оператор:Учитывая, что первый элемент обладает правдивостью False (это относится к пустым строкам), он принимает второй элемент. В случае, если первый элемент обладает правдивостью True, он принимает первый элемент.
# list1 = ['','','dog','cat','cat']
# list2 = ['dog','','dog','cat','']
# l1 = [x or y for x, y in zip(list1, list2)]
# print(l1)
# #ОТВЕТ: ['dog', '', 'dog', 'cat', 'cat']
