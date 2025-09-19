# 1. 文件的打开与关闭
# 1. 编写代码，以只读模式打开名为test.txt 的文件，然后关闭该文件（假设文件存在）。
f = open('test.txt', 'r')
f.close()
# 2. 尝试以写入模式打开不存在的 data.txt 文件，然后查看是否生成了该文件，再关闭文件。
f = open('data.txt', 'w')
f.close()