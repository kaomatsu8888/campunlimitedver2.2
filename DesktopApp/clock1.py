import PySimpleGUI as sg # pysimpleguiのインポート
import datetime # datetimeのインポート
sg.theme("Darkbrown3") # テーマの設定

layout = [[sg.T("0000/00/00 (---)", font=("Arial", 40), k="txt2" ,size=(20,1), justification="center")], #
[sg.T("AM 0:00:00", font=("Arial", 40), k="txt1", size=(20,1), justification="center")]] # テキストコンポーネントの追加

win = sg.Window("時計", layout, size=(480, 150), keep_on_top=True) # Windowサイズの設定

def execute(): # ボタンが押されたときの処理
    now = datetime.datetime.now() # 現在の日時を取得
    win["txt2"].update(f"{now:%Y/%m/%d (%a)}") # ラベルの文字列を変更
    win["txt1"].update(f"{now:%p %I:%M:%S}") # ラベルの文字列を変更

while True: # イベントループ
    event, values = win.read(timeout=500) # イベントの読み取り
    execute() # execute()関数の呼び出し
    if event == None: # ウィンドウ閉じるイベントの検出
        break # イベントループを抜ける

win.close() # ウィンドウを閉じる

