class bank_account:
    def __init__(self):
      self.balance=0
      print(" Deposit  Withdrawal Machine")
 
    def deposit(self):
      amount=float(input("Enter amount to be Deposited: "))
      self.balance += amount
      print(" Amount Deposited:",amount)

    def withdraw(self):
      amount = float(input("Enter amount to be Withdrawn: "))
      if self.balance>=amount:
          self.balance-=amount
          print("You Withdrew:", amount)
   
  
    def display(self):
          print("Available Balance=",self.balance)
 
  
s=bank_account()

  
s.deposit()
s.withdraw()
s.display()
