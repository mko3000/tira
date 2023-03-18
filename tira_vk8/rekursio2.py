
global i 
i = 0

def f(n):
    global i
    i += 1
    if n <= 2:
        return n
    return f(n-1)+f(n-2)+f(n-3)


if __name__ == "__main__":
    print(f(30))
    print("kutsuja:",i)