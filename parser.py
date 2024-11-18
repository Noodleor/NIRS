from bs4 import BeautifulSoup
import requests

url = 'https://ria.ru'

page = requests.get(url)

print(page.status_code)

filteredNews = []
allNews = []

soup = BeautifulSoup(page.text, "html.parser")

print(soup)

allNews = soup.findAll('div', class_='cell-list__item m-no-image')

for data in allNews:
    print(data)
    if data.find('span', class_='cell-list__item-title') is not None:
        filteredNews.append(data.text)


for data in filteredNews:
    print(data)