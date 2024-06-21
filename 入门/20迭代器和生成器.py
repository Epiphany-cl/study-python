import sys

# 迭代器 iter() 和 next()。
it = iter([1, 2, 3])
while True:
    try:
        # 如果迭代器中没有元素会抛异常 StopIteration
        print(next(it))
    except StopIteration:
        break


# 创建一个迭代器类
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
class MyIter:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myIter = iter(MyIter())
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))


# 生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
def my_generator(n):
    for i in range(n):
        yield i


my_generator(5)
for i in my_generator(5):
    print(i)
