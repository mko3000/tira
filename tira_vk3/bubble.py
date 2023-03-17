def count(t):
    max_distance = 0
    for i in range(len(t)):
        max_distance = max(max_distance,i+1-t[i])
    return max_distance

if __name__ == "__main__":
    print(count([1, 2, 3])) # 0
    print(count([2, 3, 4, 1])) # 3
    print(count([5, 1, 2, 3, 4])) # 1
    print(count([6, 2, 4, 1, 5, 3])) # 3
    print(count([2, 7, 4, 1, 9, 3, 8, 6, 5, 10])) # 4

