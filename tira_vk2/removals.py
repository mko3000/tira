def find(s, k):
    count = 0
    as_removed = 0
    bs_removed = 0
    cs_removed = 0
    locs = {"a":[],"b":[],"c":[]}
    a_locs = {}
    b_locs = {}
    c_locs = {}
    for i in range(len(s)):
        locs[s[i]].append(i)
        
    print(locs)

    if as_removed == k and bs_removed == k and cs_removed == k:
        return count

if __name__ == "__main__":
    print(find("abc", 1)) # 3
    print(find("aabca", 1)) # 3
    print(find("aaaabbbcccc", 1)) # 6
    print(find("aabbaacc", 2)) # 6
    print(find("aaaabbbbaaaccccaaccacbbaa", 3)) # 13