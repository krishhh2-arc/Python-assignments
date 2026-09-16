def atm_simulation():
    balance = 1000.0
    pin = "1234"
    
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin != pin:
        print("Incorrect PIN. Access Denied!")
        return

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            print(f"Current Balance: ${balance:.2f}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited ${amount:.2f}. New Balance: ${balance:.2f}")
            else:
                print("Invalid deposit amount!")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= balance:
                balance -= amount
                print(f"Successfully withdrew ${amount:.2f}. Remaining Balance: ${balance:.2f}")
            elif amount > balance:
                print("Insufficient balance!")
            else:
                print("Invalid withdrawal amount!")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    atm_simulation()
              
