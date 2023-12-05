import pandas as pd # pandasをインポート
import matplotlib.pyplot as plt # matplotlibをインポート
import japanize_matplotlib # 日本語化matplotlib

# データフレームを読み込む
df1 = pd.read_csv("Sample_20190619102739.csv", index_col="時点")

# 平均気温で折れ線グラフを表示する
df1["年平均気温【℃】"].plot() # 平均気温で折れ線グラフを表示
plt.ylim(-10,40)
plt.show() # グラフを表示
