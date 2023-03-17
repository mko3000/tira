def balance(s):
    remaining_avaavia = 0
    remaining_tähtiä = 0
    remaining_sulkevia = 0
    for i in s:
        if i == "(":
            remaining_avaavia += 1
        if i == "*":
            remaining_tähtiä +=1
        if i == ")":
            remaining_sulkevia += 1
    result = []
    avaavia = 0
    counter = 0
    for i in s:
        counter += 1
        if i == "(":
            avaavia += 1
            remaining_avaavia -= 1
        if i == "*":
            remaining_tähtiä -= 1
            if avaavia > 0:
                if remaining_tähtiä > 0:
                    result.append(1)
                    avaavia -= 1
                else:#jos viimeinen tähti

                    suljetaan = avaavia + remaining_avaavia - remaining_sulkevia
                    if suljetaan <= 0:
                        return None
                    result.append(suljetaan)
                    avaavia -= suljetaan  
                    if remaining_avaavia > remaining_sulkevia:
                        return None
            else:
                #print("1. None")
                return None
        if i == ")": 
            remaining_sulkevia -= 1
            avaavia -= 1
            if avaavia < 0:
                #print("2. None",counter)
                return None
    if avaavia != 0:
        #print("3. None",counter,avaavia,remaining_sulkevia)
        return None
    else:
        #print("avaavia jäljellä", remaining_avaavia)
        return result

if __name__ == "__main__":
    print(balance("*(")) # None
    print(balance("(*")) # [1]
    print(balance("(())")) # []
    print(balance("(((((*")) # [5]
    print(balance("(((((*(")) # None
    print(balance("((((*(()*()*")) # [2,2,1]
    print(balance("((*))(((*")) # None
    print(balance("(((*)()")) 
    print(balance("((*()()()((*)()))"))