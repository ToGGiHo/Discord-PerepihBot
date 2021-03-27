import requests
from bs4 import BeautifulSoup as bs

actives_url = 'https://s1.torrents-igruha.org/index.php?do=search'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'accept': '*/*'}
output = []

def get_html(url, search=None):
    r = requests.post(url, headers=headers, params=
{'do': 'search',
'subaction': 'search',
'search_start': 1,
'full_search': 0,
'result_from': 1,
'story': search}, verify=False)
    return r

def get_content(html):
    soup = bs(html, 'html.parser')
    all = soup.find_all('div', class_="article-film-image")
    output = []
    for i in all:
        output.append([i.a['href'], i.a.img['title'], i.a.img['src']])
    return output


def parse(toFind):
    html = get_html(actives_url, toFind)
    if html.status_code == 200:
        #pass
        getet = get_content(html.text)
        return getet
    else:
        print('Error')