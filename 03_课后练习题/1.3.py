# 3. 字符串不可变性与转义字符
# 1. 尝试修改字符串 s = "example" 的第 4 个字符为 'a' ，观察会出现什么错误，并解释原因。
s = "example"
s[3] = 'a'  # 原因是字符串不可变
print(s)
# 2. 打印包含单引号的字符串 'He said: "It\'s a good day."' ，使用转义字符实现。
print("He said: \"It\"s a good day.\"")
# 3. 打印如下格式的字符串：要求使用转义字符实现换行。
# Title: Python Basics
# Author: John
print("Title: Python Basics\nAuthor: John")
# 4. 解释字符串不可变性的含义，并举例说明（比如尝试对字符串进行修改操作）。
# 字符串不可变：字符串一旦创建，就不能被修改。使用一下方法修改字符串
s = "example"
s_new = s[:3] + "a" + s[4:]
print(s)
# 5. 打印字符串
# s = "C:\\Users\\Desktop\\file.txt" ，体会转义字符在文件路径中的使用。
print("C:\\Users\\Desktop\\file.txt")