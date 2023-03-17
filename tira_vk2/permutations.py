def slowcount(a, b):
    counter = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(b)):
            if a[i] == b[j]:
                counter += 1
    return counter

def weirdcount(a, b):
    #print(a,b)
    counter = 0 
    b_loc = {}
    for i in range(len(a)):
        if a[i] not in b_loc:
            b_loc[a[i]] = b.index(a[i])
        if i < b_loc[a[i]]:
            counter += 1
    #print(b_loc)
    return counter

def badcount(a, b):
    counter = 0 
    for i in range(len(a)-1):
        for j in range(len(b)-1):            
            if b[len(b)-j-1] == a[i] and i<len(b)-j-1:
                counter += 1
                break
    return counter

def count(a, b):
    counter = 0 
    b_loc = {}
    for j in range(len(b)):
        b_loc[b[j]]=j
    for i in range(len(a)):
        if i<b_loc[a[i]]:
            counter += 1
    return counter


if __name__ == "__main__":
    print(count([1,2,3], [1,2,3])) # 0
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5