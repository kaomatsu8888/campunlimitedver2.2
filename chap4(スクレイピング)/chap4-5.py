import pandas as pd # pandasをインポート
import matplotlib.pyplot as plt # matplotlib.pyplotをインポート
import japanize_matplotlib # 日本語化matplotlib

# データフレームを読み込む
df = pd.read_csv("FEH_00200524_231202091454.csv", index_col="全国・都道府県", encoding="shift_jis")

# 2022年の列データで棒グラフを表示する
df["2022年"] = pd.to_numeric(df["2022年"].str.replace(",", "")) # 2022年の列データを数値に変換
print(df["2022年"])
df["2022年"].plot.bar() # 2022年の棒グラフを表示
plt.show() # グラフを表示


