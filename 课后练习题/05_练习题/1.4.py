# 4. 上下文管理器（with 语句）
# 1. 使用with 语句以只读模式打开test.txt 文件，读取其内容并打印，观察是否需要手动关闭文件。
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())
# 2. 使用 with 语句向data.txt 文件中写入 “Using with statement for writing.”，然后查看文件内容。
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('Using with statement for writing.')
    