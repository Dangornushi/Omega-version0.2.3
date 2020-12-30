from token import Token

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


While(open("test\\main.om").readlines()).run()