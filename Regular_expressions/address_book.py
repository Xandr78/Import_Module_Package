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

# for i in contacts_list:
#   for j in i:
#     print(j)

## 1. Выполните пункты 1-3 задания.
## Ваш код
#поиск и преобразование телефонов
def phone(a):
  pattern_phone = r'(\+7|8)\s*\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{2})[- ]?(\d{2})\s*(\(?([а-яё]{3}\.)[ ](\d{4})\)?)?'
  new_pattern_phone = r'+7(\2)\3-\4-\5 \7\8'
  result = re.sub(pattern_phone, new_pattern_phone, a)
  return result
print(phone(text))

# поиск ФИО
def FIO(f):
  pattern_FIO = r'[A-ZА-ЯЁ]{1}[a-zа-яё]+[ ,]'
  result_FIO = re.findall(pattern_FIO, text)
# pattern_FIO_sub = r'[A-ZА-ЯЁ]{1}[a-zа-яё]+[,]'
# result_FIO_sub = re.sub(pattern_FIO, pattern_FIO_sub, text)
  return result_FIO
# print(result_FIO_sub)
# print(FIO(text))
# поиск организации и должности
pattern_ORG = r'[ ,]'

##### основной блок
new_list = list()
for i in contacts_list:
  result_name = ' '.join(i[:3])
  result_name_re = FIO(result_name)

  print(result_name)
  # new_list.append(result_name)
  new_list1 = [result_name_re, i[3], i[4], phone(i[5]), i[6]]
  # print(new_list1)
  new_list.append(new_list1)
# print(new_list)

#Объединить все дублирующиеся записи о человеке в одну
new_list2 = list()



# for i in contacts_list:
#   for j in i:
#     result = re.sub(pattern_phone, new_pattern_phone, j)
#     pprint(result)

#
#     result_list = list()
#     for i in contacts:
#         if i not in result_list:
#             result_list.append(i)
#
#     return result_list

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')

## Вместо contacts_list подставьте свой список:
# datawriter.writerows(contacts_list)
