import PySimpleGUI as sg # pysimpleguiのインポート
import io # ioモジュールのインポート
import qrcode # qrcodeモジュールのインポート
sg.theme("Darkbrown3") # テーマの設定

layout =  [[sg.T("URL:"), sg.I(k="in1")], # テキストコンポーネントの追加
            [sg.B("QRコードを作成", k="btn1")], # ボタンコンポーネントの追加
            [sg.B("ファイルを保存", k="btn2")], sg.T(k="txt")], # ボタンコンポーネントの追加
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
bio 
