def count(s, c):
    result = 0
    counter = 0
    for i in range(len(s)):
        if s[i] == c:
            counter = 0
        else:
            counter += 1
        result += counter
    return result

if __name__ == "__main__":
    print(count("abacabb", "b")) # 7
    print(count("abcdef", "g")) # 21
    print(count("xxxxxxxxx", "x")) # 0
    print(count("pupujussikainen", "u")) # 48