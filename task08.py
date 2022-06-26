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