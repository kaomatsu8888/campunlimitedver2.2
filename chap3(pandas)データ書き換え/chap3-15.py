import pandas as pd # pandasをインポート
import matplotlib.pyplot as plt # matplotlib.pyplotをインポート
import japanize_matplotlib # 日本語化matplotlib

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 棒グラフを表示する
df.plot.bar() # 棒グラフを表示
plt.legend(loc="lower right") # 凡例を表示
plt.show() # グラフを表示

# 棒グラフ(水平)を表示する
df.plot.barh() # 棒グラフ(水平)を表示
plt.legend(loc="lower right") # 凡例を表示
plt.show() # グラフを表示

# 積み上げ棒グラフを表示する
df.plot.bar(stacked=True) # 積み上げ棒グラフを表示
plt.legend(loc="lower right") # 凡例を表示
plt.show() # グラフを表示

# 箱ひげグラフを表示する
df.plot.box() # 箱ひげグラフを表示
plt.show() # グラフを表示

# 面グラフを表示する
df.plot.area() # 面グラフを表示
plt.legend(loc="lower right") # 凡例を表示
plt.show() # グラフを表示
