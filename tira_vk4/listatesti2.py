import time
from collections import deque
lista = deque()

alku = time.time()
for i in range(10**5):
    lista.append(i)
loppu = time.time()
print("Lisäys:",(loppu-alku))

alku = time.time()
while len(lista) > 0:
    lista.popleft()
loppu = time.time()
print("Poisto:",(loppu-alku))
