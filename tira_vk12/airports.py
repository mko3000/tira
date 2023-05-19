class Airports:
    def __init__(self,n):
        self.n = n
        self.airports = [[] for _ in range(n+1)]

    def add_link(self,a,b):
        self.airports[a].append(b)
        

    def check(self):
        for airport in range(1,self.n):
            self.visited = [False]*(self.n + 1)
            self.dfs(airport)
            if self.visited.count(True) != self.n:
                return False
        return True

    def dfs(self, port):
        if self.visited[port]:
            return
        self.visited[port] = True
        for destination in self.airports[port]:
            self.dfs(destination)




if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1,2)
    a.add_link(2,3)
    a.add_link(1,3)
    a.add_link(4,5)
    print(a.check()) # False
    a.add_link(3,5)
    a.add_link(1,4)

    print(a.check()) # False
    a.add_link(5,1)

    print(a.check()) # True