import requests # requestsモジュールをインポート

url = "https://www.ymori.com/books/python2nen/test1.html" # URLを指定
response = requests.get(url) # URLにアクセスする

response.encoding = response.apparent_encoding # 文字化け対策
print(response.text) # URLのHTMLを表示

filename = "download.txt" # ファイル名を指定
f = open(filename, "w") # 書き込みモードで開く

f.write(response.text) # HTMLをファイルに書き込む
f.close() # ファイルを閉じる
