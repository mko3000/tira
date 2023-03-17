def find(t, x):    
    numbers = 1
    t.sort()
    i=0
    j=i+1
    while i <= len(t) and j <= len(t)-1:        
        if t[j]-t[i] <= x:            
            numbers += 1
        else:
            i += 1
        j += 1
    return numbers

if __name__ == "__main__":
    print(find([10, 10, 10, 10], 0)) # 4
    print(find([4, 2, 7, 1], 0)) # 1
    print(find([7, 3, 1, 5, 2], 2)) # 3
    print(find([7, 3, 1, 5, 2], 1000)) # 5
    print(find([19, 4, 7, 17, 3, 15, 10], 5)) # 3
    print(find([10000, 987654, 123456, 139562, 13613225], 50000)) # 2
    print(find([11, 1, 11, 4], 1)) # 2
    print(find([2, 7, 14, 11, 7, 15], 11)) #5
    a = list(range(10**5, 0, -1))
    #print(find(a, 6*10**4))

