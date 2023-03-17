def generate(n):
    counter = 1
    no = 0
    while counter <= n:
        no += 1
        for i in str(no):
            if str(no).count(i)>1:
                counter += 1
                break
    return no       

        

        

if __name__ == "__main__":

    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505 
    print(generate(3))