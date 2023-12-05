import datetime

now = datetime.datetime.now() # 現在の日時を取得
print(f"現在 = {now:%m/%d %H:%M:%S}") # 時刻を表示
goal = now.replace(hour=20, minute=30, second=0) # 20時30分に設定
print(f"目標 = {goal:%m/%d %H:%M:%S}") # 時刻を表示
td = goal - now # 経過時間を計算
print(td) # 経過時間を表示
