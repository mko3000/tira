def solve(t):
    n = len(t)
    i=0
    moves = 0

    while i < n//2:
        if t[i] > n//2:
            moves += n//2-i
        if t[i+n//2]<= n//2:
            moves += i
        i += 1

    return moves



if __name__ == "__main__":
    print(solve([2, 1, 4, 3])) # 0
    print(solve([5, 3, 4, 1, 6, 2])) # 6
    print(solve([6, 5, 4, 3, 2, 1])) # 9
    print(solve([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])) # 15
