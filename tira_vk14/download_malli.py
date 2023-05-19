class Download:
    def __init__(self,n):
        self.n = n
        self.graph = [[0]*(self.n+1) for _ in range(self.n+1)]
 
    def add_link(self,a,b,x):
        self.graph[a][b] += x
 
    def add_flow(self,a,b,f):
        if self.seen[a]:
            return 0
        self.seen[a] = True
        if a == b:
            return f
        for x in range(1,self.n+1):
            if self.flow[a][x] > 0:
                inc = self.add_flow(x,b,min(f,self.flow[a][x]))
                if inc > 0:
                    self.flow[a][x] -= inc
                    self.flow[x][a] += inc
                    return inc
        return 0
 
    def calculate(self,a,b):
        self.flow = [row[:] for row in self.graph]
        total = 0
        while True:
            self.seen = [False]*(self.n+1)
            add = self.add_flow(a,b,float("inf"))
            if add == 0:
                break
            total += add
        return total
    
if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1,4)) # 0
    d.add_link(1,2,5)
    d.add_link(2,4,6)
    d.add_link(1,4,2)
    print(d.calculate(1,4)) # 7
    d.add_link(1,3,4)
    d.add_link(3,2,2)
    print(d.calculate(1,4)) # 8