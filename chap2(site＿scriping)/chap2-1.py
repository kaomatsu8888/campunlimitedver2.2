import requests
from bs4 import BeautifulSoup

# URLを指定
load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url) # HTMLを取得
soup = BeautifulSoup(html.content, "html.parser") # HTMLを解析

print(soup) # HTMLを表示


