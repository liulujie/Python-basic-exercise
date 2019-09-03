'''
利用if语句实现猜数字的小游戏..
'''
num = 10
print('Guess one number?')
answer = int(input())
if answer > 10:
    print('too big!')

if answer < 10:
    print('too small!')

if answer == num:
    print('BINGO!')
