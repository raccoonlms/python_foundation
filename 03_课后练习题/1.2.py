# 2. 字符串常用操作与方法
# 1. 定义字符串
# str1 = "good" ，
# str2 = "morning" ，将它们拼接成一个新字符串 "good morning" 并打印。
str1 = "good"
str2 = "morning"
print(str1 + str2)
# 2. 统计字符串
# s = "She sells seashells by the seashore." 中字母's' 出现的次数（不区分大小写）。
s = "She sells seashells by the seashore."
print(s.count('s'))
# 3. 将字符串
# s = "python is easy" 中的所有字母转换为大写形式并打印。
s = "python is easy"
print(s.upper())
# 4. 去除字符串
# s = " Hello Python " 两端的空格并打印结果。
s = " Hello Python "
print(s.strip())
# 5. 查找字符串
# s = "Python Programming" 中子串 "Program" 第一次出现的索引位置并打印。
s = "Python Programming"
print(s.find("Program"))
# 6. 把字符串
# s = "12345" 转换为整数类型，再转换回字符串类型并打印，观察结果
s = "12345"
t = int(s)
print(t, type(t))
print(str(t))

