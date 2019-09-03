'''
布尔值小练习
    设置一个默认值,将输入的值与默认值进行比较,输出三种情况(>,<,==)
time:2019/9/3
author:kk
'''
# 定义一个变量num.并赋值
num = 7
# 输出提示语
print('Guss what I think?')
# 创建一个变量接受输入的答案,并转换为整数类型,原input为字符串
answer = int(input())
# 将输入的结果与原始数据进行比较
result = answer < num
# 猜测大小
print('too small?')
# 打印出比较的结果
print(result)

result = answer > num
print('too big?')
print(result)

result = answer == num
print('equal?')
print(result)
