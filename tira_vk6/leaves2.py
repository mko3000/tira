from collections import namedtuple

def count(node):  
    l = Leaves(node)
    return l


class Leaves:
    def __init__(self,node):
        self.leaves = 0
        self.node = node

    def lapikaynti(self):
        if self.node == None:
            return
        self.lapikaynti(self.node[0])
        #print(node)
        if self.node == Node(left=None, right=None):
            self.leaves += 1
            print("leave")       
        self.lapikaynti(self.node[1])

    def leaf_counter(self):
        self.lapikaynti()
        return self.leaves




def laske_solmut(node):
    if node == None:
        return 0
    return 1 + laske_solmut(node[0]) + laske_solmut(node[1])

if __name__ == "__main__":

    Node = namedtuple("Node",["left","right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 2
    print(laske_solmut(tree))
    #print(lapikaynti(tree))