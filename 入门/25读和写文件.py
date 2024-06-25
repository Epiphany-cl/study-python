"""
open(filename, mode) 将会返回一个 file 对象, node 默认是 r
"""
import pickle
import pprint

file = open("./0hello.py")
print(file.read())
file.close()

file_w = open("../other/test.txt", "w")  # w 模式会清空原数据
file_w.write("Java 是世界上最好的语言\n")
file_w.write("Java 是世界上最好的语言\n")
file_w.close()

# pickle 模块,实现了基本的数据序列和反序列化。
# 序列化
data = {"name": "James", "age": 18, "gender": "male"}
file_s = open("../other/data.pkl", "wb")
pickle.dump(data, file_s)
file_s.close()
# 反序列化
file_ss = open("../other/data.pkl", "rb")
data_s = pickle.load(file_ss)
print(data_s)  # {'name': 'James', 'age': 18, 'gender': 'male'}
