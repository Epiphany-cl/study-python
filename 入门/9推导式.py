""" 列表推导式
[表达式 for 变量 in 列表]
[out_exp_res for out_exp in input_list]
或者
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
"""

# 计算 30 以内可以被 3 整除的整数：
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

""" 字典推导式
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }
"""

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dic = {str(key): key ** 2 for key in {1, 2, 3}}
print(dic)

""" 集合推导式
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
"""

new = {i ** 2 for i in (1, 2, 3)}
print(new)

"""
`(1, 2, 3)` 和 `{1, 2, 3}` 在Python中代表两种不同的数据类型：
1. `(1, 2, 3)` 是一个元组（Tuple）。
元组是不可变的序列类型，一旦创建就不能修改。这意味着你不能向元组中添加或删除元素，也不能改变已存在的元素。
元组使用圆括号 `()` 来创建，但在实际使用中，圆括号通常是可选的，除非你需要在一个表达式中明确区分这是一个元组。
元组的一个常见用途是在需要一个固定集合的值，比如作为字典的键时。
2. `{1, 2, 3}` 是一个集合（Set）。
集合是一个无序的、不重复的元素集合。
集合使用花括号 `{}` 来创建，并且可以动态地添加或删除元素。由于集合不允许重复元素，所以如果尝试添加已经存在于集合中的元素，该元素将被忽略。
集合常用于去除列表中的重复项，或者进行集合运算，如并集、交集和差集等。
"""

""" 元组推导式（生成器表达式）
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
"""
a = (x for x in range(1, 10))
print(a)
print(tuple(a))
