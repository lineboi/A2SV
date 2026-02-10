n = int (input())
    lis=[]
cout=0
for i in range (n):
    inp=list (map(int,input().split()))
    lis.append(inp)

for l in lis:
    if l.count(1)>1:
        cout+=1
print (cout)
