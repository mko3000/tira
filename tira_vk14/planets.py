from copy import deepcopy

class Planets:
    def __init__(self,n):
        self.n = n
        self.planets = [[0]*(n+1) for _ in range(n+1)]
        self.graph = deepcopy(self.planets)

    def add_teleport(self,a,b):
        self.planets[min(a,b)][max(a,b)] += 1
        self.graph = deepcopy(self.planets)

    def calculate(self): 
        a = 1
        b = self.n
        self.graph = deepcopy(self.planets)        
        self.path = [-1]*(self.n+1)
        cut = 0
        while self.leveyshaku(a,b) : 
            
            path_flow = float("Inf")
            s = b
            while(s != a):
                path_flow = min (path_flow, self.graph[self.path[s]][s])
                s = self.path[s]

            cut += path_flow

            v = b
            while(v != a):
                u = self.path[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = self.path[v]  

        return cut

    def leveyshaku(self,a,b):
        queue = []
        seen = [False for _ in range(len(self.graph)+1)]
        queue.append(a)
        seen[a] = True
        while queue:
            node = queue.pop(0)
            for neighbour in range(len(self.graph[node])):     
                if self.graph[node][neighbour] > 0 and not seen[neighbour]:
                    queue.append(neighbour)
                    seen[neighbour] = True
                    self.path[neighbour] = node
                    if neighbour == b:
                        return True
        return False
    
    

if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate()) # 0
    p.add_teleport(1,2)
    p.add_teleport(2,5)
    print(p.calculate()) # 1
    p.add_teleport(1,5)
    print(p.calculate()) # 2

    print()
    p = Planets(3)
    print(p.calculate())
    p.add_teleport(1,3)
    p.add_teleport(2,3)
    print(p.calculate())
    print(p.calculate())
    print(p.calculate())
    print(p.calculate())
    p.add_teleport(1,3)
    print(p.calculate()) #2
    p.add_teleport(1,3)
