import random
import time

def nouseva(taulu):
    n = len(taulu)
    pisin = [1]*n
    for k in range(1,n):
        for x in range(k):
            if taulu[x] < taulu[k] and pisin[x]+1 > pisin[k]:
                pisin[k] = pisin[x]+1
    return max(pisin)


l = [*range(5000)]
random.shuffle(l)
alku = time.time()
print(nouseva(l))
loppu = time.time()
print("kesto",loppu-alku)


#esim = [6,2,5,1,7,4,8,3]
#print(nouseva(esim))

#print(nouseva([1,2,3,4,5]))
