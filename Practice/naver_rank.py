# Naver에서 html 파일을 가지고 온다.
# BeautifulSoup를 이용해서 parsing 한다.
# 실시간 검색어 10위까지 출력한다.
# BeautifulSoup4 : HTML Parsing libarary   # HTML을 분석해서 추출하는 라이브러리

import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
# 방법1
# results = soup.find_all("span", class_="ah_k")
# 방법2
results = soup.select(".ah_roll.PM_CL_realtimeKeyword_rolling_base .ah_k")
# .       .                              space.

index = 0
for result in results:
    index = index + 1
    print(index, result.text)

# top10 = bs.find(class_="ah_item").text
# print(bs.find("h3").text)
# print(top10)


