import pandas as pd

# データフレームを読み込む
df = pd.read_csv("FEH_00200524_231202091454.csv", index_col="全国・都道府県", encoding="shift_jis")
print(len(df)) # データの個数を表示
print(df.columns.values) # 列名を表示
