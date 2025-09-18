# =赋值运算符串
name = "小王"
# 同时给多个变量赋值
Name, age, height = "小王", 18, 1.75
print(name, age, height)
# 同时给多个变量赋相同的值
name = age = height = "小王"

# +=
# a保存a+b的结果
a = 10
b = 20
# a = a + b
a += b
a /= b

# 关系运算符 > < >= <= == !=
# 关系运算结果一定是bool类型
num1 = 10
num2 = 20
print(num1 > num2)  # False

# 案例:判断是否是偶数的条件表达式
num = 11
print(f"偶数的条件表达式为:{num % 2 == 0}")
print(f"奇数的条件表达式为:{num % 2 != 0}")

# 逻辑运算符 and or not
# and : 逻辑与,多个条件同时满足是True
# or : 逻辑或,多个条件满足一个True
# not : 逻辑非,结果取反
# 逻辑运算符的结果一定是bool类型，用于处理多个条件是否满足
# 案例：输入变量判断是否是偶数且大于10
a = int(input("请输入数字:"))
print(f"{a}是偶数且大于10的结果为:{a % 2 == 0 and a > 10}")
# 案例：变量是否是小于15或者是一个奇数
a = int(input("请输入数字:"))
print(f"{a}小于15或者是一个奇数的结果为:{a < 15 or a % 2 != 0}")
# 案例：判断姓名不是‘ljj’
name1 = input("请输入姓名:")
# print(f"{name1}不是ljj的结果为:{name1 != 'ljj'}")
print(f"{name1}不是ljj的结果为:{not name1 == 'ljj'}")
