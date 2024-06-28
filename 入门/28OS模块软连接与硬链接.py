# os.unlink(path) 函数用来删除文件。
# os.symlink(src, dst) 函数用来创建符号链接。
# os.link(src, dst) 函数用来创建硬链接。
# os.readlink(path) 函数用来读取符号链接。
import os

file_1 = open("../other/original.txt", "w")
file_1.write("Java 是世界上最好的语言！\n")
file_1.write("Java 是世界上最好的语言！\n")
file_1.close()

os.symlink("../other/original.txt", "../other/symlink.txt")
os.link("../other/original.txt", "../other/hardlink.txt")
print(os.readlink("../other/symlink.txt"))