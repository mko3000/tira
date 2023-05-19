class CoursePlan:
    def __init__(self):
        self.kurssit = {}
        
    def add_course(self,course):
        self.kurssit[course] = []

    def add_requisite(self,course1,course2):
        self.kurssit[course1].append(course2)

    def find(self):
        self.kayty = set()
        self.kasitelty = set()
        self.jarjestys = []
        self.sykli = False
        for kurssi in self.kurssit:
            if kurssi not in self.kayty:
                self.syvyyshaku(kurssi)
                if self.sykli:
                    return
        self.jarjestys.reverse()
        return self.jarjestys
    
    def syvyyshaku(self,kurssi):
        self.kayty.add(kurssi)
        for seuraava in self.kurssit[kurssi]:
            if seuraava in self.kayty and seuraava not in self.kasitelty:
                #print("Verkossa on sykli")                
                self.sykli = True
                return 
            elif seuraava not in self.kasitelty:
                self.syvyyshaku(seuraava)
        self.kasitelty.add(kurssi)
        self.jarjestys.append(kurssi)

        
    


if __name__ == "__main__":
    c = CoursePlan()
    #print(c.find())
    c.add_course('course2')
    c.add_course('course5')
    c.add_requisite('course2','course5')
    c.add_requisite('course5','course5')
    print(c.find()) #None
    print(c.find())
    print(c.find())
    
    # c = CoursePlan()
    # c.add_course("Ohpe")
    # c.add_course("Ohja")
    # c.add_course("Tira")
    # c.add_course("Jym")
    # c.add_requisite("Ohpe","Ohja")
    # c.add_requisite("Ohja","Tira")
    # c.add_requisite("Jym","Tira")
    # print(c.find()) # [Ohpe,Jym,Ohja,Tira]
    # c.add_requisite("Tira","Tira")
    # print(c.find()) # None

    # c = CoursePlan()
    # print(c.find())
    # c.add_course('course5')
    # c.add_requisite('course5','course5')
    # print(c.find())
    # c.add_course('course3')
    # c.add_course('course4')
    # c.add_requisite('course3','course4')
    # print(c.find())