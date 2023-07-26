from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

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
  return result_FIO
# print(result_FIO_sub)
# print(FIO(text))

##### основной блок
new_list_book = list()
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
# print(new_list_book)


# # #Объединить все дублирующиеся записи о человеке в одну
#РАБОТАЕТ
new_list_book5 = []
for i in range(len(new_list_book)):
  for j in range(len(new_list_book)):
    if new_list_book[i][0] == new_list_book[j][0]:
      new_list_book[i] = [x or y for x, y in zip(new_list_book[i], new_list_book[j])]
  if new_list_book[i] not in new_list_book5:
    new_list_book5.append(new_list_book[i])
print(new_list_book5)

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_list_book5)
