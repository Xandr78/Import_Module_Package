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
#print(mentors_names)
py_set = set(mentors_names[0])
jv_set = set(mentors_names[1])
fs_set = set(mentors_names[2])
fe_set = set(mentors_names[3])

py_jv = sorted(py_set & jv_set)
py_fs = sorted(py_set & fs_set)
py_fe = sorted(py_set & fe_set)
jv_fs = sorted(jv_set & fs_set)
jv_fe = sorted(jv_set & fe_set)
fs_fe = sorted(fs_set & fe_set)
for i in py_jv:
  py_jv_top = ', '.join(py_jv)
print(f"На курсах '{courses[0]}' и '{courses[1]}' преподают: {py_jv_top}")
for i in py_fs:
  py_fs_top = ', '.join(py_fs)
print(f"На курсах '{courses[0]}' и '{courses[2]}' преподают: {py_fs_top}")
for i in py_fe:
  py_fe_top = ', '.join(py_fe)
print(f"На курсах '{courses[0]}' и '{courses[3]}' преподают: {py_fe_top}")
for i in jv_fs:
  jv_fs_top = ', '.join(jv_fs)
print(f"На курсах '{courses[1]}' и '{courses[2]}' преподают: {jv_fs_top}")
for i in jv_fe:
  jv_fe_top = ', '.join(jv_fe)
print(f"На курсах '{courses[1]}' и '{courses[3]}' преподают: {jv_fe_top}")
for i in fs_fe:
  fs_fe_top = ', '.join(fs_fe)
print(f"На курсах '{courses[2]}' и '{courses[3]}' преподают: {fs_fe_top}")