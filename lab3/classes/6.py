class Prime:
    def __init__ (self, arr):
        self.arr=arr
    def filprime(self, x):
        cnt=0
        for i in range(1, x+1):
            if x%i==0:
                cnt+=1
        if cnt==2:
            return True
        else:
            return False
    def lam(self):
        ans=list(filter(lambda x: self.filprime(x), self.arr))
        self.ans=ans
    def __str__ (self):
        return f"prime list is {self.ans}"
arr=[x for x in range(10)]
answer=Prime(arr)
answer.lam()
print(answer)

        

# def qwe(x):
#     ans=[]
    # cnt=0
    # for i in range(1, x+1):
    #     if x%i==0:
    #      cnt+=1
    # if cnt==2:
    #    return True
    # else:
    #    return False

# arr=[1, 5, 7, 5, 4, 8, 12, 20, 31, 23]

# print(list(filter(lambda x: qwe(x), arr)))
