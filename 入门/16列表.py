list1 = ['Google', 'Baidu', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# Python列表脚本操作符 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
print(list1 + list2)
print(list1 * 2)

# 迭代
for item in list1:
    print(item)

# 判断包含
print(2000 in list1)

# 嵌套表
print([list1, list2])

# 函数和方法
len(list1)
max(list3)
min(list3)
list((1, 2, 3))
list1.append(2024)
list1.count(2000)
list1.extend(list2)
list1.index(2024)
list1.insert(1, [123])
list1.pop()
list1.remove(2024)
list1.reverse()
list3.sort()
list1.clear()
list2.copy()
