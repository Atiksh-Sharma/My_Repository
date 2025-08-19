# Project Name - Restaurant Menu 

menu = {
    "Pizza": 150,
    "Burger": 80,
    "Pasta": 120,
    "French Fries": 70,
    "Cold Drink": 40
}

print("🍴 Welcome to My Restaurant 🍴")
print("\nHere is our Menu:\n")

for item, price in menu.items():
    print(f"{item:15} - ₹{price}")

order_total = 0

while True:
    food_item = input("\nEnter the item you want to order (or type 'done' to finish): ").title()
    
    if food_item == "Done":
        break
    elif food_item in menu:
        order_total += menu[food_item]
        print(f"{food_item} added to your order. ✅")
    else:
        print("Sorry, we don't have that item.")

print("\nYour total bill is: ₹", order_total)
print(" Thanks for visiting My Restaurant! ")
