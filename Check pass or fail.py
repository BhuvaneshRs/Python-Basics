#Validating pass or fail using internal and external mark 
Internal_mark=int(input("Enter internal mark out of 20:"))
if(Internal_mark<=20 and Internal_mark>=12):
 External_mark=int(input("Enter external mark out of 80:"))
 if(External_mark<=80 and External_mark>=40):
  print("pass")
 else:
  print("Internal pass and external fail")
else:
 print("internal fail")
 
 
#Output:(1)
Enter internal mark out of 20:19
Enter external mark out of 80:70
pass

#Output:(2)
Enter internal mark out of 20:15
Enter external mark out of 80:22
Internal pass and external fail

#Output:(3)
Enter internal mark out of 20:10
internal fail
