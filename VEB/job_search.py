import re
from bs4 import BeautifulSoup
import requests
from fake_headers import Headers

headers = Headers(browser='firefox', os='win')
headers_data = headers.generate()
def find_jobs():
    html_text = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2',headers=headers_data).text
    soup = BeautifulSoup(html_text, 'lxml')
    # jobs = soup.find('div',class_='serp-item')
    jobs = soup.find_all('div', class_='serp-item')
    for job in jobs:
        # company = jobs.find('a', class_='serp-item__title').text.replace(' ','')
        vacancy_title = job.find('a', class_='serp-item__title').text
        vacancy_html = job.find('a', class_='serp-item__title')
        vacancy_url = job.h3.a['href']
        vacancy_name = job.find('div', class_='vacancy-serp-item__meta-info-company').text
        vacancy_town_html = job.find('div', class_='vacancy-serp-item__info')
        vacancy_town = vacancy_town_html.find(attrs={'data-qa': 'vacancy-serp__vacancy-address'}).text
        # print(jobs)
        # print(vacancy_url)
        vacancy_text = requests.get(vacancy_url,headers=headers_data).text
        soup_vacancy = BeautifulSoup(vacancy_text,'lxml')
        div = soup_vacancy.find('div',class_='vacancy-section').text
        div_vacancy_title = soup_vacancy.find('div', class_='vacancy-title')
        div_vacancy_title_salary = div_vacancy_title.span.text
        div_rep = div.replace(',','')
        div_lower = div_rep.lower().split()
        # print(re.search(skill, div,re.IGNORECASE))
        # if skill.lower() in div_lower:
        #     print(vacancy_title)
        count = 0
        for j in skills:
            if j.lower() in div_lower:
                count += 1
                if count == len(skills):
                    print(f'Вакансия: {vacancy_title}')
                    print(f'Ссылка: {vacancy_url}')
                    print(f'З\п: {div_vacancy_title_salary}')
                    print(f'Название компании: {vacancy_name}')
                    print(f'Город: {vacancy_town} \n')

if __name__=='__main__':
    # skills = ["Django", "Flask"]
    skills = ["python"]
    # skills = [i for i in input('Введите наименование желаемых навыков: ').split()]
    find_jobs()