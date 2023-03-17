#0.3796205520629883
 

 
import random
import time
 
def jarjesta(a,b):
    if a == b:
        return
    k = (a+b)//2
    jarjesta(a,k)
    jarjesta(k+1,b)
    lomita(a,k,k+1,b)
 
def lomita(a1, b1, a2, b2):
    a = a1
    b = b2 + 1
    for i in range(a, b):
        if a2 > b2 or (a1 <= b1 and array[a1] <= array[a2]):
            helper[i] = array[a1]
            a1 += 1
        else:
            helper[i] = array[a2]
            a2 += 1
    for i in range(a, b):
        array[i] = helper[i]
 
 
array = list(range(10**5))
random.shuffle(array)
helper = array.copy()
 
start = time.time()
jarjesta(0,len(array)-1)
end = time.time()
 
print(end-start)
print(array == sorted(array))