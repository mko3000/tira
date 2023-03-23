
def find(t):
    mem = [1]*len(t)
    for i in range(1,len(t)):
        for j in range(i):
            if abs(t[i]-t[j]) <= 1:
                mem[i] = max(mem[i],mem[j]+1)
    return max(mem)   


if __name__ == "__main__":

    print(find([4, 1, 7, 4, 7, 6, 9, 8, 8, 4])) #4
    print(find([7, 4, 6, 2, 7, 7, 2, 9, 6, 7])) #6
    print(find([1,2,3,4,5])) # 5
    print(find([5,5,5,5,5])) # 5
    print(find([5,2,3,8,2,4,1])) # 4
    print(find([1,3,5,7,9])) # 1