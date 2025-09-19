# 三、函数的参数
# 1. 定义一个函数 add ，接收两个位置参数a和b，功能是返回
# a + b的结果，然后调用该函数，传入 3 和 5，打印返回的结果。
def add(a, b):
    return a + b

print(add(3, 5))

# 2. 定义一个函数get_full_name ，接收名字和姓氏两个位置参数，功能是返回完整的姓名（名字 +
# 姓氏），调用该函数，传入 “张” 和 “三”，打印完整姓名。
def get_full_name(first_name, last_name):
    return first_name + last_name
print(get_full_name("张", "三"))
# 3. 调用calculate_area 函数（之前定义的计算长方形面积的函数），使用关键字参数的方式传入
# 长和宽（长为 4，宽为 6），查看结果。
def calculate_area(length, width):
    return length * width
print(calculate_area(length=4, width=6))
# 4. 定义函数 show_info ，接收name 、age 、city 三个参数，功能是打印 “姓名：XXX，年龄：
# XX，城市：XXX”，然后使用关键字参数的方式调用该函数，传入自己的信息。
def show_info(name, age, city):
    print(f"姓名：{name}，年龄：{age}，城市：{city}")
show_info(name="李明树", age=21, city="武汉")
# 5. 定义一个函数greet_person ，接收name 参数，还有一个默认参数greeting ，默认值为“Hello”，
# 功能是打印greeting + ", " + name 。调用该函数，只传入name 为 “Alice”，查看结果；
# 再调用该函数，传入name 为 “Bob”，greeting 为 “Hi”，查看结果。
def greet_person(name, greeting="Hello"):
    print(greeting + ", " + name)
greet_person(name="Alice")
greet_person(name="Bob", greeting="Hi")
# 6. 定义函数calculate_discount ，接收商品价格price 和折扣率discount （默认值为 0.9，即9 折），
# 功能是返回折扣后的价格（price * discount ）。调用该函数，传入价格为 100，查看折扣后价格；
# 再调用该函数，传入价格为 200，折扣率为 0.8，查看结果。
def calculate_discount(price, discount=0.9):
    return price * discount
print(calculate_discount(price=100))
print(calculate_discount(price=200, discount=0.8))
# 7. 定义一个函数sum_numbers ，接收不定长的位置参数，功能是返回所有参数的和。调用该函数
# 传入 1、2、3，查看结果；再传入 1、2、3、4、5，查看结果。
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 2, 3, 4, 5))
# 8. 定义一个函数print_kwargs ，接收不定长的关键字参数，功能是打印所有关键字参数的键和
# 值。调用该函数，传入a=1 ， b=2 ， c=3 ，查看打印结果。
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1, b=2, c=3)