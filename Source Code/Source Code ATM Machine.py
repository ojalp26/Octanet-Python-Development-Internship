from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class ATM:
    def __init__(self):
        # Initialize the ATM with a default account balance, PIN, and empty transaction history
        self.balance = 1000  # Default balance
        self.pin = "1234"    # Default PIN
        self.transaction_history = []

    def display_menu(self):
        # Display the ATM menu options in a table format
        menu = [
            ["1", "Account Balance Inquiry"],
            ["2", "Cash Withdrawal"],
            ["3", "Cash Deposit"],
            ["4", "PIN Change"],
            ["5", "Transaction History"],
            ["6", "Exit"]
        ]
        print(Fore.CYAN + "\n" + "=" * 40)
        print(Fore.YELLOW + "Welcome to the ATM Machine")
        print(Fore.CYAN + "=" * 40)
        print(tabulate(menu, headers=["Option", "Action"], tablefmt="pretty"))
        print(Fore.CYAN + "=" * 40)

    def account_balance_inquiry(self):
        # Display the current account balance in a table
        print(Fore.GREEN + "\n" + "=" * 40)
        print(Fore.YELLOW + "Account Balance Inquiry")
        print(Fore.GREEN + "=" * 40)
        print(tabulate([[f"${self.balance}"]], headers=["Current Balance"], tablefmt="pretty"))
        print(Fore.GREEN + "=" * 40)

    def cash_withdrawal(self):
        # Withdraw cash from the account
        print(Fore.GREEN + "\n" + "=" * 40)
        print(Fore.YELLOW + "Cash Withdrawal")
        print(Fore.GREEN + "=" * 40)
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > self.balance:
            print(Fore.RED + "Insufficient balance!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            print(Fore.GREEN + f"${amount} has been withdrawn.")
            self.account_balance_inquiry()
        print(Fore.GREEN + "=" * 40)

    def cash_deposit(self):
        # Deposit cash into the account
        print(Fore.GREEN + "\n" + "=" * 40)
        print(Fore.YELLOW + "Cash Deposit")
        print(Fore.GREEN + "=" * 40)
        amount = float(input("Enter the amount to deposit: $"))
        self.balance += amount
        self.transaction_history.append(f"Deposit: ${amount}")
        print(Fore.GREEN + f"${amount} has been deposited.")
        self.account_balance_inquiry()
        print(Fore.GREEN + "=" * 40)

    def pin_change(self):
        # Change the PIN
        print(Fore.GREEN + "\n" + "=" * 40)
        print(Fore.YELLOW + "PIN Change")
        print(Fore.GREEN + "=" * 40)
        old_pin = input("Enter your old PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print(Fore.GREEN + "PIN changed successfully!")
            else:
                print(Fore.RED + "PINs do not match. PIN change failed.")
        else:
            print(Fore.RED + "Incorrect old PIN. PIN change failed.")
        print(Fore.GREEN + "=" * 40)

    def transaction_history_view(self):
        # Display the transaction history in a table
        print(Fore.GREEN + "\n" + "=" * 40)
        print(Fore.YELLOW + "Transaction History")
        print(Fore.GREEN + "=" * 40)
        if not self.transaction_history:
            print(Fore.RED + "No transactions have been made yet.")
        else:
            print(tabulate([[t] for t in self.transaction_history], headers=["Transaction"], tablefmt="pretty"))
        print(Fore.GREEN + "=" * 40)

    def run(self):
        # Main loop to run the ATM simulation
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-6): ")

            if choice == "1":
                self.account_balance_inquiry()
            elif choice == "2":
                self.cash_withdrawal()
            elif choice == "3":
                self.cash_deposit()
            elif choice == "4":
                self.pin_change()
            elif choice == "5":
                self.transaction_history_view()
            elif choice == "6":
                print(Fore.YELLOW + "\nThank you for using the ATM. Goodbye!")
                break
            else:
                print(Fore.RED + "\nInvalid choice. Please try again.")

# Create an instance of the ATM and run the simulation
atm = ATM()
atm.run()
