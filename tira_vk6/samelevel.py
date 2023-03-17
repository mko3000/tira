from collections import namedtuple

def count(node, level):
    return oma_lasku(node,0,level)
    

def oma_lasku(node, nyt, tavoite):
    nyt += 1
    if node == None:
        return 0
    if nyt == tavoite:
        return 1
    return oma_lasku(node.left, nyt, tavoite) + oma_lasku(node.right, nyt, tavoite)

def laske_solmut(node):
    if node == None:
        return 0
    return 1 + laske_solmut(node.left) + laske_solmut(node.right)


if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree,1)) # 1
    print(count(tree,2)) # 1
    print(count(tree,3)) # 2
    print(count(tree,4)) # 0
    print(laske_solmut(tree))