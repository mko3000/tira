

from random import randint, shuffle
import time

def tee_vierusverkko(n):
    verkko = {}
    for a in range(1, n+1):
        verkko[a] = []
    for a in range(1, n+1):
        for b in range(a+1, a+10):
            if b <= n:
                paino = randint(1,1000)
                verkko[a].append((b, paino))
                #verkko[b].append((a, paino))
    return verkko


n = 5000
verkko = tee_vierusverkko(n)

etaisyys = [float("Inf")] * (n+1)
kasitelty = [False] * (n+1)
aloitus = 1
etaisyys[aloitus] = 0
keko = []
keko.append((0,aloitus))


alkuaika = time.time()

while keko:
    solmu = keko.pop()[1]
    if kasitelty[solmu]:
        continue
    kasitelty[solmu] = True
    for kaari in verkko[solmu]:
        nyky = etaisyys[kaari[0]]
        uusi = etaisyys[solmu]+kaari[1]
        if uusi < nyky:
            etaisyys[kaari[0]] = uusi
            keko.append((uusi,kaari[0]))

loppuaika = time.time()

etaisyys = etaisyys[1:]
print(loppuaika-alkuaika)
#print(etaisyys)