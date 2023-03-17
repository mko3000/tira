def create(n, k):
    bits = [0]*n
    bit = 0
    run = 1
    while run <= k:
        if bits[bit] == 0:
            bits[bit] = 1
            bit = 0
            run += 1            
        else: 
            bits[bit] = 0
            bit += 1
        if bit >= n:
            bit = 0
            run += 1    
    ans = ""
    for i in bits:
        ans += str(i)
    return ans


if __name__ == "__main__":
    print(create(5, 0)) # 00000
    print(create(5, 1)) # 10000
    print(create(5, 2)) # 01000
    print(create(5, 3)) # 11000
    print(create(5, 4)) # 00100
    print(create(5, 31)) # 11111
