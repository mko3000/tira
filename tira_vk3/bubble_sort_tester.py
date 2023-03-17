def bubble(t):
    count = 0
    print(t)
    while True:
        change = False
        for i in range(len(t)-1):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
                change = True                
        if not change:
            break
        print(t)
        count += 1
    return count



if __name__ == "__main__":
    print(bubble([1, 2, 3])) # 0
    print(bubble([2, 3, 4, 1])) # 3
    print(bubble([5, 1, 2, 3, 4])) # 1
    print(bubble([6, 2, 4, 1, 5, 3])) # 3
    print(bubble([2, 7, 4, 1, 9, 3, 8, 6, 5, 10])) # 4

