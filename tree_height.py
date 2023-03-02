# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    koks=numpy.zeros(n)

    def height(int):
        if koks[int]!=0:
            return koks[int]
        if parents[int]==-1:
            koks[int]=1
        else:
            koks[int]=height(parents[int])+1
        return koks[int]

    for e in range(n):
        height(e)

    max_height=int(max(koks))
    return max_height


def main():
    # implement input form keyboard and from files
    letterInput=input("F/I: ")
    if "F" in letterInput:
        fInput=input("file: ")
        if "a" in letterInput:
            return
        with open(f"./test/{fInput}", mode="r") as file:
            n=int(file.readline().strip())
            vals=list(map(int, file.readline().strip().split()))
    if "I" in letterInput:
        n=int(input())
        vals=list(map(int, input().split()))
    print(compute_height(n, vals))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))