# def 函数名(参数):
#   函数体
#   return 函数返回值

# 定义函数
def say_hello():
    print("hello world")


# 调用函数
say_hello()


# 带参数的函数
def add(a, b):
    print(f"a+b={a + b}")


add(1, 2)


# 带返回值的函数
def add1(a, b):
    return a + b


result = add1(1, 2)
print(result)


#
def info(name, age, sex, address):
    """
    :param name:
    :param age:
    :param sex:
    :param address:
    :return:
    """
    print(f"name={name},age={age},sex={sex},address={address}")


info("张三", 18, "男", "上海")


def intro(name, age):
    print(f"name={name},age={age}")


intro("张三", 18)
# 关键字参数
intro(name="张三", age=18)


# 默认参数
def greet(name, greeting="你好"):
    print(f"{greeting}, {name}")


greet("张三")
greet("张三", "hello")


# 不定长参数
# *args    **kwargs
def sum(*args):  # args 是一个元组
    total = 0
    for i in args:
        total += i
    return total


def sum1(**kwargs):  # kwargs 是一个字典
    return kwargs


print(sum(1, 2, 3, 4, 5))
print(sum1(a=1, b=2, c=3))


# 返回多个
def people(name, age):
    return name, age


people("张三", 18)


# 结束函数
def end(a):
    if a < 0:
        return False  # 结束函数

# 函数的作用域
# 全局变量：定义在函数之外
# 局部变量：定义在函数内部
# 函数内可以访问全局变量
# 函数外不能访问局部变量
# 局部变量：在函数内部定义，仅在函数内部有效。
# 全局变量：在函数外部定义，整个程序中有效（函数内部可访问，修改需用lobal 声明）
