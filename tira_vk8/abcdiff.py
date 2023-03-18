'''
Tehtäväsi on muodostaa lista, jossa on kaikki n merkin pituiset merkkijonot, 
joissa jokainen merkki on A, B tai C ja missään kohdassa ei ole vierekkäin kahta samaa merkkiä. 
Listan tulee olla aakkosjärjestyksessä.

Voit olettaa, että n on välillä 1…10
'''

def add(s,n):
    global result
    letters = "ABC"
    if len(s)==n:
        result.append(s)
    else:
        for l in letters:
            if len(s) == 0:
                add(s+l,n)
            elif s[-1]!=l:
                add(s+l,n)


def create(n):
    global result
    result = []
    add("",n)
    result.sort
    return result

if __name__ == "__main__":
    letters = "ABC"
    s = ""
    for l in letters:
        print(l)


    print(create(1)) # [A,B,C]
    print(create(2)) # [AB,AC,BA,BC,CA,CB]
    print(len(create(5))) # 48