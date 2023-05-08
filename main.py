age=(int(input("Enter Your Age")))
State=(str(input("TamilNadu or Other state")))
Aadhar=(int(input("Enter Aadhar Number")))
Phone=(int(input("Enter Phone Number")))
if ((age>=18) and (State=="Tamilnadu")) and (Aadhar in range(111111111111,999999999999) or (Phone in range(6543217890,9999999999))):
    print("You are eligible to vote")
else:
    print("Not eligible to vote")