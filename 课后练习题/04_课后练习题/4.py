# 四、函数的返回值
# 1. 修改 add 函数（之前定义的两数相加函数），使其返回a + b的结果，而不是打印，然后调用该函数，
# 传入 2 和 7，将返回结果赋值给变量result ，并打印result 。
def add(a, b):
    return a + b
result = add(2, 7)
print(result)
# 2. 定义一个函数is_even ，接收一个整数参数 num ，如果num 是偶数，返回True ，否则返回False 。
# 调用该函数，传入 10 和 11，分别打印返回结果。
def is_even(num):
    if num % 2 == 0:
        return True
    return False
print(is_even(10))
print(is_even(11))
# 3. 定义函数et_max ，接收两个参数x和y，返回其中较大的数。调用该函数，传入 5 和 8，打印
# 返回结果。
def get_max(x, y):
    if x > y:
        return x
    return y
print(get_max(5, 8))