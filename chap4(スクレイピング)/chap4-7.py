import pandas as pd # pandasをインポート
import matplotlib.pyplot as plt # matplotlibをインポート
import japanize_matplotlib # 日本語化matplotlib

# データフレームを読み込む
df = pd.read_csv("FEH_00200524_231202091454.csv", index_col="全国・都道府県", encoding="shift_jis")

# 2022年の列データで棒グラフを表示する
df = df.drop("全国", axis=0) # 全国の行を削除
df["2022年"] = pd.to_numeric(df["2022年"].str.replace(",", "")) # 2022年の列データを数値に変換
df["2022年"].plot.bar(figsize=(10, 6)) # 2022年の棒グラフを表示
plt.show() # グラフを表示
