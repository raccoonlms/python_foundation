# 3. 包（Package）
# 1. 创建一个名为my_package 的包，在包内创建两个模块module1.py 中定义函数module1.py 和module2.py 。
# 在func1() ，打印 “Function from module1”；在module2.py 中定义函 数func2() ，
# 打印 “Function from module2”。然后在包外的 Python 文件中，分别导入这两个模块并调用对应的函数。
from my_package import module1,module2
module1.func1()
module2.func2()
# 2. 在my_package 包中创建
# __init__.py 文件，在其中定义变量version = "1.0" ，然后在导 入包的文件中，打印my_package.version 。
import my_package
print(my_package.version)
