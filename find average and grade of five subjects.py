tamil=float(input("Enter Tamil mark:"))
english=float(input("Enter English mark:"))
maths=float(input("Enter Maths mark:"))
science=float(input("Enter Science mark:"))
social=float(input("Enter Social mark"))
print("\n")
avg = tamil + english + maths + science + social
print("Your Total Mark is",avg)
fail=0
if tamil<40:
  print("Tamil Subject is Fail")
  fail+=1
if english<40:
  print("English Subject is Fail")
  fail+=1
if maths<40:
  print("Maths subject is Fail")
  fail+=1
if science<40:
  print("Science subject is Fail")
  fail+=1
if social<40:
  print("Social Subjet is fail")
  fail+=1
per=avg/5
if fail==0:
  if(per>=90):
    print("You Secure A Grade, V.Good")
  elif(per>=80):
    print("You Secure B Grade, Good")
  elif(per>=70):
    print("You Secure C Grade, Not Bad")
  elif(per>=60):
    print("You Secure D Grade, Try to improve")
  elif(per>=40):
    print("You Secure E Grade, Try to make hardwok")
else:
  print("You are not eligible to Grade, because you fail in",fail,"Subjects")
  
#Output:
Enter Tamil mark:15
Enter English mark:65
Enter Maths mark:98
Enter Science mark:69
Enter Social mark39.9


Your Total Mark is 286.9
Tamil Subject is Fail
Social Subjet is fail
You are not eligible to Grade, because you fail in 2 Subjects
