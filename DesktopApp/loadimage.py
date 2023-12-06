import PySimpleGUI as  # pysimpleguiのインポート
from PIL import Image # Imageクラスのインポート
import io # ioモジュールのインポート
sg.theme("Darkbrown3") # テーマの設定

layout = [[sg.B("ファイルを開く", k="btn1"), sg.T(k="txt")], [sg.Image(k="img")]] # ボタンコンポーネントの追加
win = sg.Window("画像ファイルの読み込み", layout, size=(320,380)) # Windowの生成

def loadimage(): # ボタンが押されたときの処理
    loadname = sg.popup_get_file("画像ファイルを選択してください") # ファイルを選択する
    if not loadname: # ファイルを選択しなかったとき
        return
    try: # 画像ファイルを読み込む
        img = Image.open(loadname) # 画像ファイルを読み込む
        img.thumbnail((300, 300)) # 画像サイズを変更
        bio = io.BytesIO() # バイナリストリームを作成
        img.save(bio, format="PNG") # バイナリストリームに画像を保存
        win["img"].update(data=bio.getvalue()) # 画像を表示
        win["txt"].update(loadname) # ラベルの文字列を変更
    except: # 画像ファイルを読み込めなかったとき
        win["img"].update() # 画像を表示
        win["txt"].update("失敗しました") # ラベルの文字列を変更

while True: # イベントループ
    event, values = win.read() # イベントの読み取り
    if event == "btn1": # ボタンが押されたときの処理
        loadimage() # loadimage()関数の呼び出し
    if event == None: # ウィンドウ閉じるイベントの検出
        break # イベントループを抜ける
win.close() # ウィンドウを閉じる

