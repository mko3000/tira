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


def sums(t,a,b):
    if len(a)==len(t):
        if sum(a) == sum(b):
            return True
    else: 
        for i in t:
            pass
            #jäi kesken

def subgroups(subcodes, s, n):
    if len(s) == n:
        subcodes.append(s)
    else:
        subgroups(subcodes, s+"A", n)
        subgroups(subcodes, s+"B", n)

def check(t):
    subcodes = []
    subgroups(subcodes, "", len(t))
    #result = sums(t,[],[])
    for code in subcodes:
        a = 0
        b = 0
        for i in range(len(code)):
            if code[i] == "A":
                a += t[i]
            else:
                b += t[i]
        if a == b:
            return True
    return False
    #return subcodes

if __name__ == "__main__":
    print(check([3,4,5])) # False
    print(check([16,8,4,4])) # True
    print(check([9,4,8,7,6])) # True
    print(check([1,2,3,4,5,6])) # False
    print(check([1,2,3,4,5,6,7])) # True
    print(check([4,4,4,6,6])) # True


#valitaan yksi mahdollinen osajoukko, ja katsotaan onko osajoukko + jäljelle jäävät sama. 
#Lopetus, kun osajoukko sisältää koko joukon (ja jäljellä oleva joukko on tyhjä)

if __name__ == "__main__":
    #print(haku(0,3,[]))
    print(create(3))

