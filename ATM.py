user_pin = int(1506)
for i in range(3):
    input_pin = int(input("Enter your 4-digit pin: "))
    if input_pin == user_pin:
        break
    elif i ==0:
        print("Wrong Pin, You have 2 tries left")
    elif i == 1:
        print("Wrong Pin, You have 1 tries left")
    elif i == 2:
        print("Your Account Has been blocked!!!")
        exit()
print("Welcome To ATM")
balance = 999.00
while True:
    print(""" 
    1) Check Balance
    2) Deposit
    3) Withdraw
    4) Exit
    """)
    choice = int(input("Enter Choice: "))
    if choice == 1 :
        print("Balance: ",balance)
    elif choice == 2 :
        depo = int(input("Enter Amount: "))
        s500 = depo//500
        d500 = depo-(s500*500)
        s100 = d500//100
        print("Please Put ",s500," $500 Notes")
        if s100 >0 :
            print("Please Put ",s100," $100 Notes")
        print("Deposit Successful")
        balance = balance + depo
    elif choice == 3:
        withdr = int(input("Enter Amount of Withdrawal: "))
        if withdr > balance:
            print("Insufficient Funds")
        elif withdr <= 0 or withdr % 100 != 0:
            print("Please Enter Valid Value in the Multiples of 100")
            continue
        else :
            s500 = withdr // 500
            d500 = withdr - (s500 * 500)
            s100 = d500 // 100
            d100 = d500 - (s100 * 100)
            n100 = withdr // 100
            if n100 > 1 :
                r100 = input("Do you need Amount in 100s (y/n): ")
                if r100.lower() == 'y':
                    print("Please Take ", n100, " $100 Notes")
                else:
                    print("Please Take ", s500, " $500 Notes")
            if s100 > 0:
                print("Please Take ", s100, " $100 Notes")
            print("Take your Amount of ", withdr)
            balance = balance - withdr
            print("New Balance: ",balance)
    elif choice == 4:
        confirm = input("Are you sure to exit (y/n): ")
        if confirm.lower() == 'y':
            print("Thanks For Using, Visit Again.")
            break
        else:
            continue
    else:
        print("Invalid Input, Please Try Again !")