list=(list(map(int,input().split())))
min=list[0]
max=list[0]
for i in range(0,len(list)):
   if(max<list[i]):
    max=list[i]
for i in range(0,len(list)):
   if(min<list[i]):
    min=list[i]
avg=(max+min)/2
for i in range(len(list)):
    list[i]=avg
print(i)