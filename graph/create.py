class graph :
    def __init__(self) :
        self.graph={}
        self.count=0
    def addv(self,a):
            if a in self.graph :
                 print(f"{a} already exist")
            else:
                 self.graph[a]=[]
                 self.count +=1
    def adde(self,v1,v2,a=0) :
         if v1 in self.graph and v2 in self.graph[v1] :
              print(f"{v1} to {v2} connection already exist")
         else :
             temp=[v2,a]
             self.graph[v1].append(temp)
    def __str__(self) :
         return str(self.graph)

a=graph()
a.addv(10)
a.addv(32)
a.addv(17)
a.addv(14)
a.addv(7)
a.addv(23)
a.addv(42)
a.addv(11)
a.addv(27)
a.addv(347)
a.addv(153)
a.addv(22)
a.adde(10,32,4)
a.adde(17,14,5)
a.adde(42,14,5)
a.adde(23,14,5)
a.adde(11,14,5)
a.adde(153,7,5)
a.adde(10,22,5)
a.adde(32,27,5)
a.adde(42,11,5)
print(a)
