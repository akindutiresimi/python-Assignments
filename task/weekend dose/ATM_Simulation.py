balance = 1000

while (True):
    atm = """
ATM 

Press 1 for Deposit
Press 2 for withdraw
Press 3 for checkbalance
press 4 Exit
"""     

    print(atm)
    ATM_menu = int(input("ATM menu: "))

    match ATM_menu:
        case 1:
            deposit = int(input("Enter Deposit: "))
            balance = deposit + balance
            print("balance: ", balance)

        case 2:
            withdraw = int(input("enter withdraw: "))
            if balance >= withdraw:
                balance = balance - withdraw
                print("Balance: ", balance)
            
            else:
                print("Insufficient fund")

        case 3:
            
            print("balance: ", balance)

        case 4:
            print("Exit")
            

