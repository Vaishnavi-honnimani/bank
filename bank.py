initial_balance=float(input("Enter initial amount"))
deposit=float(input("Enter deposit amount"))

new_balance=initial_balance+deposit

print(f"Initial Balance:",initial_balance)
print(f"Deposit:",deposit)
print(f"New Balance",new_balance)

withdraw=float(input("Enter withdrawal amount"))
new_balance-=withdraw

print(f"withdraw:",withdraw)
print(f"Final balance:",new_balance)