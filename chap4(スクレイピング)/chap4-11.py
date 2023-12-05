import pandas as pd # pandasをインポート
import matplotlib.pyplot as plt # matplotlibをインポート
import japanize_matplotlib # 日本語化matplotlib

# データフレームを読み込む
df1 = pd.read_csv("Preview_20231202100520.csv", header=1, skiprows=0,  index_col="時点")
df2 = pd.read_csv("Preview_20231202100542.csv", header=1, skiprows=0, index_col="時点")
df3 = pd.read_csv("Preview_20231202100554.csv", header=1, skiprows=0, index_col="時点")

print(df1.columns.values) # 列名を表示
print(df2.columns.values) # 列名を表示
print(df3.columns.values) # 列名を表示
