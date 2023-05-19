def luo_verkko(lista):
    #tehdään verkko, johon tallennetaan mahdolliset siirrot(?)
    verkko = {}
    for n in range(len(lista)):
        verkko[n] = []
    for i in range(len(lista)):        
        if i + lista[i] < len(lista):
            verkko[i].append(i + lista[i]) 
        if i - lista[i] >= 0 and i > 0:
            if i not in verkko[i-lista[i]]:#tarkistetaan, ettei turhaan mennä sinne mistä tultiin
                verkko[i].append(i - lista[i])
    print(verkkokuva(verkko))
    return verkko

def luo_hyppyverkko(lista):
    verkko = {}
    for n in range(len(lista)):
        verkko[n] = []
    for i in range(len(lista)):        
        if i + lista[i] < len(lista):
            verkko[i].append((i + lista[i], lista[i])) 
        if i - lista[i] >= 0 and i > 0:
            if i not in verkko[i-lista[i]]:#tarkistetaan, ettei turhaan mennä sinne mistä tultiin
                verkko[i].append((i - lista[i], lista[i]))
    return verkko
    
def verkkokuva(verkko):
    tuloste = ""
    for solmu in verkko:
        for i in range(len(verkko[solmu])):
            rivi = f'{solmu}--{verkko[solmu][i][1]}-->{verkko[solmu][i][0]};\n'
            tuloste += rivi
    return tuloste


def leveyshaku(t): #tää laskee kuinka monessa käydään, mutta ei laske askelien määrää
    network = luo_verkko(t)
    n = len(network)
    queue = []
    dist = [-1 for _ in range(n)]
    seen = [False for _ in range(n+1)]
    start = 0
    queue.append(start)
    seen[start] = True
    dist[start] = 0
    while queue:
        node = queue.pop(0)
        for neighbour in network[node]:
            if seen[neighbour]:
                continue
            queue.append(neighbour)
            seen[neighbour] = True
            dist[neighbour] = dist[node]+1
    print(dist)
    return dist[n-1]

def calculate(t):
    verkko = luo_hyppyverkko(t)
    n = len(verkko)
    etaisyys = [float("Inf")] * (n)
    kasitelty = [False] * (n)
    aloitus = 0
    etaisyys[aloitus] = 0
    keko = []
    keko.append((0,aloitus))

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
    if etaisyys[n-1] == float("Inf"):
        return -1
    return etaisyys[n-1]

if __name__ == "__main__":
    print(calculate([3,5,2,2,2,3,5]))
    print(calculate([1,1,1,1])) # 3
    print(calculate([3,2,1])) # -1
    print(calculate([3,5,2,2,2,3,5])) # 10
    print(calculate([7,5,3,1,4,2,4,6,1])) # 32