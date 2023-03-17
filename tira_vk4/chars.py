from collections import deque

def solve(s):  
    b = ""  
    i = 1
    while i < len(s):
        if s[i]==s[i-1]:            
            a = s[:i-1]
            if ord(s[i-1]) < ord("z"):
                b = chr(ord(s[i-1])+1)
            else:
                b = "a"
            c = s[i+1:]
            s = a+b+c
            i = max(0, i-2)
        else:
            b = ""
        if i>1 and s[i-1] == b:            
            i-=1
        else:
            i += 1  
    return s




if __name__ == "__main__":
    print(solve("auto")) # auto
    print(solve("ddqqirr")) # eris
    print(solve("aaaaaa")) # cb
    print(solve("wsstuva")) # xa
    print(solve("zzzzzzzz")) # c
    print(solve("mlkjihgfedcbb")) # n
    print(solve("kkkjjiikjkjiikjjiijkjji")) # mjkjmlki
    print(solve("aabaaaabbb")) # dcb



def solve2(s):  
    b = ""  
    i = -1
    while i < len(s):   
        i += 1     
        if i < len(s)-1:
            if s[i]==s[i+1]:
                a = s[:i]
                b = chr(ord(s[i])+1)
                c = s[i+2:]
                s = a+b+c
    return s