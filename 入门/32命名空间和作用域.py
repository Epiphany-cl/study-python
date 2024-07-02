# global 和 nonlocal

s = 0


def fun1():
    s = 0

    def fun2():
        nonlocal s
        s = 0
        for i in range(100):
            s += i
        print("fun2", s)

    fun2()
    print("fun1", s)


fun1()
print("global", s)
