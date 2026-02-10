peaple= int(input())
ans= list(map(int,input().split()))
if any(item==1 for item in ans):
    print("HARD")
else:
    print("EASY")