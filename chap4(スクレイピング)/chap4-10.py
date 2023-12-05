import pandas as pd

# データフレームを読み込む
df1 = pd.read_csv("Sample_20190619102739.csv", index_col="時点")
df2 = pd.read_csv("Sample_20190619102836.csv", index_col="時点")
df3 = pd.read_csv("Sample_20190619102904.csv", index_col="時点")

print(df1.columns.values) # 列名を表示
print(df2.columns.values) # 列名を表示
print(df3.columns.values) # 列名を表示

