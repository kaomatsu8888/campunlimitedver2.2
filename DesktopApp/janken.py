# じゃんけんアプリ
import PySimpleGUI as sg # pysimpleguiのインポート
import random # randomモジュールのインポート
sg.theme("Darkbrown3") # テーマの設定

layout = [[sg.T("ワタシとじゃんけんしよう")], # ラベルコンポーネントの追加
    # [sg.Im("futaba0.png", k="img1"), sg.Im("img2")], # 画像コンポーネントの追加
    [sg.Im("futaba0.png", k="img1"), sg.Im(k="img2")], # 画像コンポーネントの追加
    [sg.T(k="txt")], # ラベルコンポーネントの追加
    [sg.B("グー", k="btn0"), 
        sg.B("チョキ", k="btn1"),
        sg.B("パー", k="btn2")]] # ボタンコンポーネントの追加
win = sg.Window("じゃんけんアプリ", layout, font=(None, 14)) # Windowの生成

# handimg = ["h0.png, h1.png, h2.png"] # 間違い残しておく
handimg = ["h0.png", "h1.png", "h2.png"] # じゃんけんの手の画像のリスト
message = ["あいこ", "あなたの勝ち", "ワタシの勝ち"] # じゃんけんの結果のリスト
faceimg = ["futaba0.png", "futaba1.png", "futaba2.png"] # じゃんけんの顔の画像のリスト

def janken(mynum): # ボタンが押されたときの処理
    comnum = random.randint(0, 2) # コンピュータの手をランダムに選択
    win["img2"].update(handimg[comnum]) # コンピュータの手の画像を表示
    hantei = (comnum - mynum) % 3 # 勝敗を判定
    win["txt"].update(message[hantei] + "でーす ") # ラベルの文字列を変更
    win["img1"].update(faceimg[hantei]) # 顔の画像を表示

while True: # イベントループ
    event, values = win.read() # イベントの読み取り
    if event == "btn0": # ボタンが押されたときの処理
        janken(0) # janken()関数の呼び出し
    if event == "btn1": # ボタンが押されたときの処理
        janken(1) # janken()関数の呼び出し
    if event == "btn2": # ボタンが押されたときの処理
        janken(2) # janken()関数の呼び出し
    if event == None: # ウィンドウ閉じるイベントの検出
        break # イベントループを抜ける
    
win.close() # ウィンドウを閉じる
