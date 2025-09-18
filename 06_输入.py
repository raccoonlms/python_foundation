# 输入input()
name = input("请输入你的名字：")
age = input("请输入你的年龄：")
sex = input("请输入你的性别：")
print(f"你的名字是：{name}，年龄是：{age}，性别是：{sex}")

# 使用input函数录入的数据时str类型，不能直接参与计算
price = input("请输入商品价格：")
num = input("请输入商品数量：")
price = float(price)
num = float(num)
print(f"商品总价是：{price * num: .2f}")
