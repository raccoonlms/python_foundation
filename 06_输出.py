# 输出
print("hello world")
name = "小王"
print(name)

# 格式化输出
name = "小王"
age = 18
print("我的名字叫" + name + "，今年" + str(age) + "岁")
print("我的名字叫%s,今年%d岁" % (name, age))
# %s:字符串 %d:数字 %f:浮点数
title = "白菜"
price = 9.9
print("%s的价格是%.2f元" % (title, price))  # %.2f:保留两位小数

# format函数
name = "小王"
mobile = "12345678901"
print("我的名字叫{},手机号是{}".format(name, mobile))

# 简写语法
print(f"我的名字叫{name},手机号是{mobile}")
price = 9.9
print(f"价格是{price:.2f}")    # :.2f:保留两位小数

#print 输出自动加换行
print("hello world",end="")
print("hello world")