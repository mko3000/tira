from heapq import heappush, heappop
keko = []
heappush(keko,5)
heappush(keko,3)
heappush(keko,8)
heappush(keko,7)
print(keko[0]) # 3
print(keko)
heappop(keko)
print(keko[0]) # 5
print(keko)


from heapq import heapify, heappop
keko = [5,3,8,7]
heapify(keko)
print(keko[0]) # 3
print(keko)
print(heappop(keko))
print(keko[0]) # 5
print(keko)