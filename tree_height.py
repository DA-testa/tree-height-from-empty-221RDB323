# python3

# Danila Sinicins 221RDB323

#import sys
#import threading
import numpy


def compute_height(n, parents):
    koks=numpy.zeros(n)

    def height(i):
        if koks[i]!=0:
            return koks[i]
        if parents[i]==-1:
            koks[i]=1
        else:
            koks[i]=height(parents[i])+1
        return koks[i]

    for i in range(n):
        height(i)

    max_height=int(max(koks))
    return max_height


def main():
    # implement input from keyboard and from files
    letterInput=input("F/I: ")
    if "F" in letterInput:
        fileInput=input()
        if "a" in letterInput:
            return
        path = "test/" + fileInput
        fileRead = open(path, mode="r")
        n=int(fileRead.readline().strip())
        parents=list(map(int, fileRead.readline().strip().split()))

    if "I" in letterInput:
        n=int(input())
        parents=list(map(int, input().split()))
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))