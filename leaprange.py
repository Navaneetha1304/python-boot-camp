a=int(input("enter the year"))
b=int(input("enter the year"))
for i in range (a,b):
  if (i%4==0)and(i%100!=0):
   print(i)