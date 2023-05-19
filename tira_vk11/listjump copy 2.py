import heapq
from typing import List, Tuple

def luo_hyppyverkko(lista):
    verkko = {}
    for n in range(len(lista)):
        verkko[n] = []
    for i in range(len(lista)):        
        if i + lista[i] < len(lista):
            verkko[i].append((i + lista[i], lista[i])) 
        if i - lista[i] >= 0 and i > 0:
            verkko[i].append((i - lista[i], lista[i]))

    #print(verkko)
    return verkko



def calculate(t):
    verkko = luo_hyppyverkko(t)
    #shortest_path_length = dijkstra(verkko, 0, len(t)-1)
    etaisyydet = dijkstra(verkko)
    return etaisyydet[len(t)-1]

def dijkstra_ai(graph, start, end):
    # Initialize distances to infinity and the start vertex to 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Initialize the priority queue with the start vertex
    pq = [(0, start)]
    
    # Initialize the list of visited vertices
    visited = set()
    
    # Dijkstra's algorithm
    while pq:
        # Get the vertex with the smallest distance from the start
        current_distance, current_vertex = heapq.heappop(pq)
        
        # If we've already visited this vertex, skip it
        if current_vertex in visited:
            continue
        
        # Otherwise, mark it as visited
        visited.add(current_vertex)
        
        # If we've reached the end vertex, return its distance
        if current_vertex == end:
            return distances[end]
        
        # Update the distances to each neighbor of the current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    # If we've searched the entire graph and haven't found the end vertex, return -1
    return -1

def dijkstra_clean(graph, start, end):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        if current_vertex == end:
            return distances[end]
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return -1

def dijkstra(verkko):
    n = len(verkko)
    alku = 0
    etaisyydet = {solmu: float('inf') for solmu in verkko}
    etaisyydet[alku] = 0
    keko = [(0, alku)]
    kasitelty = set()
    while keko:
        print("käsitelty",kasitelty)
        print(keko)
        nyky, uusi = heapq.heappop(keko)
        print("nyky",nyky,"uusi",uusi)
        if uusi in kasitelty:
            continue
        kasitelty.add(uusi)
        for naapuri, paino in verkko[uusi]:
            etaisyys = nyky + paino
            if etaisyys < etaisyydet[naapuri]:
                etaisyydet[naapuri] = etaisyys
                heapq.heappush(keko, (etaisyys, naapuri))
    return etaisyydet

def dijkstra2(verkko, alku, loppu):
    n = len(verkko)
    etaisyys = [float("Inf")] * n
    kasitelty = [False] * n
    vanhempi = [-1] * n
    etaisyys[alku] = 0
    keko = []
    keko.append((0,alku))

    while keko:
        solmu = keko.pop()[1]
        if kasitelty[solmu]:
            continue
        kasitelty[solmu] = True
        for kaari in verkko[solmu]:
            nyky = etaisyys[kaari[0]]
            uusi = etaisyys[solmu]+kaari[1]
            if uusi < nyky:
                etaisyys[kaari[0]] = uusi
                vanhempi[kaari[0]] = solmu
                keko.append((uusi,kaari[0]))
                
    if etaisyys[loppu] == float("Inf"):
        return []
    path = [loppu]
    while path[-1] != alku:
        path.append(vanhempi[path[-1]])
    path.reverse()
    return path

def dijkstra_toimiva(verkko, alku, loppu):
    n = len(verkko)
    etaisyydet = {solmu: float('inf') for solmu in verkko}
    print(etaisyydet)
    etaisyydet[alku] = 0
    keko = [(0, alku)]
    kasitelty = set()
    while keko:
        print(keko)
        nyky, uusi = heapq.heappop(keko)
        if uusi in kasitelty:
            continue
        kasitelty.add(uusi)
        if uusi == loppu:
            return etaisyydet[loppu]
        for naapuri, paino in verkko[uusi]:
            etaisyys = nyky + paino
            if etaisyys < etaisyydet[naapuri]:
                etaisyydet[naapuri] = etaisyys
                heapq.heappush(keko, (etaisyys, naapuri))
    return -1

if __name__ == "__main__":

    print(calculate([1,1,1,1])) # 3
    print(calculate([3,2,1])) # -1
    print(calculate([3,5,2,2,2,3,5])) # 10
    print(calculate([7,5,3,1,4,2,4,6,1])) # 32
    print(calculate([2, 7, 1, 3, 2, 1, 3, 9, 4, 9])) # 9
