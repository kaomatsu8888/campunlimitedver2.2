import pandas as pd # pandasをインポート
import matplotlib.pyplot as plt # matplotlib.pyplotをインポート
import japanize_matplotlib # 日本語化matplotlib

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 国語の棒グラフを表示する
df["国語"].plot.barh() # 国語の棒グラフを表示
plt.legend(loc="lower right") # 凡例を表示
plt.show() # グラフを表示

# 国語と数学の棒グラフを表示する
df[["国語", "数学"]].plot.barh() # 国語と数学の棒グラフを表示
plt.legend(loc="lower right") # 凡例を表示
plt.show() # グラフを表示

# C子の棒グラフを表示する
df.loc["C子"].plot.barh() # C子の棒グラフを表示
plt.legend(loc="lower right") # 凡例を表示
plt.show() # グラフを表示

# 箱ひげグラフを表示する
df.plot.box() # 箱ひげグラフを表示
plt.show() # グラフを表示

# 面グラフを表示する
df.plot.area() # 面グラフを表示
plt.legend(loc="lower right") # 凡例を表示
plt.show() # グラフを表示
