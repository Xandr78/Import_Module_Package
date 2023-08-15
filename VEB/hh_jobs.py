import json
import re

from bs4 import BeautifulSoup
import requests
from fake_headers import Headers


headers = Headers(browser='firefox', os='win')
headers_data = headers.generate()
html_text = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=headers_data).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find(class_='serp-item')
vacancy_name = jobs.h3.span.a.text
salary = jobs.find(attrs={'data-qa':'vacancy-serp__vacancy-compensation'})
company = jobs.find('div',class_='vacancy-serp-item__meta-info-company').a.text
town_html = jobs.find('div',class_='vacancy-serp-item__info')
town = town_html.find(attrs={'data-qa':'vacancy-serp__vacancy-address'}).text
url = jobs.h3.span.a['href']

description_text = requests.get(url, headers=headers_data).text
description_soup = BeautifulSoup(description_text,'lxml')
skills = description_soup.find_all('div',class_='bloko-tag bloko-tag_inline')
skills_string = ' '.join(map(str,skills))
pattern = r'>([A-Za-z]+)<'
result_skills = re.findall(pattern,skills_string, flags=re.IGNORECASE)
result_skills_str = ', '.join(map(str,result_skills))
dict_jobs = {}
dict_skills = {}
skills_list = []
skills_list.append(f'Компания: {company}')
skills_list.append(f'Город: {town}')
skills_list.append(f'Ссылка: {url}')
skills_list.append(f'З\п: {salary}')
dict_skills[vacancy_name]=skills_list
dict_jobs.update(dict_skills)
with open('jobs.json', 'w', encoding="utf-8") as f:
    json.dump(dict_jobs, f, ensure_ascii=False, indent=4)
# dict_jobs.update(dict_skills)
# print(f'Вакансия: {vacancy_name}')
# print(f'З\п: {salary}')
# print(f'Компания: {company}')
# print(f'Город: {town}')
# print(f'Ссылка: {url}')
# print(f'Навыки: {result_skills_str}')
print(dict_jobs)
print()
