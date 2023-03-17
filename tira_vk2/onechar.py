def count(s):
    curstrings = 0
    substrings = 0
    i = 0
    for l in range(len(s)):
        i += 1
        curstrings += i
        try:
            if s[l] != s[l+1]:
                substrings += curstrings
                i=0
                curstrings = 0
        except:
            substrings+=curstrings
    return substrings


if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5