from pathlib import Path

def savetext(filename):
    p = Path(filename) # ファイルパスを作成
    txt = " 書き出しテスト用テキストデータです。"
    p.write_text(txt, encoding="utf-8") # ファイルに書き出す

savetext("output.txt") # ファイルに書き出す


