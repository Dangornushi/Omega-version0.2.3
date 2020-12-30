class Define:
    
    def __init__(self, data):
        self.data = data
        self.datade = None
        self.funcname = "del"
    
    def run(self):
        dick = {}
        lis = []
        lis2 = []
        i = 0
        
        for datav in self.data:
            datav = datav.replace("\n", "").replace("", "")
            lis.append(datav)
        
        for data in lis:
            
            if data.startswith("define"):
                i+=1
                self.datade = data.replace("define", "")

            if self.datade == str(i):
                self.funcname = lis[lis.index("define"+self.datade)+1]
            
            valis = "".join(lis).split("define")
            valis = "".join(valis).split(":")
            dick[self.funcname] = valis
        
        dicklist = dick.pop("del")
        dicklist.pop(0)
        for dilis in dicklist:
            if dilis.endswith("()"):
                lis2.append(dilis)
                dicklist.pop(dicklist.index(dilis))
        dick = dict(zip(lis2, dicklist))
        return dick


Define(open("test\\main.om").readlines()).run()