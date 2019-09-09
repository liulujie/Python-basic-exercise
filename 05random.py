'''
导入random随机数模块,随机猜数
'''
from random import randint

num = randint(1, 20)  # randint方法左右为闭区间
bingo = False
while bingo == False:
    print('Guess what I think ?')
    answer = int(input())  # 将input强制转换为int型(input接收的值均为字符串)
    if answer > num:
        print('too big!')
    elif answer < num:
        print('too samll!')
    else:
        print('BINGO!')
        bingo = True
