# Verkossa on solmut 1,2,…,N ja N=5000
# Aloitussolmu on solmu 1
# Solmusta a on kaari solmuun b, jos a<b ja b−a<10
# Jokaisen kaaren paino on satunnainen kokonaisluku välillä 1…1000
# Kaaret ovat satunnaisessa järjestyksessä kaarilistassa.

from random import randint, shuffle
import time

def tee_verkko(n):
    for a in range(1,n+1):
        for b in range(a+1,a+9):
            if b<=n:
                kaaret.append({"alku":a,"loppu":b,"paino":randint(1,1000)})
    shuffle(kaaret)

n = 5000
kaaret = []
tee_verkko(n)
#print(kaaret)

etaisyys = [float("Inf")] * (n+1)

aloitus = 1
etaisyys[aloitus] = 0

alkuaika = time.time()
while True:
    muutos = False
    for kaari in kaaret:
        nyky = etaisyys[kaari["loppu"]]
        uusi = etaisyys[kaari["alku"]]+kaari["paino"]
        if uusi < nyky:
            etaisyys[kaari["loppu"]] = uusi
            muutos = True
    if not muutos:
        break
loppuaika = time.time()

etaisyys = etaisyys[1:]
print(loppuaika-alkuaika)