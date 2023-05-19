import time

class MaxSet:
    def __init__(self,n):
        self.n = n
        self.link = {x:x for x in range(1,self.n+1)} #O(n)
        self.size = {x:1 for x in range(1,self.n+1)} #O(n)
        self.components = {}
        self.biggest = 1

    def get_max(self):
        return self.biggest

    def same(self,a,b):
        return self.find(a) == self.find(b)
    
    def find(self,x):
        # Pidetään kirjaa, mitkä kaikki solut on nähty.
        # Käytetään set(), ettei tule samaa kahteen kertaan.
        # len(visited) ei ole koskaan > 2, koska kaaria lisätään yksitellen 
        #   ja kaari on aina oikaistu näyttämään komponentin edustajaa
        visited = set() 
        visited.add(x)
        while x != self.link[x]:
            visited.add(x)
            x = self.link[x] 
        if x not in self.components.keys(): #Aikavaativuus pahimmillaan O(n/2), jos kaikki solut on kahden solun komponenteissa
            self.components[x] = set()
        for i in visited: #lisätään nähdyt solut (max 2 kpl) komponenttiin x
            self.components[x].add(i)
        return x

    def merge(self,a,b):
        a = self.find(a) 
        b = self.find(b) 
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a,b = b,a

        #laitetaan kaikki komponentin b solmut osoittamaan suoraan edustajaa a ja siirretään ne komponenttiin a
        #   Silmukan aikavaativuus O(n) 
        #   Tässä läpikäytävään komponenttiin voi kuulua enimmillään alle puolet verkon soluista
        for i in self.components[b]: 
            self.components[a].add(i) #O(1)
            self.link[i] = a  #O(1)     
        self.components.pop(b)        
        
        self.size[a] += self.size[b]
        self.biggest = max(self.size[a],self.biggest)

if __name__ == "__main__":

    
    alkuaika = time.time()
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1,2)
    m.merge(3,4)
    m.merge(3,5)
    print(m.get_max()) # 3
    m.merge(1,5)
    print(m.get_max()) # 5
    loppuaika = time.time()
    print(loppuaika-alkuaika)
    
    alkuaika = time.time()
    m = MaxSet(100000)
    m.merge(73846,95230)
    m.merge(65689,91281)
    print(m.get_max())
    m.merge(56793,63652)
    m.merge(54686,67495)
    m.merge(46393,62264)
    m.merge(80760,96970)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(91852,98254)
    m.merge(69907,74715)
    m.merge(91092,91882)
    print(m.get_max())
    m.merge(41193,70278)
    print(m.get_max())
    m.merge(4474,49377)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(58372,93525)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(15274,92644)
    m.merge(1733,22362)
    m.merge(40269,70325)
    m.merge(88469,91735)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(13142,84949)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(80264,88691)
    m.merge(45648,55883)
    m.merge(52198,90801)
    print(m.get_max())
    m.merge(38246,91212)
    m.merge(98587,99083)
    m.merge(82946,92201)
    m.merge(26088,51679)
    print(m.get_max())
    print(m.get_max())
    m.merge(23272,25808)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(74161,97911)
    print(m.get_max())
    m.merge(874,49821)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(49359,69736)
    m.merge(2262,82351)
    print(m.get_max())
    m.merge(14065,38027)
    print(m.get_max())
    print(m.get_max())
    m.merge(99253,99731)
    print(m.get_max())
    m.merge(73053,76582)
    print(m.get_max())
    m.merge(53476,71491)
    m.merge(53513,60286)
    m.merge(20962,48423)
    print(m.get_max())
    print(m.get_max())
    m.merge(67072,75995)
    m.merge(4328,80126)
    m.merge(77744,78417)
    print(m.get_max())
    m.merge(76121,93753)
    print(m.get_max())
    m.merge(77708,95007)
    m.merge(97693,98661)
    m.merge(67975,95602)
    print(m.get_max())
    print(m.get_max())
    m.merge(45715,45987)
    print(m.get_max())
    m.merge(59374,62955)
    print(m.get_max())
    m.merge(25763,55654)
    m.merge(43317,75375)
    m.merge(69730,87799)

    loppuaika = time.time()

    print(loppuaika-alkuaika)