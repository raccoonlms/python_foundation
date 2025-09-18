# 六、运算符练习题（计算与逻辑）
# 1. 算术运算符练习：定义变量a = 15，b = 4，计算并打印以下结果：
# a + b、a - b、a * b、a / b（浮点数除法）、a // b（整数除法）、a % b（取余）、a ** b（幂运算）
a = 15
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
# 2. 比较与逻辑运算符练习：
# 定义变量x = 10，y = 20，判断x > y、x == y、x != y的结果（布尔值），并打印
x = 10
y = 20
print(x > y)
print(x == y)
print(x != y)
# 定义变量age = 25，has_job = True，判断 “年龄大于 18 且有工作”（age > 18 and has_job）、
# “年龄小于 18 或没有工作”（age < 18 or not has_job）的结果，打印并解释逻辑
age = 25
has_job = True
print(f"年龄大于 18 且有工作{age > 18 and has_job}")
print(f"年龄小于 18 或没有工作{age < 18 or not has_job}")
# 3. 赋值运算符练习：定义变量num = 5，依次执行num += 3、num *= 2、num -= 4、num /= 2，每步操作后打印num的值，观察变量变化过程
num = 5
num += 3
print(num)  # 8
num *= 2
print(num)  # 16
num -= 4
print(num)  # 12
num /= 2
print(num)  # 6.0

