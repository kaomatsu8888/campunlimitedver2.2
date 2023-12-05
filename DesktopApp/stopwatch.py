import PySimpleGUI as sg # pysimpleguiのインポート
import datetime # datetimeのインポート
sg.theme("Darkbrown3") # テーマの設定

layout = [[sg.T("0:00:00:000000", font=("Arial", 40), k="txt", size=(15,1), justification="center")], # テキストコンポーネントの追加
        [sg.Push(), sg.B("START/STOP", k="btn"), sg.Push(), ]] # ボタンコンポーネントの追加

win = sg.Window("ストップウォッチ", layout, font=(None,14), size=(400, 120), keep_on_top=True) # Windowサイズの設定

def execute(): # ボタンが押されたときの処理
    if startflag == True: # スタートフラグがTrueのとき
        now = datetime.datetime.now() # 現在の日時を取得
        td = now - start # 経過時間を計算
        win["txt"].update(td) # ラベルの文字列を変更

def startstop(): # ボタンが押されたときの処理
    global start, startflag # グローバル変数の宣言
    if startflag == True: # スタートフラグがTrueのとき
        startflag = False # スタートフラグをFalseにする
    else: # スタートフラグがFalseのとき
        start = datetime.datetime.now() # 現在の日時を取得
        startflag = True

startflag = False # スタートフラグの初期化
while True: # イベントループ
    event, values = win.read(timeout=50) # イベントの読み取り
    execute() # execute()関数の呼び出し
    if event == "btn": # ボタンが押されたときの処理
        startstop() # startstop()関数の呼び出し
    if event == None: # ウィンドウ閉じるイベントの検出
        break # イベントループを抜ける
win.close() # ウィンドウを閉じる
