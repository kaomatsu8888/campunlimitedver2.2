import requests # HTTP通信を行う
from bs4 import BeautifulSoup # HTMLを解析する
import urllib #絶対URLならそのまま。相対URLなら絶対URLに変換

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url) # HTMLを取得
soup = BeautifulSoup(html.content, "html.parser") # HTMLを解析

# すべてのimgタグを検索して、リンクを取得する
for element in soup.find_all("img"): # imgタグを取得
    src = element.get("src") # imgタグのsrc属性を取得

    # 絶対URLに変換,ファイルを表示する
    image_url = urllib.parse.urljoin(load_url, src)
    filename = image_url.split("/")[-1] # 画像ファイル名
    print(image_url, ">>", filename) # ファイル名を表示 
