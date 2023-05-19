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
        r =  self.FordFulkerson(a,b)

        return r

    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        visited = [False]*(self.n+1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # If we find a connection to the sink node,
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 
        # We didn't reach sink in BFS starting
        # from source, so return false
        return False
             
     
    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.n+1)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                #print(path_flow)
                print(parent)
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow

  

if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1,4)) # 0
    d.add_link(1,2,5)
    d.add_link(2,4,6)
    d.add_link(1,4,2)
    print(d.calculate(1,4)) # 7
    d.add_link(1,3,4)
    d.add_link(3,2,2)
    print(d.calculate(1,4)) # 8


    d = Download(5)
    print(d.calculate(2,3))
    d.add_link(2,5,6)
    d.add_link(1,2,8)
    print(d.calculate(1,2))
    d.add_link(4,5,1)
    d.add_link(4,2,6)
    d.add_link(5,4,5)
    print(d.calculate(4,2))
    d.add_link(4,5,1)
    print(d.calculate(3,2))
    d.add_link(3,1,5)
    d.add_link(2,4,4)
    d.add_link(3,5,8)
    print(d.calculate(4,5))
    print(d.calculate(4,3))
    d.add_link(5,3,7)
    d.add_link(3,2,2)
    d.add_link(3,5,6)
    d.add_link(2,4,3)
    print(d.calculate(3,2))
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

# graph = [[0, 16, 13, 0, 0, 0],
#         [0, 0, 10, 12, 0, 0],
#         [0, 4, 0, 0, 14, 0],
#         [0, 0, 9, 0, 0, 20],
#         [0, 0, 0, 7, 0, 4],
#         [0, 0, 0, 0, 0, 0]]
 
# g = Graph(graph)
 
# source = 0; sink = 5
  
# print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
 
# # This code is contributed by Neelam Yadav