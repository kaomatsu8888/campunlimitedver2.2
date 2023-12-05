import PySimpleGUI as sg # pysimpleguiのインポート

savename = sg.popup_get_file("名前をつけて保存してください" , default_path = "test.txt" , save_as = True) # ファイル名の指定
print(savename) # ファイル名の表示
