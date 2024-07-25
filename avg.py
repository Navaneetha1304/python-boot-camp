my_list=list(map(int,input().split(",")))
count=0
sum=0
for i in range(0,len(my_list),2):
  count+=1
sum=sum+my_list[i]
avg=sum/count
print(avg)

