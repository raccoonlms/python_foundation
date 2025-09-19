# 提示用户输入年份，判断是否是闰年，是则打印 “闰年”，不是则打印“平年”。
year = int(input("请输入年份："))
print("闰年" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "平年")

# 2. 提示用户输入考试分数，若分数大于等于 60，打印 “考试通过”，否则打印 “考试未通过”。
score = int(input("请输入考试分数："))
print("考试通过" if score >= 60 else "考试未通过")