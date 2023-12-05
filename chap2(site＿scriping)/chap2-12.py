import requests
from pathlib import Path

# 保存用フォルダを作る
out_forder = Path ("download")
out_forder.mkdir(exist_ok=True)

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

# URLから最後のファイル名を取り出す
filename = image_url.split("/")[-1]# 画像ファイル名を取得
out_path = out_forder.joinpath(filename)

# 画像データをファイルに書き込む
with open(filename, mode="wb") as f:
    f.write(imgdata.content)# 画像データを書き込む

# 後で動かすhttpのエラーのため
