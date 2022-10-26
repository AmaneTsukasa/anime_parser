import requests
from bs4 import BeautifulSoup as BS

page = 1

while True:
    r = requests.get('https://animedub.ru/anime/komedija/page/'+str(page))
    html = BS(r.content, 'html.parser')
    items = html.select('.floaters > .mov-t')

    if (len(items)):
        for el in items:
            title = el.select('h2')
            print(title[0].text)
        page += 1
    else:
        break

