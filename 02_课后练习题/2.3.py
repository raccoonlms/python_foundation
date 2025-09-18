# 1. break 关键字
# 1. 使用 for 循环遍历1到20的整数，当遇到数字10时使用 break 关键字跳出循环，并打印 “遇到 10，跳出循环”。
for i in range(1, 21):
    if i == 10:
        break
    print(i)
print("遇到 10，跳出循环")
# 2. continue 关键字
# 1. 给定列表 numbers = [3, 7, 2, 8, 5, 10] ，使用 for 循环和 continue 关键字，跳过列表中大于 6 的数字，打印剩下的数字。
numbers = [3, 7, 2, 8, 5, 10]
for i in numbers:
    if i > 6:
        continue
    print(i)
