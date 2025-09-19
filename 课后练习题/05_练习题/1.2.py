# 2. 文件读取操作
# 1. 有一个info.txt 文件，内容如下：使用 read() 方法读取该文件的全部内容并打印。
# Hello
#  Python
#  File
#  Operation
with open('info.txt', 'r', encoding='utf-8') as f:
    print(f.read())
# 2. 对于上述info.txt 文件，使用readline() 方法逐行读取并打印每一行内容。
with open('info.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
# 3. 对于上述info.txt 文件，使用readlines() 方法读取所有行，存储到列表中，然后遍历列表
# 打印每一行。
with open('info.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        