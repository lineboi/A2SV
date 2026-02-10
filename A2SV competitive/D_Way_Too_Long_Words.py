n= int (input())
word=[]
for i in range (n):
    word.append(input())
for w in word:
    if len(w)<=10:
        print (w)
    else:
        first=w[:1]
        size=len(w)
        last=w[size-1:]
        le=len(w)-2
        wor=f"{first}{le}{last}"
        print(wor)
