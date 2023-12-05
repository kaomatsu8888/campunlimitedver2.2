import requests
from bs4 import BeautifulSoup

# URLを指定
load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url) # HTMLを取得
soup = BeautifulSoup(html.content, "html.parser") # HTMLを解析

#title,h2,liタグを検索してその文字列を表示(タグが外れる)
print(soup.find("title").text) # titleタグを検索して表示
print(soup.find("h2").text) # h2タグを検索して表示
print(soup.find("li").text) # liタグを検索して表示


