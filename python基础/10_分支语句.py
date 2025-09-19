# if分支语句
# if <条件>:
#     <执行语句>
# 案例 判断是否成年
age = int(input("请输入年龄:"))
if age >= 18:
    print("已成年")

# 检查数字是否为正数
num = int(input("请输入数字:"))
if num > 0:
    print(f"{num}正数")
# if else 分支结构
# if <条件>:
# <执行语句>
# else:
# <执行语句>
# 案例 判断奇数偶数
num = int(input("请输入整数:"))
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")
# 案例2 登录验证简化版，假设用户名admin，密码123456
username = input("请输入用户名:")
password = input("请输入密码:")
if username == "admin" and password == "123456":
    print("登录成功")
else:
    print("登录失败")
# 练习 1：输入一个整数，若能被 5 整除，则打印 “该数是 5 的倍数”。
num = int(input("请输入一个整数:"))
if num % 5 == 0:
    print(f"{num}是5的倍数")
# 练习 2：输入两个数，比较大小并打印 “前者大” 或 “后者大”（假设两数不相等）。
num1 = int(input("请输入第一个数:"))
num2 = int(input("请输入第二个数:"))
if num1 > num2:
    print(f"{num1}大")
else :
    print(f"{num2}大")
# 三目运算符
num3 = int(input("请输入一个数:"))
print("正数" if num3 > 0 else "负数")

# 多重if分支
# if <条件1>:
#   <执行语句1> 满足条件1执行
# elif <条件2>:
#   <执行语句2> 满足条件2不满足条件1执行
# elif <条件3>:
#   <执行语句3> 满足条件3不满足条件1和条件2执行
# else:
#   <执行语句4> 满足所有条件都不满足执行
# 案例，成绩评级
score = int(input("请输入成绩:"))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")
# 判断月份季节
month = int(input("请输入月份:"))
if 3 <= month <= 5:
    print("春季")
elif 6 <= month <= 8:
    print("夏季")
elif 9 <= month <= 11:
    print("秋季")
elif month in [12,1,2]:
    print("冬季")
else:
    print("输入错误")
# if else 嵌套
# 年龄大于18岁 且成绩大于60
age = int(input("请输入年龄:"))
if age >= 18:
    score = int(input("请输入成绩:"))
    if score >= 60:
        print("通过")
    else:
        print("未通过")
else:
    print("未通过")
# 判断三角形类型
a = int(input("请输入三角形的边长a:"))
b = int(input("请输入三角形的边长b:"))
c = int(input("请输入三角形的边长c:"))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("等边三角形")
    elif a == b or b == c or a == c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("三角形不存在")