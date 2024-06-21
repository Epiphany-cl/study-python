# 一个 Java 开发学习 Python 记录

## 1. 注释

python 单行注释:`#`，多行注释:`"""""`
> python 的多行注释本质是未被引用的字符串

## 2. 字符串格式化输出 %、{}

```python
name = "小明"
age = 18
# 方法一
print("名字：%s，年龄：%d" % (name, age))
# 方法二 3.6 版本的解释器才有
print(f"名字：{name}，年龄：{age}")
```

字典的格式化输出
```python
table = {'Google': 1, 'Baidu': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))
```
> `{0:10}` 表示的是第一个参数（在这个例子中是name）会被转换成一个字符串，并且至少占据10个字符宽度的空间。

```python
table = {'Google': 1, 'Baidu': 2, 'Taobao': 3}
print('Baidu: {0[Baidu]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
print('Baidu: {Baidu:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
```
> 这种方式利用了`**`运算符来解包字典`table`
## 3. python 中特殊的运算符和关键字

1. `//` 整除
2. `**` 幂运算
3. `not` 关键字 相当于 Java 中的 `!`
4. `a, b = 1, 2` 多变量赋值
5. `in` 可以检查成员关系
6. `:=` 赋值表达式 又叫 海象运算符，将赋值和应用并为一步
7. `[out_exp_res for out_exp in input_list if condition]` 推导式
8. `and` 和 `or` 相当于 Java 中的 `&&`和`||`

## 4. python 元组使用小括号 `()`，列表使用方括号 `[]`。

- 元组的元素不能修改
- 其他使用方法和列表基本一致

## 5. Python 解释器

- Python 装饰器直接改变了函数的执行流程，可以在函数调用前后添加自定义逻辑。
- Java 注解则是在编译时或运行时提供元数据，需要通过反射 API 或其他工具来读取并处理注解信息。

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
```

除了函数装饰器，Python 还支持类装饰器。类装饰器是包含 __call__ 方法的类，它接受一个函数作为参数，并返回一个新的函数。

```python
class DecoratorsClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before calling the function")
        result = self.func(*args, **kwargs)
        print("After calling the function")
        return result


@DecoratorsClass
def my_function():
    print("Inside the function")


my_function()
```

# 5. Python 标准库
Python 3 的标准库非常丰富，提供了大量的模块来支持各种功能。以下是一些主要的模块和它们的用途：

1. **os**: 提供与操作系统交互的功能，如文件操作、进程管理等。
2. **sys**: 提供与 Python 解释器交互的功能，如命令行参数、解释器状态等。
3. **math**: 提供数学函数，如三角函数、对数函数等。
4. **cmath**: 复数数学函数。
5. **random**: 随机数生成。
6. **statistics**: 统计计算，如平均值、中位数、众数等。
7. **datetime**: 日期和时间处理。
8. **time**: 时间相关功能，如延时、时间格式化等。
9. **re**: 正则表达式支持。
10. **string**: 字符串操作函数和常量。
11. **collections**: 高级数据结构，如 defaultdict、deque 等。
12. **itertools**: 迭代器函数，用于高效循环。
13. **functools**: 函数工具，如偏函数、装饰器等。
14. **operator**: 实现内建操作符的函数。
15. **contextlib**: 上下文管理器，用于 with 语句。
16. **argparse**: 命令行参数解析。
17. **json**: JSON 数据编码和解码。
18. **pickle**: 对象序列化和反序列化。
19. **shutil**: 高级文件操作，如复制、移动文件和目录等。
20. **zipfile**: ZIP 文件存档读写。
21. **tarfile**: TAR 文件存档读写。
22. **gzip** 和 **bz2**: 压缩文件读写。
23. **socket**: 网络编程。
24. **http.server**: 简单的 HTTP 服务器。
25. **urllib**: URL 请求和解析。
26. **requests** (虽然不是标准库，但非常常用): HTTP 请求库。
27. **email**: 邮件处理。
28. **sqlite3**: SQLite 数据库接口。
29. **csv**: CSV 文件读写。
30. **xml.etree.ElementTree**: XML 文档解析和生成。
31. **subprocess**: 子进程管理。
32. **pathlib**: 路径操作，提供面向对象的 API。
