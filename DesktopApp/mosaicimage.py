import PySimpleGUI as sg # pysimpleguiのインポート
from PIL import Image # Imageクラスのインポート
import io # ioモジュールのインポート
sg.theme("Darkbrown3") # テーマの設定

layout = [[sg.B("ファイルを開く", k="btn1"), sg.T(k="txt")], # ボタンコンポーネントの追加
        [sg.B("ファイルを保存", k="btn2")], 
        [sg.Image(k="img")]] # ボタンコンポーネントの追加
win = sg.Window("モノクロ画像へ変換", layout, size=(320,400)) # Windowの生成

def loadimage(): # ボタンが押されたときの処理
    global img
    loadname = sg.popup_get_file("画像ファイルを選択してください") # ファイルを選択する
    if not loadname: # ファイルを選択しなかったとき
        return
    try: # 画像ファイルを読み込む
        img = Image.open(loadname) # 画像ファイルを読み込む
        w = img.width # 画像の幅を取得
        h = img.height # 画像の高さを取得
        mw = 200 # 幅の最大値を設定
        mh = int(h * mw / w) # 高さを計算
        img = img.resize((mw, mh)). resize((w, h),resample= 0) # 画像サイズを変更
        img2 = img.copy() # 画像をコピー
        img2.thumbnail((300, 300)) # 画像サイズを変更
        bio = io.BytesIO() # バイナリストリームを作成
        img2.save(bio, format="PNG") # バイナリストリームに画像を保存
        win["img"].update(data=bio.getvalue()) # 画像を表示
        win["txt"].update(loadname) # ラベルの文字列を変更
    except: # 画像ファイルを読み込めなかったとき
        win["img"].update() # 画像を表示
        win["txt"].update("失敗しました") # ラベルの文字列を変更
img = None # 画像を初期化
def saveimage(): # ボタンが押されたときの処理
        if img == None: # 画像が読み込まれていないとき
            return # 何もしない
        savename = sg.popup_get_file("png画像名をつけて保存してください", save_as=True) # ファイルを保存する
        if not savename: # ファイルを選択しなかったとき
            sg.PopupTimed("ファイル名を入力してください",) # ファイルを保存する
            return # 何もしない
        if savename.endswith(".png") == False:  # 拡張子がないとき
            savename = savename + ".png" # 拡張子を追加
            try: # 画像ファイルを保存する
                img.save(savename) # 画像ファイルを保存する
                win["txt"].update(f"{savename}を保存しました。") # ラベルの文字列を変更
            except: # 画像ファイルを保存できなかったとき
                win["txt"].update("失敗しました")


while True: # イベントループ
    event, values = win.read() # イベントの読み取り
    if event == "btn1": # ボタンが押されたときの処理
        loadimage() # loadimage()関数の呼び出し
    if event == "btn2": # ボタンが押されたときの処理
        saveimage()
    if event == None: # ウィンドウ閉じるイベントの検出
        break
win.close() # ウィンドウを閉じる

