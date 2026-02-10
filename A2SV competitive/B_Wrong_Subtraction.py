inputs=list(map(int,input().split()))
n=inputs[0]
times=inputs[1]
for i in range (times):
    num=str(n)
    if int(num[-1])==0:
        n=n//10
    else:
        n=n-1
print (n)