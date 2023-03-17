import random

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def lisaa(self, luku):
        if luku < self.value:
            if self.left:
                #jos vasen oli olemassa, kutsutaan itseä uudestaan
                self.left.lisaa(luku)
            else:
                #jos ei ollut olemassa, lisätään luku
                self.left = Node(luku)
        elif luku > self.value:
            if self.right:
                self.right.lisaa(luku)
            else:
                self.right = Node(luku)

def korkeus(node):
    if node == None:
        return -1
    return 1 + max(korkeus(node.left), korkeus(node.right))


if __name__ == "__main__":

    n=10**5
    puun_alkiot = list(range(1,n+1))
    random.shuffle(puun_alkiot)

    root = Node(puun_alkiot[0])
    for i in range(1,len(puun_alkiot)):
        root.lisaa(puun_alkiot[i])

    print(korkeus(root))

