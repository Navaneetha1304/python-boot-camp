list=(list(map(int,input().split())))
max=list[0]
for i in range(max,len(list)):
    if(list[i]<max):
        maxi=list[i]
print(max)