

def haku(y,x,r,visited):
    if y < 1 or x < 1 or y > len(r) or x > len(r[0]):
        return
    if r[y][x] == "#" or visited[y][x]:
        return
    visited[y][x] = True
    haku(y+1,x,r,visited)
    haku(y-1,x,r,visited)
    haku(y,x+1,r,visited)
    haku(y,x-1,r,visited)

def count(r):
    visited = [[False]*len(r[0]) for _ in range(len(r))]
    rooms = 0
    for y in range(len(visited)-1):
        for x in range(len(visited[0])-1):
            if not visited[y][x]:
                haku(y,x,r,visited)
                if visited[y][x]:                    
                    rooms += 1
    return rooms

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3

