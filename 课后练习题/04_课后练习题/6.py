# 六、函数的嵌套调用
# 1. 定义函数func1 ，功能是打印 “这是函数 1”，然后定义func2 ，在func2 内部调用函数
# func1 ，然后再打印 “这是函数 2”。调用func2 ，查看运行结果。
def func1():
    print("这是函数 1")
def func2():
    func1()
    print("这是函数 2")
func2()

# 2. 定义函数calculate_square ，接收一个参数num ，返回num 的平方；
# 再定义函数calculate_cube ，接收一个参数num ，在函数内部调用calculate_square 函数，传入num ，
# 然后将结果乘以num ，返回立方体的体积。调用calculate_cube 函数，传入 3，打印返回结果。
def calculate_square(num):
    return num ** 2
def calculate_cube(num):
    square = calculate_square(num)
    return square * num
print(calculate_cube(3))
# 3. 定义函数get_total ，接收两个参数a和b，返回a + b；再定义函数get_average ，接收
# 两个参数x和y，在函数内部调用 get_total 函数，传入x和y，然后将结果除以 2，返回平均值。
# 调用 get_average 函数，传入 4 和 6，打印返回结果。
def get_total(a, b):
    return a + b
def get_average(x, y):
    total = get_total(x, y)
    return total / 2
print(get_average(4, 6))
