# 学校举行跑步比赛，如果成绩在15秒以内，可以进入决赛，否则直接淘汰,如果是男性则提示“恭喜你进入男子组决赛”，否则提示“恭喜你进入女子组决赛”。
score = int(input("请输入成绩："))
if score <= 15:
    print("恭喜你进入决赛")
    sex = input("请输入性别：")
    if sex == "男":
        print("恭喜你进入男子组决赛")
    elif sex == "女":
        print("恭喜你进入女子组决赛")
    else:
        print("输入错误")
else:
    print("你被淘汰")

# 商场做活动，满300可以打折，会员打8折，非会员打9折，输出实际消费金额。
x = int(input("请输入金额："))
if x >= 300:
    isVip = input("是否会员：")
    if isVip == "是":
        print("实际消费金额：", x * 0.8)
    elif isVip == "否":
        print("实际消费金额：", x * 0.9)
    else:
        print("输入错误")
else:
    print("不满300没有打折")
