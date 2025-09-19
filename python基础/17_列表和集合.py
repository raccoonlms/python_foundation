# 列表（List）
# 列表是有序、可变的元素集合，，允许存储重复值，元素类型可混合（整数、字符串、列表等）。
# 列表的创建
list1 = [1, 2, 3, 4, 5]
print(list1)
list2 = ['hello', 1, 2.0, True]
print(list2)
list3 = list(range(1, 6))
print(list3)

# 列表的访问与切片
fruits = ['apple', 'banana', 'orange', 'pear', 'peach']
# 访问列表元素
print(fruits[0])  # 访问第一个元素
print(fruits[-1])  # 访问最后一个元素
print(fruits[1:3])  # 访问第二个和第三个元素
print(fruits[::2])  # 访问第一个、第三个和第五个元素

# 列表的修改(可变性) 而字符串是不可变的
fruits = ['apple', 'banana', 'orange', 'pear', 'peach']
fruits[0] = 'Apple'
print(fruits)
fruits.append('grape')  # 追加元素
print(fruits)
fruits.insert(0, 'watermelon')  # 插入元素
print(fruits)
del fruits[0]  # 删除指定位置元素
fruits.remove('orange')  # 删除指定元素
print(fruits)
fruits.pop()  # 删除最后一个元素

# 列表常用方法
fruits = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9, 10]
print(len(fruits))  # 获取列表长度
print(fruits.count(1))  # 获取列表中指定元素的个数
print(fruits.index(5))  # 获取列表中指定元素的索引 (类似字符串的find)
fruits.sort()  # 升序
fruits.sort(reverse=True)  # 降序
fruits.reverse()  # 反转

# 二维列表（矩阵）
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 访问嵌套列表元素
print(matrix[1][2])  # 第2行第3列 → 6
# 遍历二维列表
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
# 输出：
# 1 2 3
# 4 5 6
# 7 8 9

# 列表推导式
# 创建0-9的列表
list1 = []  # list1 = list()
for i in range(10):
    list1.append(i)
list2 = [i for i in range(10)]  # 列表推导式

# 创建0-9的偶数列表
list3 = [i for i in range(10) if i % 2 == 0]

# 使用列表推导式生成平方数集合
list4 = [1, 3, 4, 6, 8, 10]
list4 = [i ** 2 for i in list4]
print(list4)

# 集合（Set） 集合是无序、可变的元素集合，不允许重复值，适合去重和集合运算。
# 创建集合
# 用花括号 {} 或 set() 函数创建,{}表示空字典
num = {1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10}
print(num)  # 自动对元素进行去重处理
fruits = {'apple', 'banana', 'orange', 'pear', 'peach'}
print(fruits)  # 保存的元素是无序的

# 可以通过列表创建集合
list6 = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]
set1 = set(list6)
print(set1)

# 集合基本操作
# 添加元素
fruits2 = {'apple', 'banana', 'orange', 'pear', 'peach'}
fruits2.add('grape')  # 添加元素
fruits2.update(['watermelon', 'cherry'])  # 添加多个元素
print(fruits2)
# 删除元素
fruits2.remove('orange')  # 删除指定元素,如果元素不存在，则报错
fruits2.discard('apple')  # 删除指定元素,如果元素不存在，则不报错
fruits2.pop()  # 随机删除一个元素
fruits2.clear()  # 清空集合

# 集合转列表
set4 = {'apple', 'banana', 'orange', 'pear', 'peach'}
list7 = list(set4)
print(list7)

# 集合元素
num1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
num2 = {3, 4,  6, 7, 8}
num3 = num1 & num2  # 交集
print(num3)
num4 = num1 | num2  # 并集
print(num4)
print(num1.intersection(num2))   # 交集
print(num1.union(num2))  # 并集
print(num1.difference(num2))   # 差集
print(num1.symmetric_difference(num2))  # 对称差集
