import pandas as pd # pandasをインポート

# データフレームを読み込む
df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis")
print(len(df)) # データの個数を表示
print(df.columns.values) # 列名を表示
