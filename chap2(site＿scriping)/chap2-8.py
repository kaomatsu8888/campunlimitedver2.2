import requests
from bs4 import BeautifulSoup
import urllib #絶対URLならそのまま。相対URLなら絶対URLに変換

# URLを指定
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url) # HTMLを取得
soup = BeautifulSoup(html.content, "html.parser") # HTMLを解析

# すべてのaタグを検索して、リンクを表示する
for element in soup.find_all("a"):
    print(element.text)
    url = element.get("href")
    # print(url) 相対URLを表示
    link_url = urllib.parse.urljoin(load_url, url)# 絶対URLに変換
    print(link_url) # リンクを表示
