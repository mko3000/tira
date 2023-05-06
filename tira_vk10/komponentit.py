
def verkot(n):
    verkko = {}
    for i in range(2,n):
        verkko[i]=[]
    for i in range(2,n):
        for j in range(2,n):
            if j % i == 0 and i != j:
                verkko[i].append(j)
                verkko[j].append(i)
    return verkko

def syvyyshaku(solmu):
    #print(solmu)
    if vierailtu[solmu]:
        return
    vierailtu[solmu] = True
    for naapuri in verkko[solmu]:
        syvyyshaku(naapuri)

n = 1000
verkko = verkot(n)
vierailtu = {}
for i in range(2,n):
    vierailtu[i] = False

alkusolmu = 2
komponentit = 0
while True:
    komponentit += 1
    syvyyshaku(alkusolmu)
    if False in vierailtu.values():
        alkusolmu = list(vierailtu.keys())[list(vierailtu.values()).index(False)]
    else:
        break

print(komponentit)


# Tirakirja:
# Suuntaamaton verkko on yhtenäinen, jos kaikki solmut ovat yhteydessä toi-
# siinsa. Voimmekin tarkastaa verkon yhtenäisyyden aloittamalla syvyyshaun
# jostakin solmusta ja tutkimalla, saavuttaako haku kaikki verkon solmut.
# Lisäksi voimme löytää verkon yhtenäiset komponentit käymällä läpi solmut
# ja aloittamalla uuden syvyyshaun aina, kun vastaan tulee vierailematon sol-
# mu. Jokainen syvyyshaku muodostaa yhden komponentin.