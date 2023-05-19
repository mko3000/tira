from copy import deepcopy
 
class Download:
    def __init__(self,n):
        self.n = n
        self.network = [[0]*(n+1) for _ in range(n+1)]
        self.graph = deepcopy(self.network)        
 
    def add_link(self,a,b,x):
        self.network[a][b] += x
        self.graph = deepcopy(self.network)
 
    def print_graph(self,g):
        h = "   "
        for i in range(self.n+1):
            h += f'{i}  '
        print(h)
        print(f'  -{"---"*(self.n)}--')
        for line in range(self.n+1):
            print(line,g[line]) 
        print(f'  -{"---"*(self.n)}--')
      
    
    def calculate(self,a,b): 
        self.graph = deepcopy(self.network)
        self.print_graph(self.graph)
 
        max_flow = 0        
        while True:
            self.queue = []   
            path_flow = float("Inf") 
            self.path =[]
            found = self.leveyshaku(a,b)
 
            if not found:
                break
 
            for i in range(len(self.path)-1):
                #print(self.path[i],"-->" ,self.path[i+1], "flow:", self.graph[self.path[i]][self.path[i+1]])
                path_flow = min(path_flow,self.graph[self.path[i]][self.path[i+1]])
 
            if path_flow <= 0:
                break
            
            max_flow += path_flow
 
            for i in range(len(self.path)-1):
                self.graph[self.path[i]][self.path[i+1]] -= path_flow
                self.graph[self.path[i+1]][self.path[i]] += path_flow
 
        return max_flow
    
    
    def leveyshaku(self,a,b):
        seen = [False for _ in range(len(self.graph)+1)]
        self.queue.append(a)
        self.path.append(a)
        seen[a] = True
        while self.queue:
            node = self.queue.pop(0)
            for neighbour in range(len(self.graph[node])):                
                if self.graph[node][neighbour] > 0 and self.network[node][neighbour] > 0:
                    #print("node: ",node,", neighbour: ", neighbour, ", weight: ", self.graph[node][neighbour])
                    if seen[neighbour]:
                        continue
                    self.queue.append(neighbour)
                    if node not in self.path:
                        self.path.append(node)
                    seen[neighbour] = True
                    if neighbour == b:
                        self.path.append(neighbour)
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
    #print(d.calculate(2,3))
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
    print(d.calculate(4,5))
    d.add_link(5,3,8)
    print(d.calculate(5,2)) #jumittaa
    d.add_link(3,2,9)
    print(d.calculate(3,1))
    print(d.calculate(4,3))
    d.add_link(4,5,3)
    d.add_link(3,4,5)