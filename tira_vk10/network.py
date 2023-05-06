class Network:
    def __init__(self,n):
        self.network = [[] for _ in range(n+1)] #katsoin tämän syntaksin edellisen tehtävän malliratkaisusta

    def add_link(self,a,b):
        self.network[a].append(b)
        self.network[b].append(a)

    def best_route(self,a,b):
        self.queue = []
        self.dist = [-1 for _ in range(len(self.network)+1)]
        self.seen = [False for _ in range(len(self.network)+1)]
        self.leveyshaku(a)
        return self.dist[b]

    def leveyshaku(self,start):
        self.queue.append(start)
        self.seen[start] = True
        self.dist[start] = 0
        while len(self.queue) != 0:
            node = self.queue.pop(0)
            for neighbour in self.network[node]:
                if self.seen[neighbour]:
                    continue
                self.queue.append(neighbour)
                self.seen[neighbour] = True
                self.dist[neighbour] = self.dist[node]+1

if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2

   