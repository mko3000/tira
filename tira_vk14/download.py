from copy import deepcopy

class Download:
    def __init__(self,n):
        self.n = n
        self.network = [[0]*(n+1) for _ in range(n+1)]
        self.graph = deepcopy(self.network)        

    def add_link(self,a,b,x):
        self.network[a][b] += x
        self.graph = deepcopy(self.network)


    def calculate(self,a,b): 
        self.graph = deepcopy(self.network)
        
        self.path = [-1]*(self.n+1)
        max_flow = 0

        while self.leveyshaku(a,b) : 
            path_flow = float("Inf")
            s = b
            while(s != a):
                path_flow = min (path_flow, self.graph[self.path[s]][s])
                s = self.path[s]
 
            max_flow +=  path_flow

            v = b
            while(v != a):
                u = self.path[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = self.path[v]  

        return max_flow
    
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
    # d = Download(4)
    # print(d.calculate(1,4)) # 0
    # d.add_link(1,2,5)
    # d.add_link(2,4,6)
    # d.add_link(1,4,2)
    # print(d.calculate(1,4)) # 7
    # d.add_link(1,3,4)
    # d.add_link(3,2,2)
    # print(d.calculate(1,4)) # 8

    # d=Download(5)
    # print(d.calculate(1,5))
    # d.add_link(1,3,4)
    # d.add_link(1,2,3)
    # d.add_link(2,4,8)
    # d.add_link(3,4,2)
    # d.add_link(4,5,3)
    # print(d.calculate(1,5))
    # #print(d.best_route(1,4))

    # d = Download(5)
    # print(d.calculate(3,4))
    # d.add_link(5,3,6)
    # print(d.calculate(5,4))
    # print(d.calculate(4,5))
    # print(d.calculate(5,1))
    # d.add_link(5,4,9)
    # d.add_link(1,2,10)
    # print(d.calculate(3,1))
    # print(d.calculate(2,4))
    # print(d.calculate(5,4))
    # d.add_link(5,2,9)
    # print(d.calculate(1,5))
    # d.add_link(3,5,2)
    # d.add_link(1,3,2)
    # d.add_link(5,4,9)
    # print(d.calculate(5,4)) #18
    # print(d.calculate(2,3)) 
    # print(d.calculate(1,3))
    # print(d.calculate(3,2))
    # print(d.calculate(5,4)) #18
    # print(d.calculate(4,5))
    # d.add_link(4,3,9)
    # print(d.calculate(4,5))
    # print(d.calculate(2,4))
    # print(d.calculate(4,5))
    # d.add_link(5,1,6)
    # d.add_link(3,5,3)
    # d.add_link(4,5,2)
    # print(d.calculate(3,4))
    # d.add_link(5,3,3)

   
    d = Download(5)
    print(d.calculate(2,3))
    d.add_link(2,5,6)
    d.add_link(1,2,8)
    #print(d.calculate(1,2))
    d.add_link(4,5,1)
    d.add_link(4,2,6)
    d.add_link(5,4,5)
    #print(d.calculate(4,2))
    d.add_link(4,5,1)
    #print(d.calculate(3,2))
    d.add_link(3,1,5)
    d.add_link(2,4,4)
    d.add_link(3,5,8)
    #print(d.calculate(4,5))
    #print(d.calculate(4,3))
    d.add_link(5,3,7)
    d.add_link(3,2,2)
    d.add_link(3,5,6)
    d.add_link(2,4,3)
    #print(d.calculate(3,2))
    d.add_link(5,1,6)
    d.add_link(4,5,10)
    #print(d.calculate(4,5))
    d.add_link(5,3,8)    
    print(d.calculate(5,2)) #15
    print("^pitäis tulla 15")
    d.add_link(3,2,9)
    #print(d.calculate(3,1))
    #print(d.calculate(4,3))
    d.add_link(4,5,3)
    #d.add_link(3,4,5)

