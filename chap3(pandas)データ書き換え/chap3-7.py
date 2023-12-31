import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 条件に合うデータを抽出する
data_s = df[df["国語"] >= 90] # 国語が90点以上のデータを抽出
print("国語が90点以上\n", data_s) # 抽出したデータを表示

data_c = df[df["数学"] < 70] # 数学が70点未満のデータを抽出
print("数学が70点未満\n", data_c) # 抽出したデータを表示
