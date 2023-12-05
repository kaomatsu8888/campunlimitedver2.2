import pandas as pd # pandasをインポート
import openpyxl # openpyxlをインポート

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# ソート (国語の点数が高いもの順に並べる)
kokugo = df.sort_values(by="国語", ascending=False)

# Excelファイルを書き出す
kokugo.to_excel("csv_to_excel.xlsx")
