import time
from random import randint

n = 10**5
syote = ""

for i in range(n):
    syote+= str(randint(0,1))


alku = time.time()
laskuri = 0
nollat = 0
for i in range(len(syote)):
    if int(syote[i]) == 0:
        nollat += 1
    else:
        laskuri += nollat
print(laskuri)
loppu = time.time()
print("nopealla tavalla aikaa kului", loppu-alku, " s")


alku = time.time()
laskuri = 0
for i in range(len(syote)):
    for j in range(i+1,len(syote)):
        if int(syote[i]) == 0 and int(syote[j]) == 1:
            laskuri += 1
print(laskuri)
loppu = time.time()
print("hitaalla tavalla aikaa kului", loppu-alku, " s")