# 变量转换为整形
num = '18'
print(type(num))
num = int(num)  # 转换为整形
print(type(num))
print(num + 1)

# 浮点转换为整形
num = 9.99
print(type(num))
num = int(num)  # 转换为整形
print(type(num))
print(num)

# 转换为浮点型
num = '9.99'
print(type(num))
num = float(num)  # 转换为浮点型
print(type(num))
print(num)
num = 10
print(type(num))
num = float(num)
print(num)  # 10.0

# 当字符串的内容不清楚时，使用eval()函数
num = '10'
print(type(num))
num = eval(num)
print(type(num))

# 布尔转换为整形
num = True
print(type(num))
num = int(num)  # 转换为整形
print(type(num))
print(num)
