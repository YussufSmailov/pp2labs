def filter_prime(arr):
    cnt=0
    prime=[]
    for ch in arr:
        cnt=0
        for j in range(1, ch+1):
            if ch%j==0:
                cnt+=1
        if cnt==2:
            prime.append(ch)
    return prime


n=int(input("length of list "))
arr=[]
for i in range(n):
    q=int(input('enter a num'))
    arr.append(q)
print(filter_prime(arr))