# 自定义异常 异常类继承自 Exception 类
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


raise MyError("啦啦啦")
