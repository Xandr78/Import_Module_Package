# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
import requests
f   rom fake_headers import Headers
import bs4
headers = Headers(browser='firefox', os='win')
headers_data = headers.generate()
#"""<span id="ip">95.46.195.232</span>"""

# response = requests.get('https://www.myip.com/', headers=headers_data)
response = requests.get('https://www.iplocation.net/', headers=headers_data)
# soup = bs4.BeautifulSoup(html_data, 'lxml')
html_data = response.text
soup = bs4.BeautifulSoup(html_data, 'lxml')
tag = soup.find('span', id='ip')
tag_div = soup.find('div', id = 'ip-placeholder')
tag_p = tag_div.find_all('p')[0]
tag_span = tag_p.find_all('span')[0]
print(tag_span.text)