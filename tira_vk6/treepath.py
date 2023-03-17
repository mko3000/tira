from collections import namedtuple
#jos solmulla on kaksi oksaa, reittejä tulee 1 lisää
#haara on lista, solmussa yhdistetään listat

def count(node):
    return paths(node)

def paths(node):
    if not node: return [[],0]
    l = paths(node.left)
    r = paths(node.right)
    if l!=[[],0] and r!=[[],0]:
        #haarautuu, eli reittien määrä lisääntyy 1:llä
        #tarviiko reittien määrää tietää?
        return korkeus()


def korkeus(node):
    if node == None:
        return -1
    return 1 + max(korkeus(node.left), korkeus(node.right))

if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(Node(None,None),Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 8