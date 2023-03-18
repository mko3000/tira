
def add(anag,s, result):
    global length
    if len(anag) == length:
        if anag not in result:
            result.append(anag)
    else:
        for l in range(len(s)):
            add(anag+s[l],s[:l] + s[l+1:],result)


def create(s):
    global length
    length = len(s)
    result = []
    add("", s, result)
    result = sorted(result)
    return result

if __name__ == "__main__":
    print(create("ab")) # [ab,ba]
    print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("aybabtu"))) # 1260

