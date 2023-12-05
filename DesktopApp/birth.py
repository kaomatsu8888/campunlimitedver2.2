import PySimpleGUI as sg # pysimpleguiのインポート

sg.theme("Darkbrown3")  # テーマの設定

# layout変数の定義（インデントを整理）
layout = [
    [sg.T("あなたの出生の秘密をお答えしましょう")],  # テキストコンポーネントの追加
    [sg.T("あなたは何歳？"), sg.I("18", k="in1")],  # キーワード引数 k の設定
    [sg.T("お母さんは何歳？"), sg.I("50", k="in2")],  # キーワード引数 k の設定
    [sg.B("実行", k="btn"), sg.T("", k="txt")]  # Text コンポーネントの初期テキスト
]

win = sg.Window("出生の秘密アプリ", layout, font=("none, 14"), size=(300, 240))  # Windowサイズの設定

def execute():
    in1 = int(values["in1"])  # あなたの年齢
    in2 = int(values["in2"])  # お母さんの年齢
    txt = f"あなたのお母さんは{in2 - in1}歳で出産しました"  # ラベルに表示する文字列
    win["txt"].update(txt)  # ラベルの文字列を変更

while True:  # イベントループ
    event, values = win.read()  # イベントの読み取り
    if event == "btn":
        execute()
    if event == sg.WIN_CLOSED:
        break

win.close()
