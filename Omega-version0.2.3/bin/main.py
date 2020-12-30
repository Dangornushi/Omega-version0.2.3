import sys, os,re

#TODO:define
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


#TODO:if
class If:
    
    def __init__(self, data):
        self.data = data.split(" ")
    
    def run(self, dick, lis, i):
        if self.data[2] == "==":
            if dick[self.data[1]] == self.data[3]:
                token = Token(self.data[5].replace("{", "").replace("}", ""))
                token.run(dick, lis, i)
        
        elif self.data[2] == "<":
            if int(dick[self.data[1]]) < int(self.data[3]):
                token = Token(self.data[5].replace("{", "").replace("}", ""))
                token.run(dick, lis, i)
    
        elif self.data[2] == ">":
            if int(dick[self.data[1]]) > int(self.data[3]):
                token = Token(self.data[5].replace("{", "").replace("}", ""))
                token.run(dick, lis, i)


#TODO:while処理
class While:
    
    def __init__(self, data):
        self.datalis = data.split(" ")

    def run(self, dick, lis, i):
        for lis in self.datalis:
            if lis.startswith("while"):
                lis = lis.split("=")
                func = lis[1].replace("{", "").replace("}", "")
                num = "".join(lis[0]).split("_")[1]
                if num == "True":
                    while True:
                        token = Token(func)
                        token.run(dick, lis, i)
                for i in range(int(num)):
                    token = Token(func)
                    token.run(dick, lis, i)


#TODO:仮想機械
class Vm:
    
    def __init__(self, inp):
        self.data = inp

    def run(self, dick, lis, i):
        
        self.data = "".join(self.data).replace("\n", "")
        self.datalis = self.data.split("_")
        valdata = Define(open(sys.argv[1], encoding="utf-8").readlines()).run()

        try:
            self.data = self.data.replace(";", "")
            if self.data.startswith("move"):
                #TODO:val = 要素
                val = self.datalis[2]
                dick[self.datalis[1]] = val
            
            elif self.data.startswith("add"):
                try:
                    val = int(dick[self.datalis[2]]) + int(dick[self.datalis[3]])
                    dick[self.datalis[1]] = val

                except KeyError:
                    print("値を参照できません(add)")
            
            elif self.data.startswith("mull"):
                try:
                    val = int(dick[self.datalis[2]]) / int(dick[self.datalis[3]])
                    dick[self.datalis[1]] = val
                
                except KeyError:
                    print("値を参照できません(mull)")
            
            elif self.data.startswith("mult"):
                try:
                    val = int(dick[self.datalis[2]]) * int(dick[self.datalis[3]])
                    dick[self.datalis[1]] = val
                
                except KeyError:
                    print("値を参照できません(mult)")

            elif self.data.startswith("subt"):
                try:
                    val = int(dick[self.datalis[2]]) - int(dick[self.datalis[3]])
                    dick[self.datalis[1]] = val
                
                except KeyError:
                    print("値を参照できません(変数ではありません:subt)")
        
            elif self.data.startswith("str"):
                val = self.datalis[2]
                dick[self.datalis[1]] = val
            
            if self.data.startswith("define"):
                valdata = Define(open(sys.argv[1], encoding="utf-8").readlines()).run()

            elif self.data.startswith("println"):
                try:
                    print(dick[self.datalis[self.datalis.index("println")+1]])
                
                except KeyError:
                    print(self.datalis[self.datalis.index("println")+1])
            
            elif self.data.endswith("()") and self.data.startswith("    ") is False:
                for val in valdata[self.data].split(";"):

                    if val.endswith("()") and val.startswith("    ") is False:
                        val = val.replace(val, "")

                    elif re.match(r'[0-9]+', val):
                        val = re.sub(r'[0-9]+', '', val)
                    
                    elif val.startswith("return "):
                        val = val.replace(val, "")
                        lis.append(val)
                        

                    elif val == "    end":
                        break

                    token = Token(val.replace(";", "").replace("    ", ""))
                    token.run(dick, lis, i)

            elif self.data.startswith("exit"):
                sys.exit()
            
            elif self.data.startswith("if"):
                If(self.data).run(dick, lis, i)
            
            elif self.data.startswith("input"):
                self.data = self.data.split('"')
                val = input("{}".format(self.data[1]))
                dick[self.data[2]]= val
            
            elif self.data.startswith("while"):
                self.data = self.data.replace(" ", "")
                While(self.data).run(dick, lis, i)
            

        except IndexError:
            print("代入対象を特定できません")
        
        with open("set.oms", "a") as fi:
            print(self.data, file=fi)


#TODO:トランスパイル
class Token:
    
    def __init__(self, data):
        self.data = data

    def run(self,dick, lis, i):
        self.data = self.data.split("//")[0].replace("\n", "").replace(";", "")

        if self.data.startswith("let"):
            self.data = self.data.replace("let ", "move _").replace("=", "_").split(" ")

        elif self.data.startswith("<+>"):
            self.data = self.data.replace("<+> ", "add _").replace("=", "_").replace("+", "_").split(" ")
        
        elif "-" in self.data:
            self.data = self.data.replace("calc ", "subt _").replace("=", "_").replace("-", "_").split(" ")
        
        elif self.data.startswith("</>"):
            self.data = self.data.replace("</> ", "mull _").replace("=", "_").replace("/", "_").split(" ")

        elif self.data.startswith("<*>"):
            self.data = self.data.replace("<*> ", "mult _").replace("=", "_").replace("*", "_").split(" ")
        
        elif self.data.startswith("def"):
            self.data = self.data.replace("def", "define{}".format(i))
            i += 1

        vm = Vm(self.data)
        vm.run(dick, lis, i)


#TODO:Main / カーネル
class Main:
    def __init__(self):
        pass

    #TODO:data = すべてのデータ
    def run(self, dick, lis):
        valts = []
        i = 1
        
        name = sys.argv[1]
        file = open(name, encoding="utf-8")
        data = file.readlines()
        file.close()

        valts.append(data)
        valts = [e for inner_list in valts for e in inner_list]
        for data in valts:
            token = Token(data)
            token.run(dick, lis, i)


if __name__ == '__main__':
    if os.path.isfile("set.oms"):
        os.remove("set.oms")
    dick = {}
    lis = []
    omega = Main()
    omega.run(dick, lis)
