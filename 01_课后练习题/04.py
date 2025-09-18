# 四、控制台输入输出练习题（交互操作）
# 1. 编写一个 “个人信息收集” 程序：
# 通过input()函数依次获取用户的姓名、年龄、身高（保留 1 位小数）、是否喜欢
# Python（输入 “是” 或 “否”）
# 通过print()函数将收集到的信息整理输出，格式如下：
name = input("请输入你的姓名：")
age = int(input("请输入你的年龄："))
height = float(input("请输入你的身高："))
like_python = input("你喜欢Python吗？（输入是或否）")
print(f"你的个人信息为：\n姓名：{name}\n年龄：{age}\n身高：{height:.2 f}\n是否喜欢Python：{like_python}")
# 2. 编写代码实现 “数值计算交互”：
# 提示用户输入两个整数，分别存储到num1和num2变量中
# 计算两个数的和、差、积，并用一句话打印结果（如 “3 + 5 = 8，3 - 5 = -2，3 * 5 = 15”）
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))
print(f"和= {num1 + num2}，差 = {num1 - num2}，积= {num1 * num2}")
