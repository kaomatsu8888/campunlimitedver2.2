import PySimpleGUI as sg #pysimpleguiのインポート

layout = [[sg.Input("フタバ", k="txt")], #入力欄の作成
        [sg.Button("実行", k="btn")], #ボタンの作成 
        [sg.Text(k="txt")]] #テキストの作成
window = sg.Window("テスト", layout) #ウィンドウの作成

def execute(): # ボタンが押されたときの処理
    txt = "こんにちは、"+values["txt"]+"さん" # ラベルに表示する文字列
    window["txt"].update(txt) # ラベルの文字列を変更

while True: #無限ループ
    event, values = window.read() #イベントの読み取り
    if event == "btn": #ボタンが押されたとき
        execute() #execute()の実行
    if event == None: #ウィンドウが閉じられたとき
        break #無限ループの終了
window.close() #ウィンドウの破棄
