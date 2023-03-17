
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def parse_list_from_command_string(s):
    s = s.replace("("," ( ")
    s = s.replace(")"," ) ")
    s = s.split()
    return s

def eval(s):
    s = parse_list_from_command_string(s)
    operators = []
    numbers = [[]]
    opened = 0
    for i in s:
        if i == "(":
            opened += 1
        if i in ["+","*"]:
            operators.append(i)
            numbers.append([])   
        if is_integer(i):
            numbers[opened].append(int(i))
        if i == ")":
            opened -= 1
            operator = operators.pop()
            #print("operator",operator, "opened", opened, "numbers", numbers)
            result = 1
            if operator == "+":
                result = sum(numbers.pop())
            if operator == "*":
                members = numbers.pop()
                for j in members:
                    result *= j
            numbers[opened].append(result)
    return numbers[0][0]

if __name__ == "__main__":
    print(eval("(+ 1 2 3 4 5)")) # 15
    print(eval("(+ 5 (* 3 2) 7)")) # 18
    print(eval("(* (+ (+ 1 2) 3) (+ (* 4 5) 6 2))")) # 168
    print(eval("(+ 123 456)")) # 579