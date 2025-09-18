# 5行5个*
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

for i in range(5):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()
# 打印乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}", end="\t")
    print()
# 练习4：今有鸡兔同笼，上有35个头，下有94足，问鸡兔各几只？
a = int(input("请输入头："))
b = int(input("请输入足："))
for i in range(a+1):
    for j in range(a+1):
        if i + j == a and 2 * i + 4 * j == b:
            print(f"鸡有{i}只，兔子有{j}只")
for i in range(a+1):
    if i * 2 + (a-i) * 4 == b:
        print(f"鸡有{i}只，兔子有{a-i}只")
