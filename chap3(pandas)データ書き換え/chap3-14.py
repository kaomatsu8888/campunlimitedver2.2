import pandas as pd # pandasをインポート
import matplotlib.pyplot as plt # matplotlib.pyplotをインポート
import japanize_matplotlib # 日本語化matplotlib

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# グラフを表示する
df.plot()
plt.show() # グラフを表示
