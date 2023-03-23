def count(n,a,b):
    length = (n//a+1)
    moves = [a,b]
    result = [0]*length
    for i in range(a,length):
        result[i] = i
        for jump in moves:
            if i+jump <= n:
                result[i] += jump 
    return result
    result = [[a]]*(n//a)
    print(result)
    moves = [a,b]
    for i in range(1,(n//a)):
        #for j in range
        for jump in moves:
            if result[i-1] + jump <= n:
                result[i] = result[i-1] + jump

def find_one(n,a,b):
    first_solution = [a]
    moves = [a,b]
    for i in range(1,(n//a)):
        jump = a
        if first_solution[i-1] + jump <= n:
            first_solution[i] = first_solution[i-1] + jump
    return first_solution
    
def coins(total, coins):
    result = [0]*(total+1)
    for i in range(1, total+1):
        result[i]=i
        for coin in coins:
            if i - coin >= 0:
                result[i] = min(result[i], result[i-coin]+1)
    return result

def recurs(n,a,b,):
    if n == 0:
        return 0
    if n - a >= 0:
        pass
        
def count_jumps(n, a, b):
    # Initialize a table to store the results of subproblems
    print("n,a,b:",n,a,b)
    dp = [0] * (n + 1)
    dp[0] = 1

    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        print(dp)
        if i >= a:
            print("*a*  i =", i, ", dp[i] =", dp[i], ", dp[i-a] =",dp[i-a], "new dp[i]:", dp[i]+dp[i-a])
            dp[i] += dp[i-a]
            
        if i >= b:
            print("*b*  i =",i,", dp[i] =", dp[i], ", dp[i-b] =",dp[i-b], "new dp[i]:", dp[i]+dp[i-b])
            dp[i] += dp[i-b]
            
        print("")

    # Return the final result
    return dp
        
    


if __name__ == "__main__":
    
    # print(find_one(4,1,2))
    # print(coins(25,[1,6,7]))

    print(count_jumps(4,1,2)) # 5
    # print(count_jumps(10,2,5)) # 2
    # print(count_jumps(10,6,7)) # 0
    # print(count_jumps(30,3,5))
    # print(count_jumps(50,2,3))

    # print(count(4,1,2)) # 5
    # print(count(10,2,5)) # 2
    # print(count(10,6,7)) # 0
    # print(count(30,3,5)) # 58
    # print(count(50,2,3)) # 525456
