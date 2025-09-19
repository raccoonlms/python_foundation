# 2. 自定义模块
# 1. 创建一个名为my_module.py 的模块，在其中定义一个函数greet(name) ，功能是打印 “Hello, name!”。
# 然后在另一个 Python 文件中导入该模块，调用greet 函数，传入自己的名字。
import my_module
my_module.greet('张三')
# 2. 在my_module.py 模块中再定义一个变量PI = 3.14159 ，然后在导入该模块的文件中，打印PI 的值。
print(my_module.PI)