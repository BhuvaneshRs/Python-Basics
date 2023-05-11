#Elif Condition
A=int(input("Enter A value:"))
B=int(input("Enter B value:"))
C=int(input("1.add 2.sub 3.mul 4.div"))
if(C==1):
  print(A+B)
elif (C==2):  
  print(A-B)
elif (C==3):  
  print(A*B)
elif (C==4):
  print(A/B)
else:  
    print("enter valid option")

#Output(1)
Enter A value:20
Enter B value:30
1.add 2.sub 3.mul 4.div 2
-10

#Output(2)
Enter A value:20
Enter B value:30
1.add 2.sub 3.mul 4.div 1
50

#Output(3)
Enter A value:2
Enter B value:3
1.add 2.sub 3.mul 4.div 3
6

#Output(4)
Enter A value:4
Enter B value:2
1.add 2.sub 3.mul 4.div 4
2

#Output(5)
Enter A value:20
Enter B value:30
1.add 2.sub 3.mul 4.div 10
enter valid option
