# 创建一个模块calculator.py ，其中包含add(a, b) 、subtract(a, b) 、multiply(a,b)
# # 、divide(a, b) 四个函数，分别实现两数的加、减、乘、除运算
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return '除数不能为0'
    return a / b
