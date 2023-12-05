import PySimpleGUI as sg

loadname = sg.popup_get_file("ファイルを選択してください")
print(loadname)
