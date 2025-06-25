amount = 50
while amount > 0:
    print(f"Amount Due: {amount}")
    inserted = int(input("Insert Coin: "))
    if inserted not in [5, 10, 25]:
        continue
    amount -= inserted

if amount == 0:
    print("Change Owed: 0")
else:
    print(f"Change Owed: {-1 * amount}")
