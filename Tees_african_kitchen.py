# Tee's African Kitchen - Menu Ordering System

menu = {
    "Jollof Rice": 600,
    "Fried Rice": 700,
    "Fried Chicken": 700,
    "Fried Beef": 600,
    "Plantain": 300,
    "Puff Puff": 500,
    "Zobo": 400
}

# Store all customer orders
orders = []


# Display the restaurant menu
def view_menu():
    print("\n================================")
    print("       TEE'S AFRICAN KITCHEN")
    print("================================")
    print("\nMENU")

    for item, price in menu.items():
        print(f"{item}: KSh {price}")


# Create a new customer order
def place_order():
    view_menu()

    # Allow the customer to add multiple items
    while True:
        item = input("\nEnter the item you want to order: ").title()

        # Check if the item exists on the menu
        if item not in menu:
            print("That item is not on the menu.")
            continue

        try:
            # Handle invalid quantity input
            quantity = int(input(f"How many {item} would you like? "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        # Create an order record
        order = {
            "item": item,
            "quantity": quantity,
            "price": menu[item]
        }

        # Add the order to the orders list
        orders.append(order)

        print(f"{quantity} x {item} added to your order.")

        # Ask if the customer wants another item
        more = input(
            "Would you like to order another item? (yes/no): "
        ).lower()

        if more == "no":
            break


# Read and display all customer orders
def view_orders():
    print("\n================================")
    print("           YOUR ORDERS")
    print("================================")

    if not orders:
        print("No orders have been placed yet.")
        return

    total = 0

    for number, order in enumerate(orders, start=1):
        item_total = order["quantity"] * order["price"]
        total += item_total

        print(
            f"{number}. {order['item']} x {order['quantity']} "
            f"- KSh {item_total}"
        )

    print("--------------------------------")
    print(f"TOTAL: KSh {total}")
    print("================================")


# Update the quantity of an existing order
def update_order():
    if not orders:
        print("\nThere are no orders to update.")
        return

    view_orders()

    try:
        order_number = int(
            input("\nEnter the order number you want to update: ")
        )

        if order_number < 1 or order_number > len(orders):
            print("Invalid order number.")
            return

        new_quantity = int(input("Enter the new quantity: "))

        if new_quantity <= 0:
            print("Quantity must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    orders[order_number - 1]["quantity"] = new_quantity

    print("Order updated successfully.")


# Delete an existing customer order
def delete_order():
    if not orders:
        print("\nThere are no orders to delete.")
        return

    view_orders()

    try:
        order_number = int(
            input("\nEnter the order number you want to delete: ")
        )

        if order_number < 1 or order_number > len(orders):
            print("Invalid order number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    deleted_order = orders.pop(order_number - 1)

    print(
        f"{deleted_order['item']} order deleted successfully."
    )


# Main menu controls the program
while True:
    print("\n================================")
    print("       TEE'S AFRICAN KITCHEN")
    print("================================")
    print("1. View Menu")
    print("2. Place Order")
    print("3. View Orders")
    print("4. Update Order")
    print("5. Delete Order")
    print("6. Exit")
    print("================================")

    choice = input("Choose an option: ")

    if choice == "1":
        view_menu()

    elif choice == "2":
        place_order()

    elif choice == "3":
        view_orders()

    elif choice == "4":
        update_order()

    elif choice == "5":
        delete_order()

    elif choice == "6":
        print("Thank you for visiting Tee's African Kitchen!")
        break

    else:
        print("Invalid option. Please choose 1-6.")