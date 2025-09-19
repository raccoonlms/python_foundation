# 自定义模块
version = '1.0.0'
address = '中国'


def show():
    print('show')


def qiuhe(*args):
    return sum(args)


if __name__ == '__main__':
    print('当前模块运行')
    print(f"自测求和函数{qiuhe(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")

else:
    print(f'{__name__}导入成功')
# 默认模块名称，如果在当前模块中执行，那么名称为__name__,如果在其他模块中名称为my_module
