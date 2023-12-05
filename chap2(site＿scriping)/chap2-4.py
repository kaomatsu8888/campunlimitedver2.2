import requests
from bs4 import BeautifulSoup

# URLを指定
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url) # HTMLを取得
soup = BeautifulSoup(html.content, "html.parser") # HTMLを解析

# すべてのliタグを検索して表示
for element in soup.find_all("li"):
    print(element.text) # liタグの文字列を表示


