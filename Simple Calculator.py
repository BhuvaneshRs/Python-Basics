def add(a,b):
 print(a+b)
def sub(a,b):
 print(a-b)
def mul(a,b):
 print(a*b)
def div(a,b):
 print(a/b)
a=int(input("Enter A"))
b=int(input("Enter B"))
C=int(input("1.add 2.sub 3.mul 4.div"))
if(C==1):
  add(a,b)
elif (C==2):  
  sub(a,b)
elif (C==3):  
  mul(a,b)
elif (C==4):
  div(a,b)
else:  
    print("enter valid option")

#Output:(1)
Enter A2
Enter B2
1.add 2.sub 3.mul 4.div1
4    

#Output:(2)
Enter A2
Enter B8
1.add 2.sub 3.mul 4.div4
0.25
