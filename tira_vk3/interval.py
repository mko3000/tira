def count(t):
    best_counter = 1
    count = 1
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]-1:
            count += 1
            if count > best_counter:
                best_counter = count
        elif t[i] != t[i+1]:
            count = 1
    return best_counter

if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3

#jos on 2 samaa peräkkäin