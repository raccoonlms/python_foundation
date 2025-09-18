# for循环
# for 变量 in 序列：
# 	    循环体    依次取出序列中的元素赋值给变量，执行循环体
#     序列：列表、元组、字符串、字典、集合
import random

str = ('Python')
for i in str:
    print(i)
# 使用range(),生成数字序列
"""
range(start,end,step)
    staret:起点数字（默认为0）
    end:结束的数字（不包含）
    step:步长（默认是1）
"""
# 生成2-8的数字（不含8）
for i in range(2, 8):
    print(i)
# 生成0-100的整10的数字（不含100）
for i in range(0, 100, 10):
    print(i)

# while循环
"""
    while 条件表达式：
        循环体   #条件True执行，直到条件False时终止循环
        注意：循环体中必须包含改变条件的语句，否则会导致死循环（无限执行）。
"""
a = 0
total = 0
while a < 10:
    total += a
    a += 1
    print(a)
print(total)
"""
    break 跳出当前循环
    continue 跳过当前循环，继续下一次循环
"""
total1 = 0
for i in range(1, 10):
    total1 += i
# 猜数字基础版
random_num=random.randint(1, 10) # 1-10随机数
print(random_num)
guess_num = int(input('请输入数字：'))
count = 0
while guess_num != random_num:
    count += 1
    if guess_num > random_num:
        print('猜的数字太大了')
    else:
        print('猜的数字太小了')
    guess_num = int(input('请输入数字：'))
print(f'经过{count}次恭喜你猜对了')
