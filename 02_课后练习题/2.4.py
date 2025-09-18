# 1. 使用嵌套的 for 循环，打印以下图案：
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()
#  2. 使用嵌套的 for 循环，打印以下图案：
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end=" ")
            continue
        print(" ", end=" ")
    print()
#  3. 在马克思手稿中有一道趣味的数学问题：一共有30个人，可能包括男人，女人和小孩。他们在一
# 家饭馆吃饭共花了50先令，其中每个男人花3先令，每个女人花2先令，每个小孩花1先令。请问男
# 人、女人和小孩各几人？请编写一个程序来计算。
for man in range(0, 30):
    for woman in range(0, 30):
        for child in range(0, 30):
            if man + woman + child == 30 and man * 3 + woman * 2 + child == 50:
                print(f"男人{man},女人{woman},孩子{child}")
