def find(t, k):    
    max_distance = 0
    t.sort()
    for i in range(len(t)-1):
        max_distance = max(max_distance, t[i+1] - t[i])
    return max (max_distance//2, t[0]-1, k-t[len(t)-1])
    

if __name__ == "__main__":
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970
    print(find([15, 9, 12, 6, 10], 15)) #5
    print(find([7, 12, 4], 15)) #3   
    print(find([2, 11, 9, 10, 10], 15)) #4

