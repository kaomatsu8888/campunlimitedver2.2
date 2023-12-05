import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# ソート(国語の点数が高い順に並び替え)
kokugo = df.sort_values("国語" ,ascending=False) # 国語の列を降順にソート

# CSVファイルに出力する
kokugo.to_csv("export1.csv",) # CSVファイルに出力
