import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 1列のデータを取り出す
print("国語の列データ\n", df["国語"]) # 国語の列データを表示

# 複数列のデータを取り出す
print("国語と数学の列データ\n", df[["国語", "数学"]]) # 国語と数学の列データを表示
