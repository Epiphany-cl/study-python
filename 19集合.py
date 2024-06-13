"""
集合（set）是一个无序的不重复元素序列。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。
"""
set1 = {1, 1, 1}
set2 = set()
set2.add(1)
print(set1)
print(set2)

# add 方法适用于添加单个元素，而 update 方法更适用于从一个或多个可迭代对象中添加多个元素到集合中。
set1.add(1)
set1.update([1, 2, 3])
print(set1)

# remove 和 pop 方法在元素不存在时会引发异常，而 discard 方法则可以安全地移除元素而不会引发异常。
set1 = {1, 2, 3, 4, 5}
set1.remove(1)
set1.discard(1)
set1.pop()
