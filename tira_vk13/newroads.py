class NewRoads:
    def __init__(self,n):
        self.n = n
        self.roads = []



    def add_road(self,a,b,w):
        self.roads.append((w,a,b))

    def find(self,x):
        while x != self.link[x]:
            x = self.link[x]
        return x

    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if self.size[a] < self.size[b]:
            a,b = b,a
        self.link[b] = a
        self.size[a] += self.size[b]

    def min_cost(self):
        self.link = {city:city for city in range(1,self.n+1)}
        self.size = {city:1 for city in range(1,self.n+1)} 

        cost = 0
        self.roads.sort()

        for road in self.roads:
            w, a, b = road
            a = self.find(a)
            b = self.find(b)
            if a != b:
                cost += w
                self.union(a,b)

        components = 0
        for city in self.link:
            if city == self.link[city]:
                components += 1
                if components > 1:
                    return -1
        
        return cost

if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1,2,2)
    n.add_road(1,3,5)
    print(n.min_cost()) # -1
    n.add_road(3,4,4)
    print(n.min_cost()) # 11
    n.add_road(2,3,1)
    print(n.min_cost()) # 7