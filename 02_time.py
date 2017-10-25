from timeit import Timer

def t1():
    li = []
    for i in range (1000):
        li.append(i)

def t2():
    li=list(range(10000))

time1 = Timer('t1()','from __main__ import t1')
print("append:",time1.timeit(10000))
time2 = Timer('t2()','from __main__ import t2')
print("append:",time2.timeit(10000))

