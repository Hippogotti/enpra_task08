import random #ランダム関数用
import sys #キーボード入力・プログラム終了用
import math #ガウス記号使う用

#ランダムに正解の数字を決定
i = random.randint(1, 9)
j = random.randint(0, 9)
k = random.randint(0, 9)

#正解の3桁の整数の決定
collect_num = 100 * i + 10 * j + k 

#正解の3桁が表示されるかを確認
print(collect_num)

#tuple型に文字列を変換
def tuple_num(num) : 
    return math.floor(num / 100), math.floor(num % 100 / 10), math.floor(num % 10)

#入力した数字と正解の整合を確認する関数
def TrueFalse_func(num) : 
    #正解のとき
    if collect_num == num:
        print("Your answer is true. CONGRATULATIONS !")
        sys.exit()
    #不正解のとき
    else:
        print("Your answer is false.")