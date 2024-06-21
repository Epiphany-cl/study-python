s1 = 'hello world'

# upper() 小大写转换
print('s1.upper():', s1.upper())
print('s1.lower():', s1.lower())

# startswith() endswith()
print("s1.startswith('hello'):", s1.startswith('hello'))
print('s1.endswith("world"):', s1.endswith("world"))

print('s1.isdigit():', s1.isdigit())

print("'           你好 世界         '.strip():", ' 你好 世界 '.strip())

print("'北京 上海 广州 深圳'.split(' '):", '北京 上海 广州 深圳'.split(' '))

print("';'.join(['1', '2', '3']):", ';'.join(['1', '2', '3']))

print('s1.find("world"):', s1.find("world"))

print("s1.count('l'):", s1.count('l'))

print('s1.replace(" ", "_"):', s1.replace(" ", "_"))
