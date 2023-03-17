from collections import namedtuple

def count1(node):  
    global leaves   
    leaves = 0      
    lapikaynti(node)
    return leaves

def lapikaynti(node):
    global leaves  
    if node == None:
        return
    lapikaynti(node.left)
    #print(node)
    if node == Node(left=None, right=None):
        #print("lehti")
        leaves += 1
    lapikaynti(node.right)

def laske_solmut(node):
    if node == None:
        return 0
    return 1 + laske_solmut(node[0]) + laske_solmut(node[1])

def count(node):
    if node == None:
        return 0
    left = count(node.left)
    right = count(node.right)
    if left == 0 and right == 0:
        return 1 + left + right
    else:
        return left + right

if __name__ == "__main__":

    Node = namedtuple("Node",["left","right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    tree2 = Node(left=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=None)))))))))))))))))))))))))))))))))))))))))))))))), right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=None)))))))))))))))))))))))))))))))))))))))))))))))))
    bush = Node(left=None, right=None)
    print(count(tree)) # 2

    print(count(bush))
    print(count(Node(left=None, right=None)))

    print(laske_solmut(tree2))
    #print(count1(tree2))
    print(count(tree2))
    #print(laske_solmut(tree))
    #print(lapikaynti(tree))