import requests
from bs4 import BeautifulSoup
import urllib #絶対URLならそのまま。相対URLなら絶対URLに変換

# URLを指定
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url) # HTMLを取得
soup = BeautifulSoup(html.content, "html.parser") # HTMLを解析

# ファイルを書き込みモードで開く
filename = "links.txt"
with open(filename, "w") as f: # 書き込みモードで開く
    # すべてのaタグを検索して、リンクを表示する
    for element in soup.find_all("a"):
        url = element.get("href")
        link_url = urllib.parse.urljoin(load_url, url)# 絶対URLに変換
        f.write(element.text+"\n")# リンクの文字列を書き込む
        f.write(link_url+"\n")
        f.write("\n")
