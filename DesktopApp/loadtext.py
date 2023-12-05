import PySimpleGUI as sg # pysimpleguiのインポート
from pathlib import Path # Path クラスのインポート
import chardet # chardetのインポート
sg.theme("Darkbrown3") # テーマの設定

layout = [[sg.B("ファイルを開く", k="btn1"), sg.T(k="txt1")], # ボタンコンポーネントの追加
    [sg.ML(k="txt2", font=(None, 14), size=(80, 15))]] # マルチラインテキストコンポーネントの追加d
win = sg.Window("テキストファイルの読み込み", layout) # Windowの生成

def loadtext():
    global loadname, enc # -*- coding=utf-8 -*-
    loadname = sg.popup_get_file("テキストファイルを選択してください")
    if not loadname:
        return # ファイルを選択しなかったとき
    with open(loadname, "rb") as f: # ファイルを読み込む
        b = f.read() # ファイルを読み込む
        enc = chardet.detect(b)["encoding"] # 文字コードを判定 
        p = Path(loadname) # ファイルパスを取得
        txt = p.read_text(encoding=enc) # ファイルを読み込む
        win["txt1"].update(f"{loadname}の文字コードは{enc}です。")
        win["txt2"].update(txt)

while True: # イベントループ
    event, values = win.read() # イベントの読み取り
    if event == "btn1": # ボタンが押されたときの処理
        loadtext() # loadtext()関数の呼び出し
    if event == None: # ウィンドウ閉じるイベントの検出
        break # イベントループを抜ける
    
win.close() # ウィンドウを閉じる
