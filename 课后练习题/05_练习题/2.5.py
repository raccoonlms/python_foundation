# 5. 综合案例
# 1. 创建一个模块calculator.py ，其中包含add(a, b) 、subtract(a, b) 、multiply(a,b)
# 、divide(a, b) 四个函数，分别实现两数的加、减、乘、除运算。然后创建一个主程序文件，
# 导入该模块，提示用户输入两个数和一个操作符（+、-、*、/），根据操作符调用对应的函数并打印结果。
import calculator

num = input("请输入两个数字的操作（例如1+1，2-1，4*1，4/2）：")


def a_b(num1, count):
    a1 = float(''.join(num1[:count].split()))  # 将列表转为字符串后再转换成数字
    b1 = float(''.join(num1[count + 1:].split()))
    print(f"符号的位置是：{count}")
    return a1, b1

if '+' in num:
    count = num.index('+')
    a, b = a_b(num, count)
    print(calculator.add(a, b))
elif '-' in num:
    count = num.index('-')
    a, b = a_b(num, count)
    print(calculator.subtract(a, b))
elif '*' in num:
    count = num.index('*')
    a, b = a_b(num, count)
    print(calculator.multiply(a, b))
elif '/' in num:
    count = num.index('/')
    a, b = a_b(num, count)
    print(calculator.divide(a, b))
# print(num)
# 2. 利用os模块，编写程序，遍历当前目录下的所有文件，打印每个文件的名称和大小。
import os

for root, dirs, files in os.walk(os.getcwd()):  # 获取当前目录下的所有文件和目录
    for file in files:
        # 构造完整的文件路径
        file_path = os.path.join(root, file)
        print(f"文件名：{file}，大小：{os.path.getsize(file_path)} Bytes")
