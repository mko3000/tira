n = 6
routes = [[False]*n for _ in range(n)]

print(routes[2][3])
for y in routes:
    print(y)

for y in routes:
    for x in y:
        print(x)

print(routes)