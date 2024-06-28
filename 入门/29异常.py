# 异常处理 try、except、else 和 finally
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("不能除以零！", e)
except ValueError:
    print("输入的不是一个有效的数字！")
else:
    print(f"结果是: {result}")
finally:
    print("这段代码总是会执行。")

# 抛出异常 Python 使用 raise 语句抛出一个指定的异常。
# raise [Exception [, args [, traceback]]]
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
