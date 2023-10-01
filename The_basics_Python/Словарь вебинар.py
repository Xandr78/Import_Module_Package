countries_dict = {"Россия":"Москва", "Белоруссия":"Минск", "Франция":"Париж", "Германия":"Берлин"}
countries2_dict = {"Англия":"Лондон", "Италия":"Рим", "США":"Вашингтон"}
phonecodes_dict = {(7, 495):'Москва'}
#print(countries_dict[key])
for country in countries_dict:
    print(country)
for country, city in countries_dict.items():
    print(f'{country}: {city}')
for country in countries_dict:
    print(country, countries_dict[country])
new_countries_dict = countries_dict.copy()
print(new_countries_dict)
new_countries_dict.update(countries2_dict)
print(new_countries_dict)  
new_countries_dict["Турция"] = "Анкара"
print(new_countries_dict)
new_countries_dict['Греция'] = "Афины"
print(new_countries_dict)
new_countries_dict.setdefault("Египет","Александрия")
print(new_countries_dict)
if "Турция" in new_countries_dict.keys():
    del new_countries_dict["Турция"]
print(new_countries_dict)
city = phonecodes_dict[(7, 495)]
value_list = list(countries_dict.values())
key_list = list(countries_dict.keys())
print(value_list, key_list)
index_city = value_list.index(city)
country_res = key_list[index_city]
print(country_res)



    