# := 赋值表达式 又叫 海象运算符，将赋值和应用并为一步
a = 1
if a == 1:
    print("a = 1")
# 相比于传统方法少一部
if (b := 2) == 2:
    print("b = 2")

# 应用
# 1. 在while循环中使用
while (n := int(input("请输入一个数字（输入0退出）："))) != 0:
    print(f"你输入的数字是: {n}")

# 2. 在列表推导式中使用
numbers = [1, 2, 3, 4, 5]
results = [(square := n ** 2) for n in numbers]
print(results)

# 3. 在if语句中使用
if (result := complex(1, 2)) is not None:
    print(result)
