# 時間割アプリを作成
import PySimpleGUI as sg
import datetime
sg.theme("Darkbrown3")

layout = [[sg.T("00:00:00", font=("Arial", 24), k="txt1")], # テキストコンポーネントの追加
        [sg.ML(font=("Arial", 18), size=(40, 10), k="txt2")]] # マルチラインテキストコンポーネントの追加
win = sg.Window("時間割アプリ", layout, font=(None, 14), size=(450,250), keep_on_top=True) # Windowサイズの設定

sch = [["1時限",8,50], # 時間割を格納するリスト
        ["2時限",10,30],
        ["昼休み",12,40],
        ["3時限",13,20],
        ["4時限",15,50],
        ["5時限",17,00],
        ["6時限",16,50]]

def execute():
    now = datetime.datetime.now() # 現在の日時を取得
    #now = now.replace(hour=10) # テスト用
    win["txt1"].update(f"{now:%H:%M:%S}") # ラベルの文字列を変更
    txt2 = ""
    for s in sch:
        dt = now.replace(hour=s[1], minute=s[2], second=0) - now # 経過時間を計算
        if dt.total_seconds() > 0: # 経過時
            txt2 += f"{s[0]} 【{s[1]:02d}:{s[2]:02d}】あと{dt}です。\n"
        else: # 経過時
            txt2 += f"{s[0]} 【{s[1]:02d}:{s[2]:02d}】---\n"
    win["txt2"].update(txt2) # ラベルの文字列を変更

while True: # イベントループ
    event, values = win.read(timeout=500) # イベントの読み取り
    execute() # execute()関数の呼び出し
    if event == None: # ウィンドウ閉じるイベントの検出
        break # イベントループを抜ける
    execute() # execute()関数の呼び出し
    
win.close() # ウィンドウを閉じる
