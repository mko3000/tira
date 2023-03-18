def haku(k,n,sana):
    if k == n:
        return 
    else:
        sana[k]=0
        haku(k+1)
        sana[k]=1
        haku(k+1)

def create(n):
    if n == 1:
        return [[1],[0]]
    else:
        old = create(n-1)
        new = [[]]
        for i in old:
            new.append(i.append(1))
            new.append(i.append(0))
        return new


if __name__ == "__main__":
    #print(haku(0,3,[]))
    print(create(3))


