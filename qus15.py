#find the duplicate in the array
list=(list(map(int,input().split())))
v=[]
for i in list:
    if i not in v:
       v.append(i)
print(i)
    