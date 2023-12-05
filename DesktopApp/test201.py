import PySimpleGUI as sg #pysimpleguiのインポート

layout = [[sg.Input("フタバ")], #入力欄の作成
        [sg.Button("実行")], #ボタンの作成 
        [sg.Text("こんにちは")]] #テキストの作成
window = sg.Window("テスト", layout) #ウィンドウの作成

event, values = window.read() #イベントの読み取り
window.close() #ウィンドウの破棄


