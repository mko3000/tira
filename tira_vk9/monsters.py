def routeCount(r):
    # tässä lasketaan vaan reitit eikä välitetä hirviöistä
    n = len(r)
    routes = [[0]*n for _ in range(n)]
    if r[0][0] == "#" or r[n][n] == "#":
        return -1
    for y in range(n):
        for x in range(n):
            if x == 0 and y == 0:
                routes[y][x] = 1
            elif r[y][x] == "#":
                routes[y][x] = 0
            else:
                routes[y][x] = routes[y-1][x] + routes[y][x-1]
    return routes

# this counts the number of monsters on the route
def count(r):
    n = len(r)
    monsters = [[0]*n for _ in range(n)]
    if r[0][0] == "@":
        monsters[0][0] = 1
    for y in range(n):
        for x in range(n):
            if x == 0 and y == 0 and r[x][y] == "@":
                monsters[y][x] = 1
            elif r[y][x] == ".":
                if y == 0:
                    monsters[y][x] = min(2*n, monsters[y][x-1])
                elif x == 0:
                    monsters[y][x] = min(monsters[y-1][x], 2*n)
                else:
                    monsters[y][x] = min(monsters[y-1][x], monsters[y][x-1])
            elif r[y][x] == "@":
                if y == 0:
                    monsters[y][x] = min(2*n, monsters[y][x-1])+1
                elif x == 0:
                    monsters[y][x] = min(monsters[y-1][x], 2*n)+1
                else:
                    monsters[y][x] = min(monsters[y-1][x], monsters[y][x-1])+1
            elif r[y][x] == "#":
                monsters[y][x] = 2*n #reitillä voi olla maksimissaan 2*n-1 hirviötä, joten laitetaan esteen kustannukseksi tätä isompi luku
    if monsters[-1][-1] >= 2*n:
        return -1
    return monsters[-1][-1]

if __name__ == "__main__":
    r = ["....@",
         "@##.#",
         ".##@#",
         ".@..#",
         "###@."]
    print(count(r)) # 2

    m = ["@..@#",
         ".@@@@",
         "@.@#@",
         "..#..",
         "@@.@."]
    print(count(m)) # 4

    f = ["#@.@#",
         "@...@",
         "@@@##",
         "@#@@@",
         "@.#@@"]
    print(routeCount(f)) # -1
    print(count(f))

    
