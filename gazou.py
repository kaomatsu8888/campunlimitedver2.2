import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def disp_photo(path):
    #画像を読み込む
    newImage = PIL.Image.open(path).resize((300,300))
    #読み込んだ画像をラベルに表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData

def open_file():
    fpath = fd.askopenfilename()
    if fpath:
        disp_photo(fpath)

#ウィンドウを作成
root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="開く", command=open_file)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
