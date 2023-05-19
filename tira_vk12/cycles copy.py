class Cycles:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n+1)]
        self.memory = {}

    def add_edge(self,a,b):
        self.graph[a].append(b)

    def check(self):
        visited = [False] * (self.n+1)
        stack = [False] * (self.n+1)

        for node in range(1, self.n+1):
            if not visited[node]:
                if self.dfs(node, visited, stack, self.graph):
                    return True
        return False

    def dfs(self, node, visited, stack, graph):
        visited[node] = True
        stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor, visited, stack, graph):
                    return True
            elif stack[neighbor]:
                return True

        stack[node] = False
        return False
    
    def cycle_search(self, node):
        pass

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