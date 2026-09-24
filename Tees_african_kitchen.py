# Tee's African Kitchen - Menu Order Calculator

menu = {
    "Jollof Rice": 600,
    "Fried Rice": 700,
    "Fried Chicken": 700,
    "Fried Beef": 600,
    "Plantain": 300,
    "Puff Puff": 500,
    "Zobo": 400
}

print("================================")
print("     TEE'S AFRICAN KITCHEN")
print("================================")
print("\nMENU")

for item, price in menu.items():
    print(f"{item}: KSh {price}")


# Take the customer's order

order = []

while True:
    item = input("\nEnter the item you want to order: ").title()

    if item not in menu:
        print("That item is not on the menu.")
        continue

    try:
        quantity = int(input(f"How many {item} would you like? "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    order.append({
        "item": item,
        "quantity": quantity,
        "price": menu[item]
    })

    print(f"{quantity} x {item} added to your order.")

    more = input(
        "Would you like to order another item? (yes/no): "
    ).lower()

    if more == "no":
        break


# Calculate the total cost

total = 0

for order_item in order:
    item_total = order_item["quantity"] * order_item["price"]
    total += item_total


# Display the receipt

print("\n================================")
print("             RECEIPT")
print("================================")

for order_item in order:
    item_total = order_item["quantity"] * order_item["price"]

    print(
        f'{order_item["item"]} x {order_item["quantity"]} '
        f'- KSh {item_total}'
    )

print("--------------------------------")
print(f"TOTAL: KSh {total}")
print("================================")