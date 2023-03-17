from string import ascii_lowercase as alphapet

def encrypt(s):
    i = 0
    enclist=[]
    for letter in s:
        i+=1
        if alphapet.index(letter)+i >= len(alphapet):
            i=i-len(alphapet)
        enclist.append(alphapet[alphapet.index(letter)+i])
    return ''.join(enclist)

if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzz")) # bcdefghijklmnopqrstuvwxyzabcde