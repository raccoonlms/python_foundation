# 五、函数的作用域
# 1. 在函数内部定义一个变量inner_var = 10 ，然后在函数外部尝试打印
# inner_var ，观察会出现什么错误，并解释原因。
def func_scope():
    inner_var = 10
print(inner_var)  # 错误，因为inner_var是函数内部的变量，不能在函数外部访问
# 2. 定义一个全局变量global_var = 20 ，然后在函数内部打印global_var ，再在函数内部修改
# global_var 的值为 30，调用函数后，在外部打印global_var ，观察结果并解释。
global_var = 20
def func_scope1():
    print(global_var)
def func_scope2():
    global_var = 30
func_scope1()  # 外部打印global_var=20
func_scope2()  # 尝试在函数内修改全局global_var的值为30
print(global_var)  # 外部打印global_var=20  函数内无法直接修改全局global_var的值，需要使用global声明
# 3. 定义函数func_scope ，在函数内部定义局部变量 local_var = 5 ，然后在函数内部打印
# local_var ，再尝试在函数外部打印local_var ，解释现象。
def func_scope3():
    local_var = 5
    print(local_var)
print(local_var)  # 错误，因为local_var是函数内部的变量，不能在函数外部访问