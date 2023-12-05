import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 表データの情報を表示
print("データの件数 =",len(df)) # データの件数を表示
print("項目名 =",df.columns.values) # 項目名を表示
print("インデックス =",df.index.values) # インデックスを表示
