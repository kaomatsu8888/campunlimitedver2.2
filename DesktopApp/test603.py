# 足し算ゲームアプリ
import random

def question():
    global playflag, ans
    a = random.randint(0,100)
    b = random.randint(0,100)
    ans = a + b
    print(f"問題: {a} + {b} = ?")
    playflag = True

def anscheck():
    global playflag
    if indate.isdecimal() == True:
        mynum = int(indate)
        if mynum == ans:
            print("正解です。")
            playflag = False
        else:
            print(f"{mynum}は不正解です。")

question()
while True:
    indate = input("答えを入力してください。")
    if playflag == False:
        question()
    else:
        anscheck()


        
