class Transaction:
  def __init__(self, amount, type):
    self.amount = amount
    self.type = type 

class Account:
  def __init__(self, name, account_number, balance):
    self.name = name
    self.account_number = account_number
    self.balance = balance
    self.transactions = []
  def deposit(self, amount):
    self.balance += amount
    self.transactions.append(Transaction(amount, "Deposit"))

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds")
      return
    self.balance -= amount
    self.transactions.append(Transaction(amount, "Withdrawal"))

  def get_balance(self):
    return self.balance

  def show_transactions(self):
    print("Transaction History:")
    for transaction in self.transactions:
      print(f"{transaction.type}: £{transaction.amount}")

def main():
  # Initialize empty account
  current_account = None

  while True:
    print("\nMy Bank Account")
    print("1. Create New Account")
    print("2. Select Existing Account")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      name = input("Enter your name: ")
      account_number = int(input("Enter your account number: "))
      balance = float(input("Enter your initial balance: "))
      current_account = Account(name, account_number, balance)
      print("Account created successfully!")

    elif choice == "2":
      if current_account is None:
        print("Please create an account first.")
        continue

      while True:
        print("\nAccount Management")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Go Back")

        choice = input("Enter your choice: ")

        if choice == "1":
          amount = float(input("Enter deposit amount: "))
          current_account.deposit(amount)
          print(f"Deposited £{amount}.")

        elif choice == "2":
          amount = float(input("Enter withdrawal amount: "))
          current_account.withdraw(amount)

        elif choice == "3":
          print(f"Current Balance: £{current_account.get_balance()}")

        elif choice == "4":
          current_account.show_transactions()

        elif choice == "5":
          break

        else:
          print("Invalid choice.")

    elif choice == "3":
      print("Exiting...")
      break

    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()