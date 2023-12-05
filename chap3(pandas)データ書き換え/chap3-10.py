import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 行と列を入れ替えて表示
print("行と列を入れ替えて表示\n", df.T)

# データをリスト化する
print("Pythonのリストデータ化\n", df.values)
