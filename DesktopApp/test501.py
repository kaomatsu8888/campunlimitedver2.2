import chardet # 文字コード判定ライブラリ
def loadtext(filename): # テキストファイルを読み込む
    with open(filename, 'rb') as f: # バイナリモードで開く
        b = f.read() # バイナリデータを読み込む
        enc = chardet.detect(b) # 文字コードを自動判別
        print(f"{filename}の文字コードは{enc['encoding']}です。")
loadtext("utest.txt")
loadtext("stest.txt")
