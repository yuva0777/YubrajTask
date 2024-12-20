balance = 5000
print("welcome to the ATM")
print("1. balance inquirey")
print("2. withdraw cash")
print("3. Deposite cash")
print("4. exit")
choice = int(input("Please enter your choice(1-4):"))
if choice==1:
    print(f"your current balance is: {balance}")
elif choice ==2:
    amount = int(input("Enter the amount to withdraw:"))
    if amount > balance:
        print("Insufficient balance.")
else:
    balance -= amount
    print(f"Withdraw succcessful! your new balance is: {balance}")
    if choice == 3:
        amount = int(input("Enter the amount to deposite:"))
        if amount <= 0:
            print("invalid amount. please enter a positive value.")
        else:
            balance += amount
        print(f"Deposite successful! your new balance is: {balance}")
    elif choice == 4:
         print("thank you for using the ATM. goodbye!")
    else:
        print("invalid choice. please try again.")

