# 七、综合案例
# 1. 编写一个程序，包含以下函数：
# get_input ：用于获取用户输入的两个整数，返回这两个整数。
# calculate ：接收两个整数参数，计算并返回它们的和、差、积（三个结果，可将结果放在一个元组中返回）。
# print_results ：接收和、差、积三个结果，打印 “和：XX，差：XX，积：XX”。然后在主程序中，调用
# get_input 获取两个数，调用calculate 计算结果，再调用print_results 打印结果。
def get_input():
    num1 = int(input("请输入第一个整数："))
    num2 = int(input("请输入第二个整数："))
    return num1, num2
def calculate(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    return sum, difference, product
def print_results(sum, difference, product):
    print("和：{}，差：{}，积：{}".format(sum, difference, product))

in_put = get_input()
cal1 = calculate(in_put[0], in_put[1])
print_results(cal1[0], cal1[1], cal1[2])
# 2. 编写一个函数is_prime ，判断一个数是否为质数（只能被 1 和自身整除的大于 1 的整数），然
# 后编写主程序，提示用户输入一个数，调用is_prime 函数判断该数是否为质数，并打印判断结果
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
num = int(input("请输入一个数："))
if is_prime(num):
    print("{}是质数".format(num))
else:
    print("{}不是质数".format(num))
