import PySimpleGUI as sg # pysimpleguiのインポート
from pathlib import Path # Path クラスのインポート
import chardet # chardetのインポート
sg.theme("Darkbrown3") # テーマの設定

layout = [[sg.B("ファイルを開く", k="btn1"), sg.T(k="txt1")], # ボタンコンポーネントの追加
        [sg.B("ファイルを保存", k="btn2")], 
        [sg.ML(k="txt2", font=(None, 14), size=(80, 15))]] # マルチラインテキストコンポーネントの追加d
win = sg.Window("テキストファイルの保存", layout, resizable=True) # Windowの生成

loadname = None # ファイル名の初期化
enc = "UTF-8" # 文字コードの初期化
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
        win["txt1"].update(f"{loadname}の文字コードは{enc}です。") # ラベルの文字列を変更
        win["txt2"].update(txt) # ラベルの文字列を変更

def savetext(): # ボタンが押されたときの処理
    global loadname, enc # -*- coding=utf-8 -*-
    savename = sg.popup_get_file("保存するファイル名を入力してください", default_path = loadname, save_as=True) # ファイルを保存する
    if not savename: # ファイルを選択しなかったとき
        sg.popup_get_file("保存するファイル名を入力してください", save_as=True) # ファイルを保存する
        return
    if savename.find(".") == -1: # 拡張子がないとき
        savename = savename + ".txt" # 拡張子を追加
    p = Path(savename) # ファイルパスを取得
    p.write_text(values["txt2"], encoding=enc) # ファイルを保存する
    win["txt1"].update(f"{savename}を保存しました。") # ラベルの文字列を変更
    loadname = savename # ファイル名を更新

while True: # イベントループ
    event, values = win.read() # イベントの読み取り
    if event == "btn1": # ボタンが押されたときの処理
        loadtext() # loadtext()関数の呼び出し
    if event == "btn2": # ボタンが押されたときの処理
        savetext() # savetext()関数の呼び出し
    if event == None: # ウィンドウ閉じるイベントの検出
        break # イベントループを抜ける
    
win.close() # ウィンドウを閉じる
    
