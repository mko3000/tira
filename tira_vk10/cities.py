class Cities:
    def __init__(self,n):
        self.kaupungit = {}
        self.vierailtu = {}
        for k in range(1, n+1):
            self.kaupungit[k]=[]
            self.vierailtu[k]=False
 
    def syvyyshaku(self,kaupunki):
        if self.vierailtu[kaupunki]:
            return
        self.vierailtu[kaupunki] = True
        for naapuri in self.kaupungit[kaupunki]:
            self.syvyyshaku(naapuri)    

    def add_road(self,a,b):
        self.kaupungit[a].append(b)
        self.kaupungit[b].append(a)

    def has_route(self,a,b):
        self.vierailtu = {k: False for k in self.vierailtu} #kaikki kaupungit palautetaan vierailemattomiksi ennen hakua
        self.syvyyshaku(a)
        return self.vierailtu[b]
        

if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.kaupungit)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)

    print(c.kaupungit)
    print(c.has_route(1,5)) # True