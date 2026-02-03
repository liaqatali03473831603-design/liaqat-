#account {} storing User informatin
#key : account number
#value : another dictinary {Customer_name + Balance}
#for example
"""{
"101:{"name": "liaqat ali":5000.20}
}"""
account = {}
#Create_account
def Create_account():
    User_account = input("Enter Account Number")
    if User_account in accounts:
        print("Account already exists!")
    else:
        Name = input("Enter Account Holder Name: ")
        Balance = float("Enter Initial Balance: ")
        account[User_account] = {"name": Name, "balance": Balance}
        print("Account Created Successfully!")
#Deposite
def Deposit():
    User_account = input("Enter Account Number")
    if User_account in account:
        amount = float(input("Enter Amount to Deposit:"))
        accounts [User_account]["balance"] += amount
        print("Amount Deposited successfully!")
    else:
        print("Account not found!")
#Withdraw
def Withdraw():
     User_account = input("Enter Account Number")
     if User_account in accounts:
        amount = float(input("Enter Amount to Withdraw: "))
        if amount <= accounts[User_account]["balance"]:
            accounts [User_account]["balance"] -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient amount!")
     else:
        print("Account not fount!")
#Check_balance
def Check_balance():
     User_account = input("Enter Account Number")
     if User_account in account:
        print("Account Holder:",accounts[User_account]["name"])
        print("Balance:",accounts[User_account]["balance"])
     else:
        print("Account not found!")
#menu - driven
while True:
    print("==========Bank Management System==========")
    print("\nMenu")
    print("1.Create Account")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Check Balance")
    print("5.Exit\n")

    choice = input("Enter your choice(1/2/3/4/5) ")
    if choice == "1":
        choicereate_account()
    elif choice == "2":
        Deposit()
    elif choice == "3":
        Withdraw()
    elif choice == "4":
        Check_balance
    elif choice == "5":
        print("thanks for visiting Our Bank Management system")
        break
    else:
        print("invalid choice! choose again")
