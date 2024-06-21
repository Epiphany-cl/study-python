"""
Python装饰器直接改变了函数的执行流程，可以在函数调用前后添加自定义逻辑。
Java注解则是在编译时或运行时提供元数据，需要通过反射API或其他工具来读取并处理注解信息。
"""


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


#  除了函数装饰器，Python 还支持类装饰器。类装饰器是包含 __call__ 方法的类，它接受一个函数作为参数，并返回一个新的函数。
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
