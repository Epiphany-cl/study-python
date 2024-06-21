import math

# sin() cos() tan() asin() acos() atan() 不多解释
pi = math.pi
print(math.sin(pi / 6))  # sin(30°)
asin_0_5 = math.asin(0.5)  # 0.5235987755982988
print(asin_0_5 / pi * 180)  # 转化为角度 30°

# atan2(x, y) 获取角度的反正切值
print(math.atan2(1, 1))  # 0.7853981633974483 也就是 45°

# hypot(x, y) 获取直角三角形的斜边长度 欧几里得数
print(math.hypot(3, 4))

# degrees() radians()
print(math.degrees(pi / 2))  # 转换为角度
print(math.radians(90))  # 转换为弧度
