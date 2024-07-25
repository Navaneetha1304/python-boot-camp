k=3
n=2
k=int(input())
n=int(input())
list=(list(map(int,input().split())))
if k+n>len(list): 
    print("error")
else:
   for i in range(0,k+n+1):
    if(i==k+n):
      print(list)
    