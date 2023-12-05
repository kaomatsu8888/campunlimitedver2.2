import datetime


sch = [ # スケジュールをリストに格納
    ["1時限", 8, 30],
    ["昼休み", 12, 35]
]

now = datetime.datetime.now() # 現在の日時を取得
now = now.replace(hour=10) # テストのための時間設定
print(f"現在 = {now:%H:%M:%S}") # 時刻を表示

for s in sch: # スケジュールを表示
    dt = now.replace(hour=s[1], minute=s[2], second=0) - now # 経過時間を計算
    print(f"{s[0]} = あと{dt}") # 経過時間を表示
