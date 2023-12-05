import datetime

start = datetime.datetime.now() # 現在の日時を取得
input("Enterを押すと終了します。") # Enterを押すと終了
now = datetime.datetime.now() # 現在の日時を取得
td = now - start # 経過時間を計算
print(td) # 経過時間を表示
