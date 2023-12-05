import PySimpleGUI as sg #pysimpleguiのインポート

sg.theme("Darkbrown3")  # テーマの設定

layout = [  # レイアウトの修正
    [sg.T("身長と体重を入力してください")], # テキストコンポーネントの追加
    [sg.T("身長(cm)"), sg.I("160", k="in1")],  # キーワード引数 k の設定
    [sg.T("体重(kg)"), sg.I("50", k="in2")],   # キーワード引数 k の設定
    [sg.B("実行", k="btn"), sg.T("", k="txt")] # Text コンポーネントの初期テキスト
]

win = sg.Window("BMI計算", layout, size=(300, 240)) # Windowサイズの設定


def execute(): # ボタンが押されたときの処理
    in1 = float(values["in1"]) / 100.0 # 身長を m に変換
    in2 = float(values["in2"]) # 体重を kg に変換
    bmi = in2 / (in1 * in1) # BMIの計算
    txt = f"BMIは{bmi:.2f}です" # ラベルに表示する文字列
    win["txt"].update(txt) # ラベルの文字列を変更

while True: # イベントループ
    event, values = win.read()  # イベントの読み取り
    if event == "btn": # ボタンが押されたときの処理
        execute() # execute()関数の呼び出し
    if event == sg.WIN_CLOSED:  # ウィンドウ閉じるイベントの検出
        break # イベントループを抜ける

win.close() # ウィンドウを閉じる
