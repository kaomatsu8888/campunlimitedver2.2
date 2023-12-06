# じゃんけんアプリ
import random
hand = ["グー", "チョキ", "パー"] # 手のリスト
message = {"あなたの勝ちです。", "あなたの負けです。", "あいこです。"} # 結果の辞書
mynum = random.randint(0, 2) # 自分の手をランダムに選択
comum = random.randint(0, 2) # コンピュータの手をランダムに選択
print(f"あなたの手は{hand[mynum]}です。わたしの手は{hand[comum]}です。") # 手を表示
hantei = (comum - mynum) % 3 # 勝敗の判定
print(f"勝敗判定: {message[hantei]}です。")
print(f"勝敗判定: {message[hantei]}") # 勝敗の結果を表示
