class Components:
    def __init__(self,n):
        self.n = n
        self.vanhempi = {city:city for city in range(1,n+1)}  
        self.koko = {city:1 for city in range(1,n+1)}     

    def add_road(self,a,b):
        # for i in [a,b]:
        #     if i not in self.vanhempi.keys():
        #         self.vanhempi[i] = i
        #         self.koko[i] = 1
        if not self.sama(a,b):
            self.yhdista(a,b)

    def count(self):
        print(self.vanhempi)
        count = 0
        for c in self.vanhempi:
            if c == self.vanhempi[c]:
                count +=1
        return count

    def edustaja(self,x):
        while x != self.vanhempi[x]:
            x = self.vanhempi[x]
        return x
    
    def sama(self,a,b):
        return self.edustaja(a) == self.edustaja(b)
    
    def yhdista(self,a,b):
        a = self.edustaja(a)
        b = self.edustaja(b)
        if self.koko[a] < self.koko[b]:
            a,b = b,a
        self.vanhempi[b] = a
        self.koko[a] += self.koko[b]


if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1,2)
    c.add_road(1,3)
    print(c.count()) # 3
    c.add_road(2,3)
    print(c.count()) # 3
    c.add_road(4,5)
    print(c.count()) # 2


    vanhempi = {}
    # 1--2--4
    #  \
    #  3
    vanhempi[3] = 1
    vanhempi[4] = 2
    vanhempi[2] = 1