def withdraw_balance(current_balance, amount):
    if amount > current_balance:
        print("Insufficient funds")
        return current_balance
    new_balance = current_balance - amount
    return new_balance

current_balance = 1000 
print("Initial balance:", current_balance)

withdraw_amount = 300
current_balance = withdraw_balance(current_balance, withdraw_amount)
print(f"Balance after withdrawing {withdraw_amount}:", current_balance)

withdraw_amount = 200
current_balance = withdraw_balance(current_balance, withdraw_amount)
print(f"Balance after attempting to withdraw {withdraw_amount}:", current_balance)
