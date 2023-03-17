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

def etsi(node, key): 
    if (node == None):
        return False 
    if (node.value == key):
        return True 
    
    """ then recur on left subtree """
    res1 = etsi(node.left, key)
    # node found, no need to look further
    if res1:
        return True
 
    """ node is not found in left,
    so recur on right subtree """
    res2 = etsi(node.right, key)
 
    return res2


def lapikaynti(node):
    if node == None:
        return
    lapikaynti(node.left)
    print(node.value)
    lapikaynti(node.right)

def laske_solmut(node):
    if node == None:
        return 0
    return 1 + laske_solmut(node.left) + laske_solmut(node.right)

if __name__ == "__main__":

    n=10**5
    puun_alkiot = list(range(1,n+1))
    random.shuffle(puun_alkiot)

    root = Node(puun_alkiot[0])
    for i in range(1,len(puun_alkiot)):
        root.lisaa(puun_alkiot[i])

    print(korkeus(root))

