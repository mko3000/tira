def paths(x):
    if x == 1:
        return 1
    if x in memory:
        return memory[x]
    count = 0
    for y in graph[x]:
        count += paths(y)
    memory[x] = count
    return count   



memory = {}

graph = {}
graph[2] = [1,3]
graph[3] = [1]
graph[5] = [2,3,4]
print(graph[2])
print(paths(5))

# n=5
# graph = [[] for _ in range(n+1)]

# graph[2].append(1)
# graph[2].append(3)
# graph[3].append(1)
# graph[5].append(2)
# graph[5].append(3)
# graph[5].append(4)
# print(graph)

# print(paths(n))



# for n in range(1,10):

#     graph = [[] for _ in range(n+1)]

#     last = n
#     while last > 0:
#         for i in range(1,last):
#             graph[last].append(i)
#         last -= 1
#     print(graph[2:])
#     print(f'{n}:{paths(n)}, lasku: {2**(n-2)}')


# n=10
# graph = [[] for _ in range(n+1)]

# last = n
# while last > 0:
#     for i in range(1,last):
#         graph[last].append(i)
#     last -= 1
# print(paths(n))