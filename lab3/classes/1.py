class Output:
    def __init__(self):
       pass
    def getstring(self):
        self.name=input("vvedi chtoto: ")
    def printstring(self):
        print(self.name.upper())

chtoto=Output()
chtoto.getstring()
chtoto.printstring()