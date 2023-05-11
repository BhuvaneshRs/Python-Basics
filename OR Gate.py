#OR Gate
print("OR gate")
a=int(input("Enter 1 or 0 value:"))
b=int(input("Enter 1 or 0 value:"))
if(a==0 or b==0):
 print("False")
elif(a==1 or b==0):
 print("True")
elif(a==0 or b==1):
 print("True")
elif(a==1 or b==1):
 print("True")
else:
 print("enter correct value")

#Output(1)
OR gate
Enter 1 or 0 value:0
Enter 1 or 0 value:0
False

#Output(2)
OR gate
Enter 1 or 0 value:1
Enter 1 or 0 value:0
True

#Output(3)
OR gate
Enter 1 or 0 value:0
Enter 1 or 0 value:1
True

#Output(4)
OR gate
Enter 1 or 0 value:1
Enter 1 or 0 value:1
True
