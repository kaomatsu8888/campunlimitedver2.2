import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 1列のデータを取り出す
print("C子のデータ\n", df.loc[2]) # C子のデータを表示

# 複数列のデータを取り出す
print("C子とD郎のデータ\n", df.loc[[2, 3]]) # C子とD郎のデータを表示

# 指定した行の指定した列のデータを取り出す
print("C子の国語のデータ\n", df.loc[2]["国語"]) # C子の国語のデータを表示
