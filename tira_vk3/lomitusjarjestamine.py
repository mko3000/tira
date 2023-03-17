import time
from random import shuffle

def jarjesta(a,b):
    if a == b:
        return
    k = (a+b)//2 #int((a+b)/2)
    jarjesta(a,k)
    jarjesta(k+1,b)
    lomita(a,k,k+1,b)

def lomita(a1, b1, a2, b2):
    a = a1
    b = b2+1
    for i in range(a,b):
        if a2 > b2 or (a1 <= b1 and taulu[a1] <= taulu[a2]):
            apu[i] = taulu[a1]
            a1 += 1
        else:
            apu[i] = taulu[a2]
            a2 += 1
    for i in range(a,b):
        taulu[i] = apu[i]


#taulu = [5,1,2,9,7,5,4,2] #[1, 2, 2, 4, 5, 5, 7, 9]
taulu = list(range(10**5))
shuffle(taulu)
apu = [""]*len(taulu)


start_time = time.time()
jarjesta(0, len(taulu)-1)
end_time = time.time()
print(taulu)
print(end_time-start_time)