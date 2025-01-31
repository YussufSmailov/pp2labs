class answer:
    def __init__(self):
        self.userstr = ''
    def getstring(self):
        self.userstr = str(input())
    def printstring(self):
        self.userstr = print(self.userstr.upper())
        self.userstr
ans = answer()
ans.getstring()
ans.printstring()