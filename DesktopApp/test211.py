import PySimpleGUI as sg

sg.theme("Darkbrown3")

layout = [
    [sg.T("テキスト")],
    [sg.I("入力欄")],
    [sg.ML("複数行テキスト 1行目\n2行目", size=(20, 2))],
    [sg.Im("futaba.png")]
]

# Window の作成。ここで font と size を指定
win = sg.Window("テスト", layout, font=(None, 14), size=(300,240))

event, values = win.read()
win.close()
