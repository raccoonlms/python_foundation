# 1. 定义一个函数greet ，该函数没有参数，功能是打印 “Hello, Function!”。调用greet 函数，查看
# 运行结果。
def greet():
    print("Hello, Function!")
greet()
# 2. 定义一个函数 calculate_area ，用于计算长方形的面积，需要接收长和宽两个参数，然后在函
# 数内计算并打印面积，传入长为 5，宽为 3，查看打印的面积结果。
def calculate_area(length, width):
    print("面积是：", length * width)
calculate_area(5, 3)

# 3. 定义一个函数print_info ，接收姓名和年龄两个参数，功能是打印 “姓名：XXX，年龄：XX”，
# 然后调用该函数，传入自己的姓名和年龄进行测试。
def print_info(name, age):
    print("姓名：", name, "年龄：", age)
print_info("李明树", 21)
