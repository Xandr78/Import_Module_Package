import re
import csv

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern_phone = re.compile(
    r'(\+7|8)\s*\(?(\d{3})\)?(\s*|-)(\d{3})(\s*|-*)(\d{2})-?(\d{2})(\s*(\(?(\доб.)?)\s*(\d{4}))?(\))*')
pattern_words = re.compile(
    r'(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё]\w+[А-яЁё –]*\–*\s*)*\,*(\+*\d\s*\(*\d+\)*\-*\s*\d+\-*\d+\-*\d+\s*\(*\w*\.*\s*\d*\)*)*\,*(\w+\.*\w*\@\w+\.\w+)*')

new_info_list = []

for i in range(len(contacts_list)):
    if i == 0:
        new_info_list.append(contacts_list[i])
    else:
        line = ','.join(contacts_list[i])
        result = re.search(pattern_words, line)
        new_info_list.append(list(result.groups()))
        if new_info_list[i][0] in new_info_list:
            print(new_info_list[i][0:3])
        if new_info_list[i][5] != None:
            new_info_list[i][5] = pattern_phone.sub(r'+7(\2)\4-\6-\7 \10\11', new_info_list[i][5])

print(new_info_list)

fixed_info_list = []
for i in range(len(new_info_list)):
    for j in range(len(new_info_list)):
        if new_info_list[i][0] == new_info_list[j][0]:
            new_info_list[i] = [x or y for x, y in zip(new_info_list[i], new_info_list[j])]
    if new_info_list[i] not in fixed_info_list:
        fixed_info_list.append(new_info_list[i])
print(fixed_info_list)

with open("phonebook1.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(fixed_info_list)

