# 1. 列表（list）
# 1. 创建一个包含字符串 "apple" 、 "banana" 、"orange" 的列表，然后在列表末尾添加字符串 "grape" 并打印列表。
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
print(fruits)
# 2. 创建列表
# nums = [8, 2, 5, 2, 7, 3] ，删除列表中值为 2 的第一个元素，并打印修改后的列表。
nums = [8, 2, 5, 2, 7, 3]
nums.remove(2)
print(nums)
# 3. 对列表 nums = [9, 4, 6, 1, 3] 进行排序，使其按升序排列并打印。
nums = [9, 4, 6, 1, 3]
nums.sort()
print(nums)
# 4. 创建列表
# colors = ["red", "green", "blue"] ，在列表索引为 1 的位置插入字符串"yellow" 并打印列表。
colors = ["red", "green", "blue"]
colors.insert(1, "yellow")
print(colors)
# 5. 复制列表original = [10, 20, 30] 到新列表new_list ，然后修改new_list 的第一个元素为5
# 分别打印original ,mew_list，观察变化。
original = [10, 20, 30]
new_list = original[::]
new_list[0] = 5
print(original)
print(new_list)
# 6. 统计列表 nums = [1, 3, 5, 3, 7, 3] 中元素 3 出现的次数。
nums = [1, 3, 5, 3, 7, 3]
print(nums.count(3))