a=(int(input("Enter a value: ")))
b=(int(input("Enter b value: ")))
c=(int(input("Enter c value: ")))
min,mid,max=a,b,c;
if(a<b and a<c):
  if a<b:
    min,mid,max=a,b,c
  else:
    min,mid,max=a,b,c
elif(b<c and b<a):
  if b<c:
    min,mid,max=b,a,c
  else:
    min,mid,max=b,c,a
else:
  if x<y:
    min,mid,max=c,a,b
  else:
    min,mid,max=c,b,a
print(min,mid,max)

#Output:
Enter a value: 5
Enter b value: 4
Enter c value: 9
4 5 9
