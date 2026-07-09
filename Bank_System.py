# ---------------------------------
# Bank Account System
# ---------------------------------

class Account:

    account_counter = 1000

    # Static Method
    @staticmethod
    def generate_account_number():
        Account.account_counter += 1
        return Account.account_counter

    def __init__(self, owner, balance):
        self.owner = owner
        self.account_number = Account.generate_account_number()

        # Encapsulation
        self.__balance = balance

    # Instance Methods
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{self.__balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    # Magic Method
    def __str__(self):
        return f"Account[{self.account_number}] Owner: {self.owner}, Balance: ₹{self.__balance}"


# ---------------------------------
# Savings Account
# ---------------------------------

class SavingsAccount(Account):

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        parent_info = super().__str__()
        return f"{parent_info}, Interest Rate: {self.interest_rate}%"


# ---------------------------------
# Current Account
# ---------------------------------

class CurrentAccount(Account):

    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        parent_info = super().__str__()
        return f"{parent_info}, Overdraft Limit: ₹{self.overdraft_limit}"


# ---------------------------------
# Banking System
# ---------------------------------

accounts = []


def create_account():
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    acc_type = input("Type (1: Savings, 2: Current): ")

    if acc_type == "1":
        rate = float(input("Enter interest rate: "))
        acc = SavingsAccount(name, balance, rate)

    elif acc_type == "2":
        limit = float(input("Enter overdraft limit: "))
        acc = CurrentAccount(name, balance, limit)

    else:
        print("Invalid account type.")
        return

    accounts.append(acc)
    print("Account created successfully!\n")


def view_accounts():

    if len(accounts) == 0:
        print("No accounts found.")
        return

    for acc in accounts:
        print(acc)


def deposit_money():

    acc_no = int(input("Enter account number: "))
    amount = float(input("Enter amount: "))

    for acc in accounts:
        if acc.account_number == acc_no:
            acc.deposit(amount)
            return

    print("Account not found.")


def withdraw_money():

    acc_no = int(input("Enter account number: "))
    amount = float(input("Enter amount: "))

    for acc in accounts:
        if acc.account_number == acc_no:
            acc.withdraw(amount)
            return

    print("Account not found.")


def menu():

    while True:

        print("\n====== Bank Menu ======")
        print("1 Create Account")
        print("2 View Accounts")
        print("3 Deposit")
        print("4 Withdraw")
        print("5 Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            view_accounts()

        elif choice == "3":
            deposit_money()

        elif choice == "4":
            withdraw_money()

        elif choice == "5":
            break

        else:
            print("Invalid choice")


menu()