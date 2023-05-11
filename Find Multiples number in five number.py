num1=(int(input("Enter First Number")))
num2=(int(input("Enter Second Number")))
num3=(int(input("Enter Thired Number")))
num4=(int(input("Enter Fourth Number")))
num5=(int(input("Enter Fifth Number")))
divisor=(int(input("Enter Divisor number")))
count=0
print("Multiples of", divisor,"are:")
if(num1%divisor==0):
  print(num1)
  count+=1
if(num2%divisor==0):
  print(num2)
  count+=1
if(num3%divisor==0 ):
  print(num3)
  count+=1
if(num4%divisor==0):
  print(num4)
  count+=1
if(num5%divisor==0):
  print(num5)
  count+=1
print()
print(count,"multiples of ", divisor,"found")

#Output:
Enter First Number15
Enter Second Number15
Enter Thired Number65
Enter Fourth Number45
Enter Fifth Number48
Enter Divisor number15
Multiples of 15 are:
15
15
45

3 multiples of  15 found
