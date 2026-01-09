from datetime import datetime

fromatred_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
options = ["Create Account", "Inter Your Account", "Exit system"]
sub_options = [
    "Deposit", "Withdraw", "View Balance", "Transfer", "View Transactions",
    "Exit Account"
]
accounts = []


def create_account():
  id = input("Enter your id: ")
  for acount in accounts:
    if acount.id == id:
      print("Account already exists. Please try again.")
      menu()
      return
  name = input("Enter your name: ")
  account_type = input("Enter your account type (Personal/Business): ")
  transactions = []
  blance = 0
  account = ""
  if account_type.upper() == "P":
    account = Persoanl_Account(id, name, transactions, blance)
    account.transactions.append(f"Account created at {fromatred_date}")
  elif account_type.upper() == "B":
    account = Bussiness_Account(id, name, transactions, blance)
    account.transactions.append(f"Account created at {fromatred_date}")
  else:
    print("Invalid account type. Please try again.")
    menu()
    return

  accounts.append(account)
  account_info = account
  print(f"hi {account_info.name} Account created successfully.")
  print(f"Your account blance is {account_info.blance}$")
  print("*" * 55)
  menu()


def inter_your_account():
  account = ""
  if len(accounts) == 0:
    print("No accounts found. Please create an account first.")
    menu()
  id = int(input("Enter your id: "))
  Bank_Account.Active_system()
  for account in accounts:
    print("acount id", account.id)
    print("input id", id)
    if int(account.id) == id:
      while Bank_Account.system:
        print("ok")
        print("*" * 55)
        print(f"hello {account.name.upper()} Welcome to your account")
        for index, option in enumerate(sub_options, 1):
          print(f"{index}- {option}")
        choice = int(input("Enter your choice: "))
        print("*" * 55)
        if choice == 1:
          account.deposit()
        elif choice == 2:
          account.withdraw()
        elif choice == 3:
          account.view_balance()
        elif choice == 4:
          account.Transfer()
        elif choice == 5:
          account.view_transactions()
        elif choice == 6:
          menu()
          Bank_Account.stop_system()
        else:
          print("Invalid choice. Please try again.")
          Bank_Account.stop_system()
      else:
        print("Account not found. Please try again.")
        menu()


def menu():
  print("Welcome to our bank")
  for index, option in enumerate(options, 1):
    print(f"{index}- {option}")
  choice = int(input("Enter your choice: "))
  if choice == 1:
    create_account()
  elif choice == 2:
    inter_your_account()
  # elif choice == 3:
  #   system = False
  else:
    print("Invalid choice. Please try again.")
    menu()


class Bank_Account:
  system = True

  def __init__(
      self,
      id,
      name,
      transactions=[],
      blance=0,
  ):
    self.id = id
    self.name = name
    self.blance = blance
    self.transactions = transactions
    self.transactions.append(
        f"Account created with initial balance: {self.blance}$")

  def deposit(self):
    deposit_amount = float(input("Enter the amount you want to deposit:"))
    self.blance += deposit_amount
    if deposit_amount <= 0:
      print("Invalid deposit amount. Please enter a positive amount.")
    else:
      print(
          f"Deposit successful. you deposited {deposit_amount}$ at {fromatred_date}"
      )
      print("Your new balance is:", self.blance, "$")
      self.transactions.append(
          f"Deposited: {deposit_amount}$ at {fromatred_date}")

  def withdraw(self):
    amount = float(input("Enter the amount you want to withdraw:"))
    if amount <= 0:
      print("Invalid withdrawal amount. Please enter a positive amount.")
    if self.blance >= amount:
      self.blance -= amount
      self.transactions.append(f"Withdrew: {amount}$ at {fromatred_date}")
      print("Withdrawal successful")
    else:
      print("Insufficient funds")

  def view_balance(self):
    print("Your current balance is:", self.blance, "$")
    self.transactions.append(f"Viewed balance at {fromatred_date}")

  def view_transactions(self):
    print("your transactions are:")
    for transaction in self.transactions:
      print(f"#- {transaction}")
    self.transactions.append(f"Viewed transactions at {fromatred_date}")

  @staticmethod
  def stop_system():
    Bank_Account.system = False

  @staticmethod
  def Active_system():
    Bank_Account.system = True

  def Transfer(self):
    amount = float(input("Enter the amount you want to transfer:"))
    account_id = int(input("Enter the account id you want to transfer to: "))
    if int(amount) <= 0:
      print("Invalid transfer amount. Please enter a positive amount.")
      self.transactions.append("Failed transfer at {fromatred_date}")
      return
    if int(self.id) == account_id:
      print("You can't transfer to your own account.")
      self.transactions.append(f"Failed transfer to self at {fromatred_date}")
      return
    if self.blance >= amount:
      self.blance -= amount
      for one_account in accounts:
        if int(one_account.id) == int(account_id):
          # check account
          print("do you want to transfer to", one_account.name.upper(),
                "his id is", one_account.id)
          confirm = input("Enter y to confirm: ")
          if confirm.upper() == "Y":
            one_account.blance += amount
            self.transactions.append(
                f"Transferred: {amount}$ to {one_account.name} at {fromatred_date}"
            )
            one_account.transactions.append(
                f"Received: {amount}$ from {self.name} at {fromatred_date}")
            print("Transfer successful")
            print("Your new balance is:", self.blance, "$")
          else:
            print("Transfer cancelled")
            self.blance += amount
            return


class Persoanl_Account(Bank_Account):

  def __init__(self, id, name, transactions, blance=0):
    super().__init__(id, name, transactions, blance)


class Bussiness_Account(Bank_Account):

  def __init__(self, id, name, transactions, blance=0):
    super().__init__(id, name, transactions, blance)


menu()
