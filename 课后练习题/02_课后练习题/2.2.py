# 1. 使用while循环打印输出10~100之间所有能同时被5和9整除的整数。
i = 10
while i <= 100:
    if i % 5 == 0 and i % 9 == 0:
        print(i)
    i += 1
# 2. 提示用户输入一个整数，使用 while 循环，从该整数开始倒序打印到 1。例如输入 5，打印 5、4、 3、2、1。
num = int(input("请输入一个整数："))
while num > 0:
    print(num)
    num -= 1
# 3. 计算用户输入的一个整数的阶乘（n! = n × (n - 1) ×...× 1），使用 while 循环实现。
num = int(input("请输入一个整数："))
a, b = 1, 1
while num > a:
    b = a * num
    a += 1
print(b)
