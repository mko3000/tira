class Topologinen:
    def __init__(self,n):
        self.n = n
        self.verkko = [[] for _ in range(n+1)]
        self.verkko[1].append(2)
        self.verkko[4].append(1)
        self.verkko[3].append(1)
        self.verkko[2].append(3)

    def topologinen_jarjestys(self):
        self.kasitelty = [0]*self.n
        self.jarjestys = []
        for solmu in range(self.n):
            if self.kasitelty[solmu] == 0:
                self.syvyyshaku(solmu)
        self.jarjestys.reverse()
        return self.jarjestys[:len(self.jarjestys)-1]
        
    def syvyyshaku(self,alku):
        self.kasitelty[alku] = 1
        for naapuri in self.verkko[alku]:
            if self.kasitelty[naapuri] == 1:
                print("Verkossa on sykli")
                return []
            elif self.kasitelty[naapuri] == 0:
                self.syvyyshaku(naapuri)
        self.kasitelty[alku] = 2
        self.jarjestys.append(alku)


if __name__ == "__main__":
    t = Topologinen(5)
    print(t.topologinen_jarjestys())
