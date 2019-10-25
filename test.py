import time as t
import numpy as np

def doSomething():
    a = range(10000000)
    b = range(10000000)
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])

def doSomethingEx():
    a = np.arange(10000000)
    b = np.arange(10000000)
    c = a + b

if __name__ == "__main__":
    start = t.time()

    doSomethingEx()

    print(t.time() - start)