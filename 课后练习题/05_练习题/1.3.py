# 3. 文件写入操作
# 1. 编写代码，向 new.txt 文件中写入 “Welcome to file writing!”，然后查看文件内容。
with open('new.txt', 'w', encoding='utf-8') as file:
    file.write('Welcome to file writing!')
# 2. 向已存在的info.txt 文件（内容如前面所示）中追加内容 “New Line”，然后读取文件查看结果。
with open('info.txt', 'a+', encoding='utf-8') as file:
    file.write('New Line')
with open('info.txt', 'r', encoding='utf-8') as file:
    print(file.read())
