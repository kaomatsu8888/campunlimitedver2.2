import PySimpleGUI as sg # pysimpleguiのインポート
import io # ioモジュールのインポート
import qrcode # qrcodeモジュールのインポート
sg.theme("Darkbrown3") # テーマの設定

layout = [ 
    [sg.T("URL:"), sg.I(k="in1")], # テキストコンポーネントの追加
    [sg.B("QRコードを作成", k="btn1")], # ボタンコンポーネントの追加
    [sg.B("ファイルを保存", k="btn2"), sg.T(k="txt")], # ボタンコンポーネントの追加
    [sg.Im(k="img")]]# 画像コンポーネントの追加
win = sg.Window("QRコード作成アプリ", layout, size=(320, 420)) # Windowの生成
img = None # 画像を初期化

def execute(): # ボタンが押されたときの処理
    global img # imgをグローバル変数として扱う
    if not values["in1"]: # URLが入力されていないとき
        sg.PopupTimed("URLを入力してください") # ポップアップを表示
        return # 何もしない
    img = qrcode.make(values["in1"]) # QRコードを作成
    img.thumbnail((300, 300)) # 画像サイズを変更
    bio = io.BytesIO() # バイナリストリームを作成
    img.save(bio, format="PNG") # バイナリストリームに画像を保存
    win["img"].update(data=bio.getvalue()) # 画像を表示

def saveimage(): # ボタンが押されたときの処理
    if img == None:
        return
    savename = sg.popup_get_file("png画像名をつけて保存してください", save_as=True) # ファイルを保存する
    if not savename: # ファイルを選択しなかったとき
        sg.PopupTimed("ファイル名を入力してください",) # ファイルを保存する
        return # 何もしない
    if savename.endswith(".png") == False:  # 拡張子がないとき
        savename = savename + ".png"
        try: # 画像ファイルを保存する
            img.save(savename) # 画像ファイルを保存する
            win["txt"].update(f"{savename}を保存しました。") # ラベルの文字列を変更
        except:
            win["txt"].update("失敗しました")

while True: # イベントループ
    event, values = win.read() # イベントの読み取り
    if event == "btn1": # ボタンが押されたときの処理
        execute() # execute()関数の呼び出し
    if event == "btn2": # ボタンが押されたときの処理
        saveimage()
    if event == None: # ウィンドウ閉じるイベントの検出
        break

win.close() # ウィンドウを閉じる
