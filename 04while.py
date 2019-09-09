'''
while循环语句练习
'''

# a = 1# 设置变量
# while a != 0:#设置玄幻条件
#     print('please input:')#满足条件后输出该语句
#     a = int(input ())#接收输入的结果
# print('over!')#不满足时输出

num = 10
print('Guess what I think?')
bingo = False  # 设置变量bingo值为False

while bingo == False:  # 当bingo值为False时执行循环体
    answer = int(input())
    if answer > num:
        print('too big!')
    elif answer < num:
        print('too small')
    else:
        print('BINGO!')
        bingo = True  # 回答正确时改变bingo的值,结束循环
