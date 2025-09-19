# 1. 模块的导入与使用
# 1. 导入 math 模块，使用该模块计算2的平方根，并打印结果。
import math
print(math.sqrt(2))
# 2. 导入 random 模块中的randint 函数，生成一个 1 到 10 之间的随机整数并打印。
from random import randint
print(randint(1, 10))
# 3. 使用from...import 语句导入datetime 模块中的datetime 类，获取当前日期和时间并打印。
from datetime import datetime
print(datetime.now())