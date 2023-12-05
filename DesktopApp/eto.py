import PySimpleGUI as sg # pysimpleguiのインポート
sg.theme("Darkbrown3") # テーマの設定

layout = [[sg.T("指定された年の干支を調べます")], # テキストコンポーネントの追加
            [sg.T("西暦何年ですか？"), sg.I("2020", k="in1")], # キーワード引数 k の設定
            [sg.B("実行", k="btn"), sg.T(k="txt")]] # Text コンポーネントの初期テキスト

win = sg.Window("干支調べアプリ", layout, font=("none, 14"), size=(300, 150)) # Windowサイズの設定

def execute(): # ボタンが押されたときの処理
    eto = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"] # 干支を格納するリスト
    in1 = int(values["in1"]) # 年を入力
    etonum = (in1 - 4) % 12 # 干支のインデックスを計算
    txt = f"{in1}年は{eto[etonum]}年です" # ラベルに表示する文字列
    win["txt"].update(txt) # ラベルの文字列を変更

while True: # イベントループ
    event, values = win.read() # イベントの読み取り
    if event == "btn": # ボタンが押されたときの処理
        execute() # execute()関数の呼び出し
    if event == None: # ウィンドウ閉じるイベントの検出
        break # イベントループを抜ける

win.close() # ウィンドウを閉じる
