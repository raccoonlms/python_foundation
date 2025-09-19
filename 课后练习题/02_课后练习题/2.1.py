# 1. 打印每个水果的名称， ["apple", "banana", "orange", "grape"] ，使用 for 循环。
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(fruit)
# 2. 计算2000年1月1日到2025年1月1日相距多少天。
days = 0
for i in range(2000, 2026):
    days += 366 if i % 100 != 0 or i % 400 == 0 else 365
print(days)
# 3. 打印斐波那契数列前20项的值(1、1、2、3、5、8、13、21、34、55、89....)。
a, b = 1, 1
for i in range(20):
    print(a)
    c = a + b
    a = b
    b = c

