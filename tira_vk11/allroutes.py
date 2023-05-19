class AllRoutes:
    def __init__(self,n):
        self.n = n
        self.roads = []
        self.table = [[-1 for x in range(n)] for y in range(n)]
        
 
    def add_road(self,a,b,x):
        self.roads.append((a,b,x))
        self.roads.append((b,a,x))
    
    #edellisen tehtävän malliratkaisusta
    def find_route(self,a,b):
        dist = [-1]*(self.n+1)
        dist[a] = 0
        while True:
            change = False
            for road in self.roads:
                if dist[road[0]] == -1:
                    continue
                new_dist = dist[road[0]]+road[2]
                if new_dist < dist[road[1]] or dist[road[1]] == -1:
                    change = True
                    dist[road[1]] = new_dist
            if not change:
                return dist[b]
    
    def get_table(self):
        for y in range(self.n):
            for x in range(y,self.n):
                if x == y:
                    self.table[y][x] = 0
                else:
                    dist = self.find_route(y+1,x+1)
                    self.table[y][x] = dist
                    self.table[x][y] = dist
        return self.table
    
if __name__ == "__main__":
    a = AllRoutes(4)
    a.add_road(1,2,2)
    a.add_road(1,3,5)
    a.add_road(2,3,1)
    print(a.get_table())
    # [[0, 2, 3, -1], [2, 0, 1, -1], [3, 1, 0, -1], [-1, -1, -1, 0]]
    # [[0, 2, 3, -1], [2, 0, 1, -1], [3, 1, 0, -1], [-1, -1, -1, 0]]

    #       1  2  3  4
    # 1   [ 0, 2, 3,-1]
    # 2   [ 2, 0, 1,-1]
    # 3   [ 3, 1, 0,-1]
    # 4   [-1,-1,-1, 0]