balance = 5000
pin = "1234"
entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    print("PIN verified successfully.\n")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    if choice == '1':
        print(f"Your current balance is: ₹{balance}\n")

    elif choice == '2':
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance = balance + amount
            print(f"₹{amount} deposited successfully.\n")
            print(f"Updated Balance: ₹{balance}")
        else:
            print("Invalid amount. Please enter a positive number.\n")

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print(f"₹{amount} withdrawn successfully.\n")
            print(f"Updated Balance: ₹{balance}")
        else:
            print("Insufficient balance or invalid amount.\n")

    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")

    else:
        print("Invalid option. Please choose between 1 to 4.\n")

else:
    print("Incorrect PIN. Access Denied.\n")
