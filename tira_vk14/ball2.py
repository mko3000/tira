from copy import deepcopy

class Ball:
    def __init__(self,n):
        self.n = n
        self.guests = [[0]*(2*n+2) for _ in range(2*n+2)]
        for x in range(1,n+1):
            self.guests[0][x] = 1
            self.guests[n+x][2*n+1] = 1
        self.graph = deepcopy(self.guests)   
    
    def add_pair(self,a,b):
        #a = Kumpula
        #b = Viikki
        self.guests[a][b+self.n] = 1
        self.graph = deepcopy(self.guests)
        pass

    def print_graph(self,g):
        h = "   "
        for i in range(len(g)):
            h += f'{i}  '
        print(h)
        print(f'  -{"---"*(len(g)+1)}--')
        for line in range(len(g)):
            print(line,g[line]) 
        print(f'  -{"---"*(len(g)+1)}--')

    def calculate(self):
        self.graph = deepcopy(self.guests)
        self.print_graph(self.graph)

        a=0
        b=2*self.n+1
        
        self.path = [-1]*(2*self.n+2)
        max_flow = 0
        cut = 0

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
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1,2)
    print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2

    # print()
    
    # b = Ball(5)
    # #print(b.calculate())
    # b.add_pair(5,5)
    # #print(b.calculate())
    # b.add_pair(3,4)
    # #print(b.calculate())
    # #print(b.calculate())
    # #print(b.calculate())
    # b.add_pair(1,3)
    # b.add_pair(4,2)
    # #print(b.calculate())
    # b.add_pair(5,3)
    # b.add_pair(5,1)
    # b.add_pair(1,4)
    # b.add_pair(1,2)
    # b.add_pair(1,3)
    # #print(b.calculate())
    # #print(b.calculate())
    # b.add_pair(4,5)
    # #print(b.calculate())
    # b.add_pair(2,5)
    # b.add_pair(5,5)
    # print(b.calculate()) #5
    # # print(b.calculate())
    # # print(b.calculate())
    # # b.add_pair(3,1)
    # # print(b.calculate())
    # # print(b.calculate())
    # # b.add_pair(5,3)
    # # print(b.calculate())
    # # b.add_pair(3,5)

    # b = Ball(50)
    # b.add_pair(31,7)
    # b.add_pair(15,46)
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(26,13)
    # b.add_pair(37,22)
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(21,2)
    # b.add_pair(49,40)
    # b.add_pair(7,9)
    # b.add_pair(10,40)
    # b.add_pair(26,3)
    # b.add_pair(31,2)
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(30,25)
    # b.add_pair(35,50)
    # b.add_pair(17,50)
    # print(b.calculate())
    # b.add_pair(25,30)
    # b.add_pair(48,24)
    # print(b.calculate())
    # b.add_pair(40,8)
    # b.add_pair(43,5)
    # print(b.calculate())
    # b.add_pair(3,42)
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(18,17)
    # print(b.calculate())
    # b.add_pair(22,43)
    # b.add_pair(11,33)
    # b.add_pair(50,18)
    # b.add_pair(6,10)
    # b.add_pair(30,9)
    # b.add_pair(50,34)
    # print(b.calculate())
    # b.add_pair(9,50)
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(38,20)
    # b.add_pair(32,34)
    # print(b.calculate())
    # b.add_pair(44,16)
    # b.add_pair(18,37)
    # b.add_pair(32,43)
    # print(b.calculate())
    # b.add_pair(48,49)
    # print(b.calculate())
    # b.add_pair(26,6)
    # print(b.calculate())
    # b.add_pair(7,19)
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(9,17)
    # b.add_pair(28,37)
    # b.add_pair(50,17)
    # b.add_pair(6,4)
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(15,16)
    # b.add_pair(35,46)
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(37,36)
    # b.add_pair(33,8)
    # b.add_pair(6,5)
    # print(b.calculate())
    # b.add_pair(23,8)
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(50,50)
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(40,34)
    # b.add_pair(31,9)
    # b.add_pair(19,45)
    # b.add_pair(25,39)
    # b.add_pair(35,1)
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(4,32)
    # print(b.calculate())
    # b.add_pair(15,20)
    # print(b.calculate())
