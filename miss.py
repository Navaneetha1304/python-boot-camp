#find the missing number in array
list=(list(map(int,input().split())))
n=int(input())
sum=0
for i in range(0,len(list)):
    sum=sum+list[i]
num=(n*(n+1))//2
print(num-sum)