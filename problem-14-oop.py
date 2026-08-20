# Q: Bank Class

#  Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), pin (numeric type), name (name of the account owner as string type), balance.
#  Create a constructor with parameters: accountNumber, pin, name, balance.
#  Create a Deposit() method which manages the deposit actions.
#  Create a Withdrawal() method which manages withdrawals actions.
#  Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
#  Create a display() method to display account details. Give the complete code for the BankAccount class.

# Eg. After making above classes and methods, on executing below code:-

# newAccount = BankAccount(2178514584, "Mandy" , 2800)

# newAccount.Withdrawal(700)

# newAccount.Deposit(1000)

# newAccount.display()

# Output:
# Account Number :  2178514584
# Account Name :  Mandy
# Account Balance :  3100 ₹

class BankAccount:

    def __init__(self,accountNumber,pin,name,balance):
        self.accountNumber = accountNumber
        self.pin = pin
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Insufficient balance')

    def bankFees(self,fee):
        fee = self.balance * 0.05
        self.balance -= fee

    def display(self):
        print('Account number', self.accountNumber)
        print('Account name', self.name)
        print('Account balance', self.balance)

    def menu(self):
        user_input = input("""
        What do you want now ?
        1. Press 1 to Deposit
        2. Press 2 for Withdraw
        3. Want to exit
        """)

        if user_input == '1':
            amount = float(input('Enter your deposit amount: '))
            self.deposit(amount)
        elif user_input == '2':
            amount = float(input('Enter your withdrawal amount: '))
            self.withdraw(amount)
        else:
            exit()

accountNumber = int(input('Enter your account number: '))
pin = int(input('Enter your pin: '))
name = input('Enter your name: ')
balance = float(input('Enter your balance: '))

account = BankAccount(accountNumber, pin, name, balance)

account.menu()
account.display()