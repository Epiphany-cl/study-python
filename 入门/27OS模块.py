"""
OS 模块
可以用来管理文件和目录、处理权限和所有权、创建和操作链接、管理进程和文件描述符等。
"""
import datetime
import os, shutil

# os.access(path, mode) 函数用来检查文件权限。
print(os.access('../other/test.txt', os.F_OK))
print(os.access('../other/test.txt', os.R_OK))
print(os.access('../other/test.txt', os.W_OK))
print(os.access('../other/test.txt', os.X_OK))

# os.getcwd() 函数用来获取当前工作目录。 cwd(current working directory)
print(os.getcwd())

# getcwdb() 函数用来获取当前工作目录的二进制形式。
print(os.getcwdb())

# os.chdir(path) 函数用来改变当前工作目录。
os.chdir('../other')
print(os.getcwd())
os.chdir('../入门')

# os.listdir(path) 函数用来获取指定目录下的文件和子目录。
print(os.listdir('/'))

#  os.mkdir(path) 函数用来创建目录。
os.mkdir("../other/os")

# os.rmdir(path) 函数用来删除目录。
os.rmdir("../other/os")

# os.makedirs(path) 函数用来创建目录。
os.makedirs("../other/os/aa/bb/cc/dd")

# os.removedirs(path) 递归地删除路径中的所有空目录。从最底层的目录开始删除，一直向上，直到遇到非空目录为止。
open("../other/os/aa/a.txt", "w").close()
os.removedirs("../other/os/aa/bb/cc/dd")

# os.removedirs(path) 函数用来删除目录。
shutil.rmtree("../other/os")

# os.rename(src, dst) 函数用来重命名文件或目录。
file_1 = open("../other/rename/test.txt", "w")
file_1.write("Java 是世界上最好的语言 😁")
file_1.close()
file_name_new = f"test_rename_{datetime.datetime.now()}.txt"
os.rename("../other/rename/test.txt", f"../other/rename/{file_name_new}")

# os.renames(src, dst) 函数用来重命名文件或目录。
os.renames(f"../other/rename/{file_name_new}", "../other/rename/test_rename.txt")

""" 总结
os.rename() 用于简单的重命名操作，不会创建目录。
os.renames() 在重命名的同时可以递归创建不存在的目录结构。
"""

# os.walk() 函数用来遍历目录树。
walk_1 = os.walk("../other")
for root, dirs, files in walk_1:
    print(f'root={root}, dirs={dirs}, files={files}')

# os.dup(fd) 函数用来复制文件描述符。
fd_1 = os.open("../other/test.txt", os.O_RDONLY)
fd_2 = os.dup(fd_1)
print(fd_2.real)  # 实部
print(fd_2.imag)  # 虚部
print(fd_2.numerator)  # 分子
print(fd_2.denominator)  # 分母
os.close(fd_1)
os.close(fd_2)

# os.dup2(fd, fd2) 函数用来复制文件描述符。
fd_1 = os.open("../other/test.txt", os.O_RDONLY)
fd_2 = os.dup2(fd_1, os.O_WRONLY)
os.close(fd_1)
os.close(fd_2)

# os.lseek() 函数用来改变文件指针的位置。
fd_3 = os.open("../other/test.txt", os.O_RDWR)
print(os.read(fd_3, 1024))
os.close(fd_3)
"""
- **只读模式**：`O_RDONLY` 可以记作 "Read Only"，表示文件只能读取。
- **只写模式**：`O_WRONLY` 可以记作 "Write Only"，表示文件只能写入。
- **读写模式**：`O_RDWR` 可以记作 "Read and Write"，表示文件可读可写。
- **追加模式**：`O_APPEND` 可以联想为 "Append"，表示在文件末尾追加数据。
- **创建模式**：`O_CREAT` 可以联想为 "Create"，表示如果文件不存在则创建新文件。
- **排他模式**：`O_EXCL` 可以联想为 "Exclusive"，与`O_CREAT`一起使用时，确保独占地创建文件。
- **截断模式**：`O_TRUNC` 可以联想为 "Truncate"，打开文件时清空其内容。
"""

# os.truncate(path, length) 函数用来截断文件。

# os.unlink(path) 函数用来删除文件。
# os.symlink(src, dst) 函数用来创建符号链接。
# os.link(src, dst) 函数用来创建硬链接。
# os.readlink(path) 函数用来读取符号链接。
