
print("================================")
print("   CAMPUS CANTEEN BILLING SYSTEM")
print("================================")

print("Menu:")
print("1. Burger      - PKR 300")
print("2. Pizza       - PKR 500")
print("3. Sandwich    - PKR 200")
print("4. Juice       - PKR 100")
print("0. Checkout")

subtotal = 0
total_quantity = 0

while True:
    choice = int(input("\nEnter item number (0 to checkout): "))

    if choice == 0:
        break
    elif choice < 0 or choice > 4:
        print("Invalid choice! Try again.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity! Try again.")
        continue

    if choice == 1:
        item = "Burger"
        price = 300
    elif choice == 2:
        item = "Pizza"
        price = 500
    elif choice == 3:
        item = "Sandwich"
        price = 200
    else:
        item = "Juice"
        price = 100

    cost = price * quantity
    subtotal = subtotal + cost
    total_quantity = total_quantity + quantity

    print(item, "x", quantity, "= PKR", cost)

if subtotal >= 1000:
    discount = subtotal * 10 / 100
else:
    discount = 0

final_bill = subtotal - discount

print("\n========== FINAL BILL ==========")
print("Subtotal: PKR", subtotal)
print("Discount: PKR", discount)
print("Total quantity:", total_quantity)
print("Final bill: PKR", final_bill)
print("Thank you for visiting!")
