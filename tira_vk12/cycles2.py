class Cycles:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n+1)]
        self.memory = {}

    def add_edge(self,a,b):
        self.graph[a].append(b)

    def check(self):
        print(self.graph)
        if self.self_cycle_search():
            return True
        self.loops = False
        self.travelled= set()
        self.visited = set()
        for node in range(len(self.graph)):

            self.cycle_search(node)
        #return cycles
        return self.loops

    
    def cycle_search(self, node):
        # print(self.visited)
        # print(self.travelled)
        if node in self.visited:
            self.loops = False
            #print(node,",",self.visited)
            return False
        self.visited.add(node)
        self.travelled.add(node)
        for neighbour in self.graph[node]:
            self.loops = False
            #print(neighbour,",",self.travelled)
            if neighbour in self.travelled or self.cycle_search(neighbour):
                #print("tosi")
                self.loops = True
                return True
        #print("epätosi")
        self.travelled.remove(node)
        return False

    def check2(self):
        if self.self_cycle_search():
            return True
        loops = False
        for node in range(len(self.graph)):
            self.travelled = {_:[] for _ in range(self.n+1)}
            self.visited = {_:False for _ in range(self.n+1)}
            loops = self.cycle_search(node)
        return loops
    
    def self_cycle_search(self):
        for node in range(len(self.graph)):
            if node in self.graph[node]:
                return True
            for neighbour in self.graph[node]:
                if node in self.graph[neighbour]:
                    return True
        return False

    def cycle_search2(self, node):
        self.visited[node] = True
        self.travelled[node] = True
        for neighbour in self.graph[node]:
            if not self.visited[neighbour]:
                if self.cycle_search(neighbour) == True:
                    return True
            elif self.travelled[neighbour]:
                return True
        self.travelled[node] = False
        return False

    def verkkokuva(self):
        verkko = self.graph
        tuloste = ""
        for solmu in range(len(verkko)):
            for i in range(len(verkko[solmu])):
                rivi = f'{solmu}-->{verkko[solmu][i]};\n'
                tuloste += rivi
        return tuloste


if __name__ == "__main__":

    # c = Cycles(5)
    # c.add_edge(1,2)
    # c.add_edge(4,1)
    # print(c.check())
    # c.add_edge(3,1)
    # c.add_edge(2,3)
    # print(c.check()) # True
    # print(c.check())
    # c.add_edge(2,4)
    # print(c.check()) 
    # c.add_edge(4,4)

    # c = Cycles(5)
    # print(c.check())
    # c.add_edge(3,4)
    # c.add_edge(4,3)
    # c.add_edge(4,1)
    # print(c.check()) # True
    # c.add_edge(3,1)
    # c.add_edge(4,2)
    # c.add_edge(2,1)
    # c.add_edge(5,5)
    # c.add_edge(4,5)


    c = Cycles(50)
    print(c.check())
    c.add_edge(27,39)
    print(c.check())
    print(c.check())
    print(c.check())
    c.add_edge(24,33)
    print(c.check())
    c.add_edge(10,44)
    print(c.check())
    c.add_edge(32,13)
    print(c.check())
    print(c.check())
    print(c.check())
    print(c.check())
    print(c.check())
    print(c.check())
    c.add_edge(22,8)
    print(c.check())
    c.add_edge(30,36)
    print(c.check())
    print(c.check())
    print(c.check())
    print(c.check())
    c.add_edge(27,18)
    c.add_edge(19,46)
    c.add_edge(18,34)
    print(c.check())
    c.add_edge(11,34)
    c.add_edge(41,15)
    c.add_edge(30,12)
    c.add_edge(32,2)
    print(c.check())
    c.add_edge(11,1)
    c.add_edge(28,2)
    c.add_edge(30,34)
    print(c.check())
    c.add_edge(24,31)
    c.add_edge(27,41)
    print(c.check())
    c.add_edge(21,18)
    c.add_edge(32,41)
    print(c.check())
    c.add_edge(47,25)
    print(c.check())
    print(c.check())
    c.add_edge(28,31)
    c.add_edge(5,12)
    c.add_edge(39,5)
    print(c.check())
    print(c.check())
    c.add_edge(19,31)
    print(c.check())
    print(c.check())
    print(c.check())
    c.add_edge(33,27)
    c.add_edge(2,45)
    c.add_edge(5,50)
    print(c.check())
    c.add_edge(17,46)
    c.add_edge(2,44)
    print(c.check())
    c.add_edge(15,42)
    c.add_edge(48,11)
    print(c.check())
    print(c.check())
    c.add_edge(23,7)
    c.add_edge(17,18)
    print(c.check())
    c.add_edge(23,5)
    print(c.check())
    print(c.check())
    print(c.check())
    c.add_edge(22,23)
    print(c.check())
    c.add_edge(8,4)
    print(c.check())
    c.add_edge(14,37)
    print(c.check())
    c.add_edge(47,49)
    c.add_edge(27,29)
    c.add_edge(20,48)
    c.add_edge(47,17)
    c.add_edge(7,47)
    print(c.check())
    c.add_edge(21,37)
    print(c.check())
    c.add_edge(44,31)
    print(c.check())
    c.add_edge(5,37)
    c.add_edge(44,20)
    print(c.check())
    c.add_edge(40,43)
    print(c.check())
    print(c.check())
    c.add_edge(41,46)
    c.add_edge(20,3)
    c.add_edge(17,23)
    c.add_edge(34,4)
    c.add_edge(39,10)
    print(c.check()) #True
    print(c.verkkokuva())