balance = 0
def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Deposited {amount}. New balance is: {balance}.")
    else:
        print("Deposit amount must be done bro.")

def withdraw(amount):
    global balance
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrew {amount}. New balance is: {balance}.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        print("Withdraw amount must be done bro.")

def display_balance():
    global balance
    print(f"Current balance is {balance}")


if __name__ == "__main__":
    deposit(1000)
    display_balance()  
    withdraw(500)
    display_balance()
    withdraw(300)  
    deposit(100)   
