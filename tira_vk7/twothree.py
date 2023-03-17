from heapq import heappush, heappop

def smallest(n):
    heap = [1]
    for i in range(n):
        smallest = heappop(heap)
        heappush(heap,smallest*2)
        heappush(heap,smallest*3)
    return heap[0]

if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552