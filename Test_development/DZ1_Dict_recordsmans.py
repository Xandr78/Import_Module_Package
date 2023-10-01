courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

def dict_recordsmans(cur_list, men_list, dur_list):
	courses_list = []
	# допишите код, который генерирует словарь-курс с тремя ключами: "title", "mentors", "duration"
	for t, m, d in zip(cur_list, men_list, dur_list):
		course_dict = {"title":t, "mentors":m, "duration":d}
		courses_list.append(course_dict)
	min_d = 100
	max_d = 0
	for d in dur_list:
	  if min_d > d:
		  min_d = d
	  elif max_d < d:
		  max_d = d
	# # подсказка 2: не забудьте, что индекс можно удобно получить функцией enumerate
	index_max = []
	index_min = []
	for index, d in enumerate(dur_list):
		if d == max_d:
			index_max.append(index)
		elif d == min_d:
			index_min.append(index)
	courses_min = []
	courses_max = []
	for id in index_min:
		courses_min.append(courses_list[id]['title'])
	# допишите код, который берет по id нужный курс из courses_list и получает название курса из ключа "title"
	res_courses = ""
	for id in index_max:
		courses_max.append(courses_list[id]['title'])
	# print(f"Самый короткий курс(ы): {', '.join(courses_min)} - {min_d} месяца(ев)")
	# print(f"Самый длинный курс(ы): {', '.join(courses_max)} - {max_d} месяца(ев)")
	res_courses = res_courses + f"Самый короткий курс(ы): {', '.join(courses_min)} - {min_d} месяца(ев)" + '\n' + f"Самый длинный курс(ы): {', '.join(courses_max)} - {max_d} месяца(ев)"

	return res_courses

if __name__=='__main__':
	print(dict_recordsmans(courses, mentors, durations))