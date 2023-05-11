ch=input("Enter single Character:")
if ch>="A" and ch<="Z":
 print(ch," is an Uppercase")
elif ch>="a" and ch<="z":
 print(ch," is an Lowercase")
elif ch>="0" and ch<="9":
 print(ch," is an Number or Integer")
else:
  print(ch," is an Special Character")
 
#Output:
Enter single Character:5
5  is an Number or Integer

Enter single Character:s
s  is an Lowercase

Enter single Character:(
(  is an Special Character
