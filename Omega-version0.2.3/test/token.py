from vm import Vm

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


