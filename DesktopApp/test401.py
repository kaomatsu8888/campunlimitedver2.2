import datetime # datetimeモジュールをインポート

now = datetime.datetime.now() # 現在の日時を取得
print(f"{now:%H時%M分%S秒}") # 時刻を表示
print(f"{now:%H:%M:%S}") # 時刻を表示
print(f"{now:%p %I:%M:%S}") # 時刻を表示
print(f"{now:%Y/%m/%d(%a)}") # 日付を表示
