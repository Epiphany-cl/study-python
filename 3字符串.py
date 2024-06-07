# python 中字符串有三种 单引号 双引号 三引号
str1 = '你好 世界'
str2 = "你好 世界"
str3 = """你好 世界"""
print(str1)
print(str2)
print(str3)

# python 的格式化输出有两种 % {}
name = "小明"
age = 18
# 方法一
print("名字：%s，年龄：%d" % (name, age))
# 方法二 3.6 版本的解释器才有
print(f"名字：{name}，年龄：{age}")
