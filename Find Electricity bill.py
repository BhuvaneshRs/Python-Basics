print(" Under 50 units price Rs.0.50/Units \n Under 100 units Price Rs.0.75/Units \n under 250 Units price Rs.1.20/Units \n Above 250 units price Rs.1.50/Units")
units=float(input("Enter Units: "))
if units <=50:
  print(units*0.50,"is Your bill amount")
elif units <=100:
 print(units*0.75,"is Your bill amount")
elif units <=250:
 print(units*1.20,"is Your bill amount")
elif units >250:
 print(units*1.50,"is Your bill amount")

#Output:
Under 50 units price Rs.0.50/Units 
Under 100 units Price Rs.0.75/Units 
under 250 Units price Rs.1.20/Units 
Above 250 units price Rs.1.50/Units
Enter Units: 63.1
47.325 is Your bill amount
