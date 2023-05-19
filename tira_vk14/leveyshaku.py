from copy import deepcopy

class Network:
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
            print(line,self.network[line]) 
        print(f'  -{"---"*(self.n)}--')

    def best_route(self,a,b):
        self.print_graph(self.network)
        self.path =set()
        self.queue = []
        self.dist = [-1 for _ in range(len(self.network)+1)]
        self.seen = [False for _ in range(len(self.network)+1)]
        self.leveyshaku(a)
        print("path:",self.path, ", dist:", self.dist)
        return self.dist[b]

    def leveyshaku(self,a):
        self.queue.append(a)
        self.path.add(a)
        self.seen[a] = True
        self.dist[a] = 0
        while self.queue:
            node = self.queue.pop(0)
            for neighbour in range(len(self.network[node])):
                #print("node: ",node,", neighbour: ", neighbour, ", weight: ", self.network[node][neighbour])
                if self.network[node][neighbour] > 0 and not self.seen[neighbour]:
                    self.queue.append(neighbour)
                    self.path.add(node)
                    self.seen[neighbour] = True
                    self.dist[neighbour] = self.dist[node]+1

if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2,1)
    w.add_link(2,3,1)
    w.add_link(1,3,1)
    w.add_link(4,5,1)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5,1)
    print(w.best_route(1,5)) # 2

    d=Network(5)
    d.add_link(1,3,4)
    d.add_link(1,2,3)
    d.add_link(2,4,8)
    d.add_link(3,4,2)
    d.add_link(4,5,3)
    print(d.best_route(1,5)) 
    #d.test()