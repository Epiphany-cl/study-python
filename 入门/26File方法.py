# 文件可以利用迭代器进行逐行遍历
file_1 = open("../other/test.txt", "r")
for row in file_1:
    print(row, end='')
file_1.close()

# file.fileno() 获取文件描述符 `0`：标准输入（stdin） `1`：标准输出（stdout） `2`：标准错误（stderr） `3`及以上：用户打开的其他文件的描述符
file_2 = open("../other/test.txt", "r")
print(file_2.fileno())
file_2.close()  # 3

# file.readline([size])
file_3 = open("../other/test.txt", "r")
print(file_3.readline(5))
print(file_3.readline())
file_3.close()

# file.readlines([sizeint]) 返回总和大约为sizeint字节的行
file_4 = open("../other/唐诗三百首.txt", "r")
print(file_4.readlines(100))
file_4.close()

# file.seek(offset[, whence])
file_5 = open("../other/test.txt")
file_5.seek(32)  # 中文算是三个字节，定位到字符的中间，可能会导致解码问题。
print(file_5.read())
file_5.close()

# file.tell() 返回文件指针的当前位置
file_6 = open("../other/test.txt")
print(file_6.tell())
file_6.close()

# file.isatty() 判断文件是否是一个终端设备
file_7 = open("../other/test.txt")
print(file_7.isatty())
file_7.close()

# file.truncate([size]) 截断文件，默认值为当前位置，如果size大于当前位置，则扩展文件(填充NUL)，如果size小于当前位置，则截断文件
file_8 = open("../other/test.txt", "w+")
file_8.write("Java 是世界上最好的语言\n")
file_8.write("Java 是世界上最好的语言\n")
file_8.truncate(20)
file_8.seek(0)
print(file_8.read())
file_8.close()

# file.writelines(sequence) 将序列中的元素写入文件，每个元素后面都会加上换行符
file_9 = open("../other/test.txt", "w+")
file_9.writelines(["PHP 是世界上最好的语言\n", "PHP 是世界上最好的语言\n"])
file_9.seek(0)
print(file_9.read())
file_9.close()
