# Это вы мне? Подсчитываем тёзок на каждом курсе

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
    course_dict = {"title": course, "mentors": mentor, "duration": duration}
    courses_list.append(course_dict)

# с этого момента начинается выполнение задания 4.
for course in courses_list:
    all_list = []
    all_names_list = []
    for m in course['mentors']:
        name = m.split()
        all_names_list.append(name)
    only_names = []
    for n in all_names_list:
        only_names.append(n[0])
    unique_sorted = sorted(set(only_names))
    ## 	# Внимание: в список same_name_list вы будете сохранять найденных тёзок-преподавателей
    same_name_list = []
    for n in unique_sorted:
        count_n = 0
        for z in course['mentors']:
            if n in z:
                count_n += 1
                if count_n > 1 and n not in same_name_list:
                    same_name_list.append(n)
    # print(same_name_list)
    same_name_list_res = []
    for i in same_name_list:
        for j in course['mentors']:
            if i in j:
                same_name_list_res.append(j)
    # print(sorted(same_name_list_res))
    print(f"На курсе {course['title']} есть тёзки: {', '.join(sorted(same_name_list_res))}")
