import tkinter as tk

root = tk.Tk() # ウィンドウを作成
root.geometry("400x300") # ウィンドウのサイズを設定

lbl = tk.Label(text="Label")# ラベルを作成
btn = tk.Button(text="PUSH")# ボタンを作成

lbl.pack() # ラベルを配置
btn.pack() # ボタンを配置
tk.mainloop() # ウィンドウを表示
