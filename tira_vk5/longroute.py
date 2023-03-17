def count_loop(s):
    if s == "":
        return 0
    route = set()
    route.add((0,0))
    location = [0,0]
    for command in s:        
        if command == "L":
            location[0] -= 1
        if command == "R":
            location[0] += 1
        if command == "D":
            location[1] -= 1
        if command == "U":
            location[1] += 1
        route.add(tuple(location))
    return len(route)

def most_commands(s):
    commands = "URDL"
    command_list = []
    for c in commands:
        command_list.append(s.count(c))
    return max(command_list)

def count(s,k):
    p = most_commands(s)    
    diff = count_loop(s*(p+1))-count_loop(s*p)
    return count_loop(s*min(p,k)) + max(0,(k-p))*diff
    

if __name__ == "__main__":
    print(count("UR", 100)) # 201
    print(count("UD", 100)) # 2
    print(count("UURRDDL", 500)) # 1506
    print(count("L", 10**9)) # 1000000001
    print(count("DLUR", 10**9)) # 4

    print(count("LDLRDRRRUU", 3)) # 23
    #print(3+48+47+2)    
    print(count("UURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL", 1000000000)) 
    