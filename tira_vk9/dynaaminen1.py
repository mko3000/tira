import time

def f(n):
    mem = [0]*(n)
    mem[0] = 1
    mem[1] = 2
    mem[2] = 3
    for i in range(3,n):
        mem[i] = mem[i-1] + mem[i-2] + mem[i-3]
    return mem[n-1]



alku = time.time()
print(f(30))
loppu = time.time()
print("kesto",loppu-alku)