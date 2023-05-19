class LongPath:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n+1)]

    def add_edge(self,a,b):
        # self.graph[a].append(b)
        # self.graph[b].append(a)
        self.graph[min(a,b)].append(max(a,b))

    def calculate(self):
        self.visited = [0]*(self.n + 1)
        self.length = {}
        self.follower = {}
        for node in range(self.n):
            if self.visited[node] == 0:
                self.longdepth(node)
        if not self.length:
            return 0
        return max(list(self.length.values()))


    def longdepth(self, node):
        self.visited[node] = 1
        self.length[node] = 0
        self.follower[node] = None
        for neighbour in self.graph[node]:
            if self.visited[neighbour] == 1:
                print("looping")
                return
            elif self.visited[neighbour] == 0:
                self.longdepth(neighbour)
            new = self.length[neighbour] + 1
            if new > self.length[node]:
                self.length[node] = new
                self.follower[node] = neighbour
        self.visited[node] = 2




if __name__ == "__main__":
    l = LongPath(5)
    l.add_edge(4,3)
    print(l.calculate())
    l.add_edge(5,4)
    l.add_edge(2,3)
    print(l.calculate())
    l.add_edge(1,4)
    print(l.calculate()) #3 --> vika siinä, että aletaan haut 1:sta, vaikka siitä pääsee vaan 4:aan. Pitäisi hakea kaikista, ja palauttaa isoin
    l.add_edge(5,3)
    l.add_edge(4,5)
    print(l.calculate())

    # l = LongPath(4)
    # l.add_edge(1,2)
    # l.add_edge(1,3)
    # l.add_edge(2,4)
    # l.add_edge(3,4)
    # print(l.calculate()) # 2
    # l.add_edge(3,2)
    # print(l.calculate()) # 3
    # # 
    # l = LongPath(5)
    # print(l.calculate())
    # l.add_edge(3,5)
    # print(l.calculate())
    # print(l.calculate())
    # l.add_edge(3,4)
    # print(l.calculate())
    # l.add_edge(5,4)
    # l.add_edge(1,2)
    # l.add_edge(3,1)
    # print(l.calculate())