import timeit

n = 50
def add():
    global n
    n += 1

print(timeit.timeit(add,number=50000))