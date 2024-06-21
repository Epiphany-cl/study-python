"""
open(filename, mode) 将会返回一个 file 对象, node 默认是 r
"""
file = open("./0hello.py")
print(file.read())
file.close()
