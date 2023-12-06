import PySimpleGUI as sg
import random # randomモジュールのインポート
sg.theme("Darkbrown3") # テーマの設定

layout = [[sg.T("さあ、おみくじを引こう")], # ラベルコンポーネントの追加
        [sg.Im("futaba.png")], # 画像コンポーネントの追加
        [sg.T(k="txt")], # ラベルコンポーネントの追加
            [sg.B("おみくじを引く", k="btn1")]] # ボタンコンポーネントの追加
            
win = sg.Window("おみくじ", layout, font=(None, 14)) # Windowの生成

def omikuji(): # ボタンが押されたときの処理
    kuji = ["大吉", "中吉", "小吉", "末吉", "凶"] # おみくじのリスト
    kekka = random.choice(kuji) # おみくじの結果をランダムに選択
    txt = f"おみくじの結果は{kekka}です。" # ラベルの文字列を変更
    win["txt"].update(txt) # ラベルの文字列を変更

while True: # イベントループ
    event, values = win.read() # イベントの読み取り
    if event == "btn1": # ボタンが押されたときの処理
        omikuji() # omikuji()関数の呼び出し
    if event == None: # ウィンドウ閉じるイベントの検出
        break # イベントループを抜ける

win.close() # ウィンドウを閉じる


