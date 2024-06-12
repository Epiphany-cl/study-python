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

## 3. python 中特殊的运算符和关键字

1. `//` 整除
2. `**` 幂运算
3. `not` 关键字 相当于 Java 中的 `!`
4. `a, b = 1, 2` 多变量赋值
5. `in` 可以检查成员关系
6. `:=` 赋值表达式 又叫 海象运算符，将赋值和应用并为一步
7. `[out_exp_res for out_exp in input_list if condition]` 推导式
