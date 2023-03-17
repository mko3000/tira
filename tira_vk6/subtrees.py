from collections import namedtuple

def diff(node):
    return max_diff(node)[1]
    return max_diff(node,0)

def max_diff(node):
    if not node:
        return (0,0)
    left = max_diff(node.left)
    right = max_diff(node.right)
    isoin = max(abs(left[0]-right[0]),left[1],right[1])
    return (left[0]+right[0]+1,isoin) 


def max_diff2(node,isoin):
    if not node:
        return 0
    left = max_diff(node.left,isoin)
    right = max_diff(node.right,isoin)
    isoin = max(abs(left-right),isoin) +1
    return isoin 


def paskaa(node):
    isoin = 0
    return max_diff(node,isoin)
    if not node:
        return 0
    return max(abs(laske_solmut(node.left)-laske_solmut(node.right)))
    return abs(diff(node.left)-diff(node.right))
    return 1 + max(diff(node.left),diff(node.right))
    return max(laske_solmut(node.left),laske_solmut(node.right))

def laske_solmut(node):
    if node == None:
        return 0
    return 1 + laske_solmut(node.left) + laske_solmut(node.right)



if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    tree2 = Node(left=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=None)))))))))))))))))))))))))))))))))))))))))))))))), right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=None)))))))))))))))))))))))))))))))))))))))))))))))))
    tree3 = Node(left=Node(left=None, right=None), right=Node(left=None, right=None))
    tree4 = Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=None))
    tree5 = Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=None)

    print(laske_solmut(tree2))
    print(diff(tree)) # 3
    print(diff(tree2))
    print(diff(tree3))
    print(diff(tree4))
    