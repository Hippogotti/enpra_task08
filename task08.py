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
        #HINT1を与える条件分岐
        if (i in tuple_num(num)) and (j in tuple_num(num)) and (k in tuple_num(num)) :
            print("HINT 1 : Three numbers are true.")
        elif ((i in tuple_num(num)) and (j in tuple_num(num))) or ((j in tuple_num(num)) and (k in tuple_num(num))) or ((k in tuple_num(num)) and (i in tuple_num(num))) :
            print("HINT 1 : Two numbers are true.")
        elif (i in tuple_num(num)) or (j in tuple_num(num)) or (k in tuple_num(num)) :
            print("HINT 1 : One number is true.")
        else :
            print("Each number is uncollect.")        
        #HINT2を与える条件分岐
        if (tuple_num(num)[0] == i and tuple_num(num)[1] == j) or (tuple_num(num)[1] == j and tuple_num(num)[2] == k) or (tuple_num(num)[2] == k and tuple_num(num)[0] == i) :
            print("HINT 2 : Two numbers' position are true.")
        elif tuple_num(num)[0] == i or tuple_num(num)[1] == j or tuple_num(num)[2] == k :
            print("HINT 2 : One number's position is true.")
        else :
            print("Each number's position is uncollect.")