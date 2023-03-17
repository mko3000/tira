from collections import defaultdict

class Mode:
    def __init__(self):
        self.group = defaultdict(lambda:0)
        self.mode = 10**10

    def add(self, x):
        self.group[x] += 1
        if self.group[x] == self.group[self.mode]:
            self.mode = min(x,self.mode)
        elif self.group[x] >= self.group[self.mode]: 
            self.mode = x
        return self.mode

if __name__ == "__main__":
    m = Mode()
    print(m.add(1)) # 1
    print(m.add(2)) # 1
    print(m.add(2)) # 2
    print(m.add(1)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 3