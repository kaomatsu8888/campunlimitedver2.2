import pandas as pd # pandasをインポート

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# ソート(並べ換え)して表示
kokugo = df.sort_values("国語" ,ascending=False) # 国語の列を降順にソート
print("国語の点数が高い順\n", kokugo) # ソートしたデータを表示
