class Stack:
    def __init__(self):
        self.pino = []
        self.ideksit_joihin_lisätty = []

    def push(self, x):
        self.pino.append(x)
        #self.lisäykset.append(0)
        #print(self.pino)

    def pop(self):
        #self.lisäykset.pop()
        return self.pino.pop()

    def increase(self, k):
        for i in range(k):            
            l = len(self.pino)-1
            self.pino[l-i]+=1
            #liian hidas



if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.increase(2)
    print(s.pop()) # 4
    s.push(1)
    s.increase(2)
    print(s.pop()) # 2
    print(s.pop()) # 4
    print(s.pop()) # 1

# pidetään kirjaa siitä, mitä lukuja on kasvatettu ja kuinka paljolla
# pidetään kirjaa siitä, montako kertaa on kasvatettu, ja kuinka pitkää 