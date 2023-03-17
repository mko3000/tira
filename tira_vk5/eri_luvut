import time
import random
lista = []
for i in range(10**6):
    lista.append(random.randint(1,10**9))
l1=lista
l2=lista

alku = time.time()
l1.sort()
laskuri = 1
for i in range(len(l1)-1):
    if l1[i] != l1[i+1]:
        laskuri += 1
loppu = time.time()

print("1. eri lukuja:",laskuri,", aikaa kului:", (loppu-alku))

alku=time.time()
joukko=set(l2)
laskuri = len(joukko)
loppu=time.time()
print("2. eri lukuja:",laskuri,", aikaa kului:", (loppu-alku))