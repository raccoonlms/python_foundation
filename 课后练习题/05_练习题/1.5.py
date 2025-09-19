# 5. 文件操作综合案例
# 1. 编写程序，实现以下功能：
# 提示用户输入一些内容。
# 将用户输入的内容写入到
# user_input.txt 文件中。
# 然后读取该文件的内容并打印。
with open('user_input.txt', 'a+', encoding='utf-8') as file:
    file.write(input('请输入内容：'))
    file.seek(0)  # 将文件指针移到开头
    print(file.read())
# 2. 编写程序，统计article.txt 文件（假设文件存在，包含若干文本）的行数、单词数（以空格
# 分隔为单词），并打印统计结果。
with open('article.txt', 'r', encoding='utf-8') as f:
    print('行数：',len(f.readlines()))
    f.seek(0)  # 将文件指针移到开头
    count = 0
    for line in f:
        line = line.strip()  # 去除空白字符
        line = line.replace(',', '').replace('.', '')  # 替换,和.
        words_list = line.split(' ')  # 按照空格进行切割
        count += len(words_list)
    print('单词数：', count)