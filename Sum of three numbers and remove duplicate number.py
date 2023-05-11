x=int(input("Enter Number a"))
y=int(input("Enter Number b"))
z=int(input("Enter Number c"))
sum1=x+y+z
print("Sum of Three Numbers is ",sum1)
if(x==y):
  print("Duplicate value are x and y and sum of non duplicate value is", z)
elif(x==z):
  print("Duplicate value are x and z and sum of non duplicate value is", y)
elif(y==z):
  print("Duplicate value are y and z and sum of non duplicate value is", x)
else:
  print("No duplicate value sum of three is", sum1)
  
#Output:(1)
Enter Number a5
Enter Number b6
Enter Number c1
Sum of Three Numbers is  12
No duplicate value sum of three is 12

#Output:(2)
Enter Number a5
Enter Number b5
Enter Number c2
Sum of Three Numbers is  12
Duplicate value are x and y and sum of non duplicate value is 2
