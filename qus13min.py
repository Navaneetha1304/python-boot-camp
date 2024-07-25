list=(list(map(int,input().split())))
min=list[0]
for i in range(0,len(list)):
    if(list[i]>min):
        maxi=list[i]
        print(min)