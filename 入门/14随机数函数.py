import random

# random.choice(sequence)从序列的元素中随机挑选一个元素
for i in range(100):
    print(random.choice(range(1, 11)))
else:
    print("random.choice(sequence) 结束")

# random.choices() 从给定的序列中随机抽取元素，并且可以指定抽取的次数
print('random.choices(range(100), k=10):', random.choices(range(100), k=10))

# random.randrange ([start,] stop [,step]) 指定半开区间 [start, stop) 内的随机整数
print('random.randrange(0, 100):', random.randrange(0, 100))

# random.randint(a, b) 返回一个指定范围内的整数
print('random.randint(1, 100):', random.randint(1, 100))

# random.random() 返回一个随机浮点数，范围是 [0.0, 1.0)
print('random.random():', random.random())

# random.seed(a=None, version=2) 设置随机数种子
random.seed(1)
print('random.random():', random.random())
random.seed()  # 取消种子

# random.shuffle(x[, random]) 将序列的所有元素随机排序
a = list(range(1, 10))
print('a:', a)
random.shuffle(a)
print('random.shuffle(a) 处理后的 a:', a)

# random.uniform(a, b) 返回一个指定范围内的随机浮点数 闭区间 [a, b]
print('random.uniform(1, 10):', random.uniform(1, 10))
