# 1. 字符串的基本概念与索引切片
# 1. 定义字符串
# s = "I love Python" ，分别打印该字符串的第 3 个字符、第 7 个字符、倒数第 2 个字符。
s = "I love Python"
print(s[2])
print(s[6])
print(s[-2])
# 2. 对字符串
# s = "Data Science" 进行切片操作，获取子串Science"
s = "Data Science"
print(s[5:])
# 3. 定义字符串
# text = "abcdefghij" ，使用切片获取从第 2 个字符到第 6 个字符的子串（包含第2 和第 6 个字符）。
text = "abcdefghij"
print(text[1:6])
# 4. 定义字符串
# str_example = "HelloWorld" ，获取从第 2 个字符开始，步长为 2 的子串并打印。
str_example = "HelloWorld"
print(str_example[1::2])
# 5. 对于字符串
# s = "Programming" ，打印其前 5 个字符组成的子串。
s = "Programming"
print(s[:5])
