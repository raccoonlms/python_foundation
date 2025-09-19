# # 21_文件操作.py
# # open('文件路径', '模式',编码格式)
# file = open('a.txt', 'r', encoding='utf-8')
# # r只读模式（默认），文件不存在则报错
# # w写入模式，文件不存在则创建，存在则清空内容
# # a追加模式，文件不存在则创建，新内容添加到末尾
# # r+读写模式，可读取和写入
# # w+读写模式，会先清空文件内容
# # a+读写模式，新内容追加到末尾
# data = file.read()
# print(data)
# file.close()
#
# # 写入文件操作
# file = open('a.txt', 'w', encoding='utf-8')
# file.write('hello world')
# file.close()
#
# # 文件读取操作
# # read() 读取整个文件内容，返回字符串
# # read(n) 读取前 n 个字符
# # readline() 读取一行内容
# # readlines()  读取所有行，返回列表（每行作为元素）
# file = open('a.txt', 'r', encoding='utf-8')
# for line in file:
#     print(line.strip())  # 去掉行末的换行符
# file.close()
#
# # 写入内容到文件的常用方法：
# # write(str) ：写入字符串。
# # writelines(iterable) ：写入可迭代对象（如列表，需自行添加换行符）。
# file = open('a.txt', 'w', encoding='utf-8')
# file.write('hello world 1')
# file.writelines(['hello worldc 2\n', 'hello world 3\n'])
# lines = ['hello world 4\n', 'hello world 5\n']
# file.writelines(lines)
# lines2 = ['hello world 6', 'hello world 7']
# file.writelines([line + '\n' for line in lines2])
# file.close()
#
# # 追加内容  w 模式会清空原有内容，如需保留原有内容并添加新内容，用 a 模式。
#
# # 上下文管理器  with 语句
# # 自动管理文件关闭，避免忘记 close() 导致的资源泄露，推荐优先使用。
# # with open('路径','模式',encoding =编码格式) as 文件对象
# with open('a.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line.strip())
#
# # 案例
# # 需求：将 a.txt 文件中的内容复制到 b.txt 文件中
# with open('a.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
# with open('b.txt', 'w', encoding='utf-8') as f:
#     f.write(content)
# print('复制完成')
# # 统计c.txt的文件中的单词数量
# with open('c.txt', 'r', encoding='utf-8') as f:
#     count = 0
#     for line in f:
#         line = line.strip()  # 去掉行末的换行符, 空行，——
#         line.replace('-', '').replace('.', '').replace(',', '')
#         words = line.split(" ")  # 以空格为分隔符，将行内容分割成单词列表
#         count += len(words)
#     print(count)
# 1. 编写程序，读取 scores.txt （每行一个学生成绩），计算平均分并写入 result.txt 。

# with open('scores.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     scores = [float(line.strip()) for line in lines]  # 将每行内容去除换行 转换为数字
#     avg = sum(scores) / len(scores)
#     with open('result.txt', 'w', encoding='utf-8') as f:
#         f.write(f'平均分：{avg:.2f}')

# 2. 用 a 模式向  log.txt 中追加一条日志，格式为 “[2025-10-01 12:00:00] 操作内容”
# （时间可用固定字符串）。

# import time
#
# with open('log.txt', 'a', encoding='utf-8') as f:
#     f.write(f'{time.strftime("[%Y-%m-%d %H:%M:%S]")} 操作内容\n')

# 3. 读取 poem.txt ，统计其中包含 “月” 字的行数(文件内容自定义)。
with open('poem.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    count = 0
    for line in lines:
        if '月' in line:
            count += 1
    print(count)