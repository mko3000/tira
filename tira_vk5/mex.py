class Mex:
    def __init__(self):
        self.group = set()
        self.min = 0

    def add(self, x):
        self.group.add(x)
        while True:
            if self.min not in self.group:
                return self.min   
            self.min += 1

if __name__ == "__main__":
    m = Mex()
    print(m.add(1)) # 0
    print(m.add(3)) # 0
    print(m.add(4)) # 0
    print(m.add(0)) # 2
    print(m.add(5)) # 2
    print(m.add(2)) # 6