from collections import deque

def solve(n,k):
    lista = deque()
    for i in range(n):
        lista.append(i+1)
    for i in range(k):
        eka = lista.popleft()
        toka = lista.popleft()
        lista.append(toka)
        lista.append(eka)
    return lista[0]

if __name__ == "__main__":
    print(solve(4,3)) # 4
    print(solve(12,5)) # 11
    print(solve(99,555)) # 11
    print(solve(12345,54321)) # 9875