from define import Define
from ifp import If
from whilep import While
from token import Token
import sys



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
