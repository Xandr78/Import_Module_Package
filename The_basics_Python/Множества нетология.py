courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
count_num = 0
mentors_names = []
for m in mentors:
  course_names = []
  for name in m:
    name_list = name.split()
    course_names.append(name_list[0])
  mentors_names.append(course_names)
print(mentors_names)
# py_set = set(mentors_names[0])
# jv_set = set(mentors_names[1])
# fs_set = set(mentors_names[2])
# fe_set = set(mentors_names[3])
#print(py_set & jv_set)
#mentors_names_copy = mentors_names.copy()
#j = 1
# for i in mentors_names:
#   if j != 
#   # for j in mentors_names_copy:
#   i_set = set(i)
#   j_set = set(mentors_names[j])
#   if set(i) - set(j) != set():
#     print(i_set, j_set)
#   j += 1
pairs = []
i = 0
j = 0
while i != len(mentors_names):
  j += 1
  
  print(set(mentors_names[i] & set(mentors_names[j])
  if j != len(mentors_names):
    continue
  else:
    i += 1
    j  = i
    continue



# # count_list = 0
# # all_names = []
# mentors_names_copy = mentors_names.copy()
# for i in mentors_names:
#   for j in mentors_names_copy:
#     if set(i) != set(j):
#       for x in i:
#         if (x in j) and (x not in pairs):
#           pairs.append([x, mentors_names.index(i)])
# print(pairs)
# pairs_sort = []
# pairs_str = []
# for i in pairs:
#   pairs_str.append(str(i[0] + str(i[1])))
  
# print(pairs_str)
# pairs_sort = sorted(pairs_set)
# print(pairs_sort)

# # делаем список списков имен
# mentors_names = []
# for m in mentors:
# 	course_names = []
# 	for name in m:
# 		course_names.append(...) # допишите код здесь
# 	# допишите ниже код, который добавляет списки имен в общий список mentors_names:
# 	...

# # храните здесь пары курсов, на есть совпавшие имена
# pairs = []
# # # попарное сравнение "наборов" преподавателей на курсах. каждую новую пару запоминаем для исключения повторов.
# for id1 in range(len(mentors_names)):
# 	for id2 in range(len(mentors_names)):
# 		# проверьте, что вы не сравниваете список сам с собой:
# 		...
# 		# допишите ниже код для сравнения двух "наборов" преподавателей. подсказка: используйте множества
# 		intersection_set = ...
# 		if len(...) > 0: # допишите проверку, что результат не пустой, имена есть
# 			# допишите ниже код, который проверяет, что эта пара еще не встречалась
# 			pair = ...
# 			# и если pair еще не встречалась, то выведите на экран два курса и список преподавателей, которые есть на обоих курсах
# 			if pair ...:
# 				pairs.append(pair)
# 				# отсортируйте имена по алфавиту. подсказка: используйте sorted() для списка
# 				all_names_sorted = sorted(...)
# 				# допишите конструкцию вывода результата. можете использовать string.join()
# 				print(f"На курсах '{courses[...]}' и '{courses[...]}' преподают: {...}")