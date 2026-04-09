def atm_simulation():
    correct_pin = "1234"
    balance = 50000.00
    pin_attempts = 3

    print("Welcome to Bharat Bank ATM")
    print("--------------------------")

    is_authenticated = False
    while pin_attempts > 0:
        entered_pin = input("Please enter your 4-digit PIN: ")
        
        if entered_pin == correct_pin:
            print("\n✅ PIN verified successfully!")
            is_authenticated = True
            break
        else:
            pin_attempts -= 1
            if pin_attempts > 0:
                print(f"❌ Incorrect PIN. You have {pin_attempts} attempts left.\n")
            else:
                print("❌ Too many incorrect attempts. Your card has been blocked.")
                return

    while is_authenticated:
        print("\n--- Main Menu ---")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            print(f"\n💰 Your current balance is: ₹{balance:.2f}")

        elif choice == '2':
            try:
                amount = float(input("\nEnter amount to withdraw: ₹"))
                if amount <= 0:
                    print("⚠️ Please enter a valid amount greater than 0.")
                elif amount > balance:
                    print("❌ Insufficient balance! Your transaction cannot be processed.")
                else:
                    balance -= amount
                    print(f"✅ Successfully withdrew ₹{amount:.2f}.")
                    print(f"💰 Your new balance is: ₹{balance:.2f}")
            except ValueError:
                print("⚠️ Invalid input. Please enter numbers only.")

        elif choice == '3':
            try:
                amount = float(input("\nEnter amount to deposit: ₹"))
                if amount <= 0:
                    print("⚠️ Please enter a valid amount greater than 0.")
                else:
                    balance += amount
                    print(f"✅ Successfully deposited ₹{amount:.2f}.")
                    print(f"💰 Your new balance is: ₹{balance:.2f}")
            except ValueError:
                print("⚠️ Invalid input. Please enter numbers only.")

        elif choice == '4':
            print("\nThank you for using Bharat Bank ATM. Goodbye! 👋")
            break

        else:
            print("\n⚠️ Invalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    atm_simulation()