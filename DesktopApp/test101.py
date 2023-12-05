import tkinter as tk

def execute(): # ボタンが押されたときの処理
    txt = "こんにちは" # ラベルに表示する文字列
    lbl.configure(text=txt) # ラベルの文字列を変更

root = tk.Tk() # メインウィンドウ
root.title("こんにちはテスト") # メインウィンドウのタイトル
root.geometry("200x100") # メインウィンドウのサイズ

lbl = tk.Label(text="") # ラベル
btn = tk.Button(text="実行", command=execute) # ボタン

lbl.pack() # ラベルを配置
btn.pack() # ボタンを配置
tk.mainloop() # メインループ
