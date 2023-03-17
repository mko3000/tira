from random import shuffle
import time

def jarjesta(taulu):
    n = len(taulu)
    for i in range(1,n):
        j = i-1
        while j >= 0 and taulu[j] > taulu[j+1]:
            bigger = taulu[j]
            taulu[j] = taulu [j+1]
            taulu[j+1] = bigger
            j -= 1
    return taulu

#print(jarjesta([4,3,1,6,8,3,9]))
print(jarjesta([5,1,2,9,7,5,4,2]))

taulukko=list(range(10**5))
shuffle(taulukko)

# start_time = time.time()
# uusi = jarjesta(taulukko)
# end_time = time.time()
# print(end_time-start_time)