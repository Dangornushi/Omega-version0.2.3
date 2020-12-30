from token import Token

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


Define(open("test\\main.om").readlines()).run()