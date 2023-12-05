import PySimpleGUI as sg

sg.theme("BrightColors") # テーマの設定

layout = [
    [sg.I("フタバ", k="txt")], # Inputの省略形
    [sg.B("実行", k="btn")], # Buttonの省略形
    [sg.T("", k="txt")] # Textの省略形
]

# ウィンドウの作成（fontとsizeの設定はWindowの引数に含める）
window = sg.Window("あいさつテスト", layout, font=(None, 20), size=(250,120))

def execute(): # ボタンが押されたときの処理
    txt = "こんにちは、" + values["txt"] + "さん" # ラベルに表示する文字列
    window["txt"].update(txt) # ラベルの文字列を変更

while True: # 無限ループ
    event, values = window.read() # イベントの読み取り
    if event == "btn": # ボタンが押されたとき
        execute() # execute()の実行
    if event == sg.WIN_CLOSED: # ウィンドウが閉じられたとき
        break # 無限ループの終了

window.close() # ウィンドウの破棄
