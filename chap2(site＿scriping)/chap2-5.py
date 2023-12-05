import requests
from bs4 import BeautifulSoup

# URLを指定
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url) # HTMLを取得
soup = BeautifulSoup(html.content, "html.parser") # HTMLを解析

# IDで検索して、そのタグの中身を表示
chap2 = soup.find(id="chap2")
for element in chap2.find_all("li"):
    print(element.text) # liタグの文字列を表示
