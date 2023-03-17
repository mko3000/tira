from collections import defaultdict
from string import ascii_lowercase as asciis


def find(s):
    letters = dict()
    for i in asciis:
        letters[i]=0
    counter = 0

    for i in range(len(s)):
        if letters[s[i]] == 0:
            letters[s[i]] = 1
        if i > 0 and s[i] == s[i-1]:            
            counter += 1
            letters[s[i]] = max(counter,letters[s[i]])            
        else:
            counter = 0
    print(letters)
    return min(letters.values())+1

if __name__ == "__main__":
    print(find("zzz")) # 1
    print(find("aybabtu")) # 1
    print(find("abcdefghijklmnopqrstuvwxyz")) # 2

    from random import randint, seed
    seed(1337)
    h = set()
    s = 'aa'
    for i in range(2, 10**5):
        for u in range(26):
            w = chr(ord('a')+u)
            if s[i-2]+s[i-1]+w not in h:
                h.add(s[i-2]+s[i-1]+w)
                s += w
                break
        if len(s) == i:
            s += chr(ord('a') + randint(0,25))
    print(find(s))