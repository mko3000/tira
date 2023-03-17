
sana = "sunnuntai"
luku = 0
A = 19
N = 10**6
for i in range(len(sana)):
    luku += A**(len(sana)-1-i)*ord(sana[i])
print(luku)
print(luku%N)