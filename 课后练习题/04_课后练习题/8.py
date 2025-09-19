# 八、常见错误与注意事项
# 1. 找出以下代码中的错误并改正：
# def say_hello(name)
#   print("Hello, " + name)
# say_hello("Tom")
"""
def say_hello(name): 缺少冒号
"""
#  2. 找出以下代码中的错误并改正：
# def add_numbers(a, b):
#       result = a + b
# print(add_numbers(3, 4))
"""
add_numbers没有返回a+b的值，应该加上 return result
"""
#  3. 解释为什么以下代码会报错：
# def func():
#       local = 5
# print(local)
# func()
"""
local是局部变量，无法在函数外调用
"""
