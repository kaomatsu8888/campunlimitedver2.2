import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 集計(最大値、最小値、平均値、中央値、合計値)として表示
print("数学の最大値", df["数学"].max()) # 数学の最大値を表示
print("数学の最小値", df["数学"].min()) # 数学の最小値を表示
print("数学の平均値", df["数学"].mean()) # 数学の平均値を表示
print("数学の中央値", df["数学"].median()) # 数学の中央値を表示
print("数学の合計値", df["数学"].sum()) # 数学の合計値を表示

