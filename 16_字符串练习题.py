# 案例 12：用户输入处理
# 需求：接收用户输入的姓名（可能包含前后空格），将首字母大写，其余小写，并输出欢迎信息。
name = input("请输入你的姓名：")
name = name.strip()  # 去除前后空格
print(name)
name = name.title()  # 首字母大写
print(f"欢迎你，{name}")

# 案例 13：邮箱验证（简化版）
# 需求：判断输入的邮箱是否包含 @ 和 .，且 @ 在 . 之前。
email = input("请输入邮箱：")
if email.find("@") != -1 and email.find(".") != -1:
    if email.find("@") < email.find("."):
        print("邮箱格式正确")
    else:
        print("邮箱格式错误")
else:
    print("邮箱格式错误")
# 编写程序，输入一个字符串，输出其反转后的结果（如输入 "abc" 输出 "cba"）
str1 = input("请输入字符串：")
print(str1[::-1])

# 统计字符串中大写字母、小写字母和数字的个数（如 "Abc123" → 大写 1，小写 2，数字 3）。
s= input("请输入字符串：")
count_upper = 0
count_lower = 0
count_digit = 0
for c in s:
    if 'A' <= c <= 'Z':
        count_upper += 1
    elif 'a' <= c <= 'z':
        count_lower += 1
    elif '0' <= c <= '9':
        count_digit += 1
print(f"大写字母个数：{count_upper}小写字母个数：{count_lower}数字个数：{count_digit}")
#  输入一个手机号（11 位数字），用字符串切片将中间 4 位替换为 *（如 "13800138000" →  "1388000"）。
phone = input("请输入手机号：")
new_phone = phone[:3] + "*" * 4 + phone[-4:]
replace_phone = phone[3:7]
print(replace_phone.replace(replace_phone, "****"))
