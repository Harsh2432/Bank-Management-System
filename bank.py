class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, name, initial_deposit):
        if name in self.customers:
            print("Account already exists")
            return
        self.customers[name] = initial_deposit
        print("Account created successfully")

    def deposit(self, name, amount):
        if name not in self.customers:
            print("Account does not exist")
            return
        self.customers[name] += amount
        print("Deposit successful")

    def withdraw(self, name, amount):
        if name not in self.customers:
            print("Account does not exist")
            return
        if self.customers[name] < amount:
            print("Insufficient balance")
            return
        self.customers[name] -= amount
        print("Withdrawal successful")

    def check_balance(self, name):
        if name not in self.customers:
            print("Account does not exist")
            return
        print(f"Balance: {self.customers[name]}")

bank = Bank()

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        name = input("\nEnter your name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        bank.create_account(name, initial_deposit)

    elif choice == 2:
        name = input("\nEnter your name: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(name, amount)

    elif choice == 3:
        name = input("\nEnter your name: ")
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(name, amount)

    elif choice == 4:
        name = input("\nEnter your name: ")
        bank.check_balance(name)

    elif choice == 5:
        break

    else:
        print("Invalid choice")
