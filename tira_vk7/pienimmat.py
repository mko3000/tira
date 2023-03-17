import time
from heapq import heapify, heappop
import random

def jarjestava(luvut):
    luvut.sort()
    summa = sum(luvut[0:(int(len(luvut)/10))])
    return summa

def pinoava(luvut):
    heapify(luvut)
    summa = 0
    for i in range(int(len(luvut)/10)):
        summa += heappop(luvut)
    return summa


if __name__ == "__main__":
    n = 10**6
    s = []
    for i in range(n):
        s.append(random.randint(1,10**9))
    
    alku = time.time()
    print(jarjestava(s))
    loppu = time.time()
    print("Järjestäen:", (loppu-alku),"s")

    alku = time.time()
    print(pinoava(s))
    loppu = time.time()
    print("Pinoten:", (loppu-alku),"s")