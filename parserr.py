import requests
from bs4 import BeautifulSoup as bs

actives_url = 'https://freesteam.ru/category/active/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'accept': '*/*'}
output = []

def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r

def get_content(html):
    soup = bs(html, 'html.parser')
    all = soup.find_all('div', class_="col-lg-4 col-md-4 three-columns post-box")
    for item in all:
        nameAndUrl = item.find('h2', class_="entry-title")
        name = nameAndUrl.a.text
        url = nameAndUrl.a.get('href')
        artifacts = item.find('span', class_="entry-cats")
        platform = artifacts.a.text
        image = item.find('img')
        #print(image['data-src'])
        #print(name, url, platform)
        output.append([platform, name, url, image['data-src']])
    return output


def parse():
    html = get_html(actives_url)
    if html.status_code == 200:
        pass
        output = get_content(html.text)
        return output
    else:
        print('Error')