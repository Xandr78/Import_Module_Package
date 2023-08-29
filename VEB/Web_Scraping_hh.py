import requests
import bs4
import fake_headers
import json
import re

headers = fake_headers.Headers(browser = 'firefox', os = 'win')
headers_dict = headers.generate()

def find_job():
    response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2',headers = headers_dict)
    main_html_data = response.text
    main_html = bs4.BeautifulSoup(main_html_data,'lxml')
    vacancy_tags = main_html.find_all('div', class_= "vacancy-serp-item__layout")
    hh_data = {}
    filename = "hh.json"
    with open(filename, "w", encoding = "utf-8") as file:
        for vacancy_tag in vacancy_tags:
            hh_data["link"] = vacancy_tag.find('a', class_="serp-item__title").get('href')
            # вывод всех тербуемых навыков по ссылке на странице вакансии:
            description_text = requests.get(hh_data["link"], headers=headers_dict).text
            description_soup = bs4.BeautifulSoup(description_text, 'lxml')
            skills = description_soup.find_all('div', class_='bloko-tag bloko-tag_inline')

            skills_string = ' '.join(map(str, skills))
            pattern = r'>([A-Za-z]+)<'
            result_skills = re.findall(pattern, skills_string, flags=re.IGNORECASE)
            result_skills_str = ', '.join(map(str, result_skills))
            # print(result_skills_str)

            # выборка вакансий по необходимым навыкам:
            count = 0
            for j in required_skills:
                if j.lower() in result_skills_str.lower():
                    count += 1
                    if count == len(required_skills):
                        if vacancy_tag.find('span', class_="bloko-header-section-2") is not None:
                            hh_data["salary"] = vacancy_tag.find('span', class_="bloko-header-section-2").get_text()
                            # print(hh_data["salary"])
                        hh_data["name_vacancy"] = vacancy_tag.find('a', class_="serp-item__title").get_text()
                        hh_data["company"] = vacancy_tag.find('a', class_="bloko-link bloko-link_kind-tertiary").get_text()
                        hh_data["city"] = list(vacancy_tag.find(class_="vacancy-serp-item__info").children)[1].text
                        hh_data["Требуемые навыки"] = result_skills_str
                        print(hh_data["name_vacancy"], hh_data["link"], hh_data["salary"], hh_data["company"], hh_data["city"], hh_data["Требуемые навыки"])
                        json.dump(hh_data, file, ensure_ascii=False, indent=4)

if __name__=='__main__':
    required_skills = ["Django", "Flask"]
    find_job()