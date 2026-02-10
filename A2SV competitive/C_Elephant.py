n= int(input())
steps=[1,2,3,4,5]
count=0
while n>0:
    if n>5:
        count+=1
        n-=5
    else:
        count+=1
        break

print(count)
