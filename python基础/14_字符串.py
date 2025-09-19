# 字符串的索引和切片
s = "hello world"
print(s[0])  # 第一个字符内容，正向索引
print(s[5])  # 第六个字符内容，正向索引
print(s[-1])  # 最后一个字符内容，反向索引
print(s[-5])  # 倒数第五个字符内容，反向索引
# 切片 语法：字符串[start:stop:step]
s = "abcdefgh"
# 截取从索引2到5的字符（不包含5）
print(s[2:5])  # 输出 'cde'
# 从开头截取到索引4
print(s[:4])  # 输出 'abcd'
# 从索引5截取到结尾
print(s[5:])  # 输出 'fgh'
# 步长为2（间隔1个字符）
print(s[::2])  # 输出 'aceg'
# 反向切片（步长为-1，倒序）
print(s[::-1])  # 输出 'hgfedcba'

# 字符串常用操作
# 1.字符串的拼接与重复
s1 = "hello"
s2 = "world"
print(s1 + s2)
print(s1 * 3)  # 重复输出3遍s1
print('-' * 20)
# 2.字符串的长度
# 使用len()函数获取字符串的长度（包含空格和符号）
s3 = "hello world"
print(len(s3))

# 字符串的常用方法
# 1.大小写转换
s = "hello world你好 WoRld"
print(s.upper())  # 将英文字符转换为大写
s = "PYTHON"
print(s.lower())  # 将英文字符转换为小写
s = "hello world"
print(s.title())  # 将字符串每个单词首字母大写

# 查找和替换
"""find(sub)：查找子串 sub 的起始索引，找不到返回-1。"""
# replace(old, new)：将所有 old 子串替换为 new。
s = "hello world,Pyhon is fun"
print(s.find("P")) # 输出 12，第13个字符是P
s = "我cnm"
print(s.replace("cnm", "***"))

# 删除空白字符
s = "   hello world   "
print(s.strip())  # 删除字符串首尾的空白字符,包括空格、换行符、制表符等
print(s.lstrip())  # 删除字符串的左侧空白字符（rstrip()删除字符串的右侧空白字符）

# 分割与连接
s = "apple,banana,orange"
fruits = s.split(",")  # 将字符串按逗号分割成列表
print(fruits)  # 输出 ['apple', 'banana', 'orange']
new_str = "-".join(fruits)  # 将列表中的元素连接成一个字符串
print(new_str)

# 字符串的不可变性
# s = "hello world"
# s[0] = "H"
# print(s)
S_new = "H" + s[1:]
print(S_new)
# 转义字符
print("hello\nworld")
print("hello\tworld")  # 制表符
print("hello\"world\"world")  # 转义双引号
print("hello\\world")  # 转义反斜杠,表示路径分隔符\