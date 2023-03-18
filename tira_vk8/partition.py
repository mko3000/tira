def subgroups(subcodes, s, n):
    if len(s) == n:
        subcodes.append(s)
    else:
        subgroups(subcodes, s+"A", n)
        subgroups(subcodes, s+"B", n)

def check(t):
    subcodes = []
    subgroups(subcodes, "", len(t))
    for code in subcodes:
        a = 0
        b = 0
        for i in range(len(code)):
            if code[i] == "A":
                a += t[i]
            else:
                b += t[i]
        if a == b:
            return True
    return False

if __name__ == "__main__":
    print(check([3,4,5])) # False
    print(check([16,8,4,4])) # True
    print(check([9,4,8,7,6])) # True
    print(check([1,2,3,4,5,6])) # False
    print(check([1,2,3,4,5,6,7])) # True
    print(check([4,4,4,6,6])) # True

