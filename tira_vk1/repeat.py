def find(s):
    i = 0
    for letter in s:        
        i+=1
        if len(s)%i==0:
            mjono = int(len(s)/i)*s[:i]
            if mjono==s:
                return i
        

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7