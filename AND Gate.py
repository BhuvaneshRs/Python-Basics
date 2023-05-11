#AND Gate
print("And gate")
a=int(input("Enter 1 or 0 value:"))
b=int(input("Enter 1 or 0 value:"))
if(a==0 and b==0):
 print("False")
elif(a==1 and b==0):
 print("False")
elif(a==0 and b==1):
 print("False")
elif(a==1 and b==1):
 print("True")
else:
 print("enter correct value")

Output:(1)
And gate
Enter 1 or 0 value:0
Enter 1 or 0 value:0
False

Output:(2)
And gate
Enter 1 or 0 value:0
Enter 1 or 0 value:1
False

Output:(3)
And gate
Enter 1 or 0 value:1
Enter 1 or 0 value:0
False

Output:(4)
And gate
Enter 1 or 0 value:1
Enter 1 or 0 value:1
True
