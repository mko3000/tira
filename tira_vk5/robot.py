def count(s):
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

if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2