import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
coins = soup.select('.coin_list tr')    # <tbody class="coin_list"> 안에 <tr>을 가져오겠다는 말

with open('bithumb.csv', 'w', encoding='utf-8') as f:
    for coin in coins:
        name = coin.select_one('td:nth-child(1) p a strong').text.replace(' ', '')      #td에서 두 번째를 가져오겠다.
        price = coin.select_one('td:nth-child(2) strong').text.replace(',', '')         #td에서 두 번째를 가져오겠다.
        #print(name, price)
        f.write(f'{name},{price}''\n')



