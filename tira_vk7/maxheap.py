from heapq import heappush, heappop, heapify

def count(n):
    
    k = 1
    t = 0
    i = 0
    while k < n:
        i += t*k
        k *= 2
        t += 1
    yli = n-k+1
    i += yli*t
    if yli < 0:
        i += abs(yli)

    return i

if __name__ == "__main__":
    print(count(1))
    print(count(2))
    print(count(3))
    print(count(4)) # 4
    print(count(5))
    print(count(7)) # 10
    print(count(123)) # 618
    print(count(999999999)) # 27926258178