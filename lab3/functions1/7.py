def has_33(nums):
    for i in range(len(nums)):
        if i>0 and i<len(nums)-1:
            if(nums[i]==3 and nums[i-1]==3) or (nums[i]==3 and nums[i+1]==3):
                return "True"
        elif i==0:
            if nums[i]==3 and nums[i+1]==3:
                return "True"
        else:
            if nums[i]==3 and nums[i-1]==3:
                return "True"
        
    return "False"



n=int(input("length of list "))
nums=[]
for i in range(n):
    q=int(input('enter a num '))
    nums.append(q)
print(has_33(nums))