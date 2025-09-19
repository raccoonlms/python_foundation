# 4. 常用标准库模块
# 1. 使用os模块，获取当前工作目录并打印。
import os

print(os.getcwd())
# 2. 使用sys 模块，打印 Python 解释器的版本信息。
import sys

print(sys.version)
# 3. 编写一个函数，计算给定生日距离今天还有多少天，以及年龄。
from datetime import datetime


def birthday(birthday):
    today = datetime.today()
    birthday = datetime.strptime(birthday, '%Y-%m-%d')
    days = (today - birthday).days
    age = days // 365
    return days, age


# 4. 创建一个抽奖程序，从10个参与者中随机选择3个获奖者（不能重复）。
import random


def lucky_draw():
    participants = ['张三', '李四', '王五', '赵六', '孙七', '周八', '吴九', '郑十', '王十一', '张十二']
    winners = random.sample(participants, 3)
    return winners


# 5. 编写一个函数，生成包含大写字母、小写字母、数字和特殊字符的随机密码，长度为12位。
import random


def get_password():
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!_@'
    password = random.choices(characters, k=12)
    password = ''.join(password)  # 将列表转换为字符串
    return password

# 6. 编写一个程序，计算圆的面积、球的体积和三角形的面积。
import math
def circle_area(r):
    area = math.pi * r ** 2
    return area
def sphere_volume(r):
    volume = (4 / 3) * math.pi * r ** 3
    return volume
def triangle_area(a, b):
    area = 0.5 * a * b
    return area
