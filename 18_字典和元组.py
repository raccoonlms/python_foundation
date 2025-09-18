# 字典 字典是无序（Python 3.7+ 后为有序）的键值对（key-value） 集合，通过键快速访问值，适合存
# 储具有映射关系的数据（如用户信息、配置参数等）。
# 创建字典
person = {
    'name': '张三',
    'age': 18,
    'sex': '男'
}
print(person)
# dict()函数创建字典
my_dict = dict(name='张三', age=18, sex='男')
# 空字典创建
my_dict1 = {}      # 创建空字典
my_dict2 = dict()
print(type(my_dict))
my_set = set()   # 创建空集合
print(type(my_set))

# 字典的键KEY特性
# 1.key不可变（数字，字符串，元组作为key）(列表，字典，集合作为key会报错)
my_dict3 = {
    1: '张三',
    'name': '张三',
    (1, 2): '张三'
}
# 2.key不可重复(如果重复，后面的key会覆盖前面的key)
# my_dict4 = {
#     'name': '张三',
#     'name': '李四'
# }

# 字典访问和更新
# 字典访问 字典名称[key]
person1 = {
    'name': '张三',
    'age': 18,
    'sex': '男'
}
print(person1['name'])
# get(key, default=None)  方法
print(person1.get('name'))
# 修改元素
person1['name'] = '张三1'
# 删除元素
del person1['name']  # 根据key删除元素
del_person = person1.pop('sex')  # 根据key删除元素，并返回这个元素
print(del_person)

# 字典常用方法
person3 = {
    'name': '张三',
    'age': 18,
    'sex': '男'
}
# 获取所有key
print(person3.keys())
# 获取所有value
print(person3.values())
# 获取所有key-value
print(person3.items())

# 向字典中添加新的键值对元素
person3['address'] = '上海'
person3.update({'phone': '12345678901', 'email': '12345678901@163.com'})


# 元组
# 元组是有序、不可变的元素集合，允许重复值，元素类型可混合，适合存储不可修改的序列数据（如坐标、日期等）。
# 创建元组使用()括号
point = (1, 2)
print(point)
print(type(point))
dates = ('2025', '9', '18')
print(dates)
# 使用tuple()函数创建元组
my_tuple = tuple([1, 2, 3, 4, 5])

# 空元组
empty_tuple1 = ()
empty_tuple2 = tuple()

# 元组索引
fruits = ('apple', 'banana', 'orange', 'grape')
print(fruits[0])
# 元组切片
print(fruits[0:2])
# 元组常见方法
fruits1 = ('apple', 'banana', 'orange', 'grape')
print(len(fruits1))  # 获取元组长度
print(fruits1.count('apple'))  # 获取元素出现的次数
print(fruits1.index('orange'))  # 获取元素在元组中的索引,不存在报错

# 元组的不可变性与应用场景
# nums = (1, 2, 3, 4, 5)
# nums[0] = 10  # 报错,
# print(nums)

points = {
    (1, 2): 'A',
    (3, 4): 'B',
    (5, 6): 'C'
}