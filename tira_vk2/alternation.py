def sequenceSubStrings(sublen):
    length = 0
    for i in range(sublen):
        length += i+1
    return length

def count(t):
    counter = 1
    alteringLenght = 2
    for i in range (2, len(t)):
        if (t[i]>t[i-1] and t[i-1]<t[i-2]) or (t[i]<t[i-1] and t[i-1]>t[i-2]):
            alteringLenght += 1
        else:
            counter += sequenceSubStrings(alteringLenght)-1
            alteringLenght = 2
    counter += sequenceSubStrings(alteringLenght)-1

    return counter

if __name__ == "__main__":
    print("sequenceSubStrings",sequenceSubStrings(4))
    print(count([1,2,3,4])) # 7
    print(count([1,4,2,5,3])) # 15
    print(count([7,2,1,3,5,4,6])) # 17 
    print(count([4,1,3,2])) #10

