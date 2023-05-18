import time
print("CREATE AN ACCOUNT")
time.sleep(1)
name=input('NAME = ').upper()
age=int(input("AGE = "))
Id=input("USER NAME =")
time.sleep(1)
print("Enter 4 digit pin _  _")
passw=int(input("PASSWORD ="))
c=0
while passw!=0:
    passw //=10
    c+=1
if c!=4:
    print("PLEASE ENTER 4 DIGIT PIN ")
    exit()
else:
    time.sleep(2)
    print("WELCOME TO THE LOGIN PAGE ")
    a2=input("USER NAME =")
if(a2==Id):
    a3=int(input("PASSWORD ="))
else:
    print("YOU DONT HAVE ANY ACCOUNT \n REGESTER YOUR SELF")
    exit()
a7=1000
if(a3!=passw):
    print(f"HELLO { name}")
    time.sleep(1)
    print("WELCOME TO THE BANK \n")
    print("||| 1000 SUCCESSFULLY CREDITED |||\n")
    time.sleep(2)

    a10=print('''    |1| FOR DEPOSITE
    |2| FOR CHECK ACCOUNT BALANCE
    |3| FOR WITHDRAW MONEY''')
    a4=int(input("ENTER  YOUR CHOICE "))
    
    if(a4==1):
        a5=int(input("ENTER THE AMOUNT = "))
        a6=a7+a5
        time.sleep(1)
        print(f"SUCCESSFULLY {a5} DEBITED TO YOUR ACCOUNT\n TOTAL AMOUNT YOU HAVE {a6}") 
      
    elif(a4==2):
        print(f"BALANCE {a7}")
    elif(a4==3):
        a8=int(input("ENTER THE AMOUNT TO WITHDRAW = "))
        a9=a7-a8
        print(f"DEBITED AMOUNT = {a8}\n TOTAL AMOUNT LEFT {a9}")
else:
    print("PASSWORD INCORRECT")




