radius=(float(input("Enter Radius: ")))
print("1.calculate Area \n 2.Calculate Perimeter")
choice=(int(input("Enter 1 or 2: ")))
if choice==1:
  print(3.1459*radius*radius,"is area")
else:
  print(2*3.1459*radius,"is perimeter")
  
#Output:(1)
Enter Radius: 3.12
1.calculate Area 
2.Calculate Perimeter
Enter 1 or 2: 1
30.62344896 is area

#Output:(2)
Enter Radius: 3.12
1.calculate Area 
2.Calculate Perimeter
Enter 1 or 2: 2
19.630416 is perimeter
