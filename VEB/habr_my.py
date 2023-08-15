import requests
from fake_headers import Headers
import bs4

headers = Headers(browser='firefox', os='win')
headers_data = headers.generate()
# response = requests.get('https://www.myip.com/', headers=headers_data)
main_page_html = requests.get('https://habr.com/ru/all/', headers=headers_data).text
main_page_soup = bs4.BeautifulSoup(main_page_html, 'lxml')

# tag_div = main_page_soup.find('div', class_='tm-articles-list')
# tag_article = tag_div.find('article', id='752836')
# tag_h2 = tag_article.find('h2', class_='tm-title tm-title_h2')
# tag_span = tag_h2.find('span')
tag_article = main_page_soup.find_all('article')
for article in tag_article:
    # name = article.h2.text
    title = article.find('h2', class_='tm-title tm-title_h2').text
    # print(name)
    print(title)
    # print(tag_article)
# print(tag_span)