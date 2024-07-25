my_list=list(map(int,input().split(",")))
choice=int(input())
if choice==1:
    print(my_list.append(5))
elif choice==2:
  my_list.pop(1)
  print(*my_list)
elif choice==3:
   my_list.sort()
    print(*my_list)
else:
    print(len(my_list))
    





