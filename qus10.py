k=int(input())
list=(list(map(int,input().split())))
if (k<=len(list)):
    print(list[k])
else:
     print(list[k%len(list)])