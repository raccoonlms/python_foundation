# . 字典（dict）
# 1. 创建一个字典，包含键值对："name": "Bob" ， "age": 30 ，"city": "Shanghai" ，然后打印该字典。
example = {
    "name": "Bob",
    "age": 30,
    "city": "Shanghai"
}
print(example)
# 2. 向上述字典中添加键值对 "job": "engineer" 并打印字典。
example["job"] = "engineer"
print(example)
# 3. 获取上述字典中键为  "city" 对应的值并打印。
print(example["city"])
# 4. 创建字典 dict_scores = {"math": 90, "english": 85, "science": 95} ，
# 修改键 "english" 对应的值为 88 并打印字典。
dict_scores = {"math": 90, "english": 85, "science": 95}
dict_scores["english"] = 88
print(dict_scores)
# 5. 删除字典 dict_scores 中键为 "math" 的键值对，打印删除后的字典。
del dict_scores["math"]
print(dict_scores)
# 6. 遍历字典 dict_example = {"a": 1, "b": 2, "c": 3} ，打印所有的键和值。
dict_example = {"a": 1, "b": 2, "c": 3}
print(dict_example .items())