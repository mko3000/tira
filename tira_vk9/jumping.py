def count(n,a,b):
    result = [0]*(n+1)
    result[0] = 1
    for i in range(1,n+1):
        if i >= a:
            result[i] += result[i-a]
        if i >= b:
            result[i] += result[i-b]
    return result[-1]

if __name__ == "__main__":
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(30,3,5)) # 58
    print(count(50,2,3)) # 525456