import heapq

def luo_hyppyverkko(lista):
    verkko = {}
    for n in range(len(lista)):
        verkko[n] = []
    for i in range(len(lista)):        
        if i + lista[i] < len(lista):
            verkko[i].append((i + lista[i], lista[i])) 
        if i - lista[i] >= 0 and i > 0:
            verkko[i].append((i - lista[i], lista[i]))

    return verkko   


def calculate(t):
    verkko = luo_hyppyverkko(t)
    n = len(verkko)
    etaisyys = [float("Inf")] * n
    kasitelty = [False] * n
    aloitus = 0
    etaisyys[aloitus] = 0
    keko = []
    keko.append((0,aloitus))

    while keko:
        solmu = heapq.heappop(keko)[1]

        if kasitelty[solmu]:
            continue
        kasitelty[solmu] = True

        for kaari in verkko[solmu]:
            nyky = etaisyys[kaari[0]]
            uusi = etaisyys[solmu]+kaari[1]
            if uusi < nyky:
                etaisyys[kaari[0]] = uusi
                heapq.heappush(keko, (uusi,kaari[0]))
                
    #print(etaisyys)
    if etaisyys[n-1] == float("Inf"):
        return -1
    return etaisyys[n-1]

if __name__ == "__main__":
    print(calculate([1,1,1,1])) # 3
    print(calculate([3,2,1])) # -1
    print(calculate([3,5,2,2,2,3,5])) # 10
    print(calculate([7,5,3,1,4,2,4,6,1])) # 32
    print(calculate([2, 7, 1, 3, 2, 1, 3, 9, 4, 9])) # 9


