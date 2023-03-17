

class QuickList:
    def __init__(self, t):
        self.l = t
        self.a = 0

    def move(self, k):
        if k >= len(self.l):
            pass
        elif k + self.a > len(self.l)-1:
            self.a = self.a + k - len(self.l)
        else:
            self.a = self.a+k


    def get(self, i):
        #print("i",i,"a",self.a,"i+a",(i+self.a),"len",len(self.l))
        if i + self.a > len(self.l)-1:
            i = i - (len(self.l) - self.a)
        else:
            i = self.a + i
        return self.l[i]

if __name__ == "__main__":
    g = QuickList([1,2,3,4,5])
    print(g.get(4))
    g.move(3)
    print(g.get(2))
    g.move(3)
    print(g.get(2))

    q = QuickList([1,2,3,4,5,6,7,8,9,10])
    print([1,2,3,4,5,6,7,8,9,10])
    print(q.get(4)) # 5
    q.move(3)
    #print(q.get(8)) 
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9