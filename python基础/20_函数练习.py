# 学生成绩管理系统函数
# 成绩录入，平均分计算，等级判定
def input_score():
    scores = []
    while True:
        score = input("请输入学生成绩:(输入q结束)")
        if score == "q":
            break
        if not score.isdigit():
            print("输入错误，请重新输入")
            continue
        scores.append(float(score))
    return scores


def calc_avg(scores):
    if len(scores) == 0:
        return 0
    avg = sum(scores) / len(scores)
    return avg


def get_grade(scores):
    if len(scores) == 0:
        return "无"
    elif scores >= 90:
        return "A"
    elif scores >= 80:
        return "B"
    elif scores >= 70:
        return "C"
    elif scores >= 60:
        return "D"
    else:
        return "E"


print("学生成绩管理系统")
scores = input_score()
if len(scores) > 0:
    avg = calc_avg(scores)
    print(f"平均分：{avg:.2f}")
    print(f"各成绩的等级：")
    for score in scores:
        grade = get_grade(scores)
        print(f"{score:.2f}：{grade}")
else:
    print("无有效成绩")


# 斐波那契数列前n
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(int(input("请输入n:"))))
