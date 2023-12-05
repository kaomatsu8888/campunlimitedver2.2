import requests # HTTP通信を行う
from bs4 import BeautifulSoup # HTMLを解析する
from pathlib import Path # ファイル名を操作する
import urllib #絶対URLならそのまま。相対URLなら絶対URLに変換
import time # 1秒待つ

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url) # HTMLを取得
soup = BeautifulSoup(html.content, "html.parser") # HTMLを解析

# 保存用フォルダを作成
out_folder = Path("download") # フォルダ名downloadを指定
out_folder.mkdir(exist_ok=True) # すでにフォルダがあれば何もしない

# すべてのimgタグを検索して、リンクを取得する
for element in soup.find_all("img"): # imgタグを取得
    src = element.get("src") # imgタグのsrc属性を取得

    # 絶対URLに変換,画像データを取得する
    image_url = urllib.parse.urljoin(load_url, src)
    imgdata = requests.get(image_url)

    # URLから最後のファイル名を取り出して、保存ファイル名とつなげる
    filename = image_url.split("/")[-1] # 画像ファイル名
    out_path = out_folder.joinpath(filename) # 保存ファイル名

    # 画像データをファイルに書き出す
    with open(out_path, mode="wb") as f: # 書き込みモードで開く
        f.write(imgdata.content) # 画像データを書き込む

# 1回アクセスしたので1秒待つ
time.sleep(1)

