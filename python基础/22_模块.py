# 导入模块
import math

# 使用
print(math.pi)  # 圆周率
print(math.e)  # 自然数
print(f"2的3次方={math.pow(2, 3)}")
print(f"向上取整={math.ceil(2.1)}")

# 2.导入模块方式
from math import sqrt, cbrt

print(f'27的立方根={cbrt(27)}')
print(f'9的平方根={sqrt(9)}')

# 导入模块所有功能
from math import *

print(f'向下取整={floor(2.1)}')
print(f"四舍五入={round(2.1)}")

# 导入模块并取别名
import math as m

print(f'向上取整={m.ceil(2.1)}')
print(f"求和={m.fsum([1, 2, 3, 4, 5])}")

from math import fsum as summ

print(f"求和={summ([1, 2, 3, 4, 5])}")

# 自定义模块
import my_module as y
print(f"版本={y.version}")
print(f"求和{y.qiuhe(1, 2, 3, 4, 5)}")
# 导入包中的模块
import my_modules.my_module1 as m1
m1.show()
# 导入具体
from my_modules.my_module2 import show
show()

# 常用标准库模块
# random 随机数据
import random
print(random.random())  # 0-1的随机数
print(random.randint(10, 20))  # 10-20的随机数
print(random.choice([9, 28, 3, "苹果", 5]))  # 随机选择一个元素

import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"))

import os # 操作系统交互
print(f"当前路径是：",os.getcwd())
print(f"目录列表是：",os.listdir())