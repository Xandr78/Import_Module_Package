from bs4 import BeautifulSoup
import requests
from fake_headers import Headers
import re
import json

headers = Headers(browser='firefox', os='win')
headers_data = headers.generate()

#выборка названия компании, вакансии, города и з\п:
def find_job():
    html_text = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=headers_data).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all(class_='serp-item')
    list_jobs = []
    for job in jobs:
        vacancy_name = job.h3.span.a.text
#з\п никак не выводится???
        salary = job.find(attrs={'data-qa':'vacancy-serp__vacancy-compensation'})

        company = job.find('div',class_='vacancy-serp-item__meta-info-company').a.text
        town_html = job.find('div',class_='vacancy-serp-item__info')
        town = town_html.find(attrs={'data-qa':'vacancy-serp__vacancy-address'}).text
        url = job.h3.span.a['href']

#вывод всех тербуемых навыков по ссылке на странице вакансии:
        description_text = requests.get(url, headers=headers_data).text
        description_soup = BeautifulSoup(description_text,'lxml')
        skills = description_soup.find_all('div', class_='bloko-tag bloko-tag_inline')

        skills_string = ' '.join(map(str, skills))
        pattern = r'>([A-Za-z]+)<'
        result_skills = re.findall(pattern, skills_string, flags=re.IGNORECASE)
        result_skills_str = ', '.join(map(str, result_skills))

#выборка вакансий по необходимым навыкам:
        count = 0
        for j in required_skills:
            if j.lower() in result_skills_str.lower():
                count += 1
                if count == len(required_skills):
                    dict_skills = {}
                    skills_list = []
                    skills_list.append(f'Компания: {company}')
                    skills_list.append(f'Город: {town}')
                    skills_list.append(f'Ссылка: {url}')
                    skills_list.append(f'З\п: {salary}')
                    dict_skills[vacancy_name] = skills_list
                    list_jobs.append(dict_skills)

#запись полученного словаря в json-файл:
    with open('jobs.json', 'w', encoding="utf-8") as f:
        json.dump(list_jobs, f, ensure_ascii=False, indent=4)
        print(list_jobs)

#точка входа:
if __name__=='__main__':
    required_skills = ['python']
    find_job()