class BestRoute:
    def __init__(self,n):
        self.bitland = [[] for _ in range(n)]
        self.n = n

    def add_road(self,a,b,x):
        if a > self.n or b > self.n:
            print("too many cities")
            return
        for i in range(len(self.bitland)):
            if self.bitland[i]['a'] == a and self.bitland[i]['b'] == b:
                x = min(self.bitland[i]['dist'],x)
                self.bitland[i] = {'a':a,'b':b,'dist':x}
            if self.bitland[i]['a'] == b and self.bitland[i]['b'] == a:
                self.bitland[i] = {'a':b,'b':a,'dist':x}
                #print("road updated",self.bitland[i])
                return
        self.bitland.append({'a':a,'b':b,'dist':x})
        self.bitland.append({'a':b,'b':a,'dist':x})

    def find_route(self,a,b):
        distance = [float("Inf")] * (self.n+1)
        distance[a] = 0
        #print(self.bitland)
        while True:
            change = False
            for road in self.bitland:
                current = distance[road['b']]
                new = distance[road['a']]+road['dist']
                if new < current:
                    distance[road['b']] = new
                    change = True
            if not change:
                break
        
        if distance[b] > 1000*self.n:
            return -1
        return distance[b]


if __name__ == "__main__":


    b = BestRoute(5)
    b.add_road(4,5,6)
    b.add_road(3,5,8)
    b.add_road(2,3,1)
    print(b.find_route(1,4))
    b.add_road(3,5,5)
    print(b.find_route(3,5)) #5
    b.add_road(2,5,2)
    b.add_road(2,4,8)
    b.add_road(1,5,9)
    b.add_road(2,4,9)



