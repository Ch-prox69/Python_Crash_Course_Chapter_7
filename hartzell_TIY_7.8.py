# Sandwich Orders list
sandwich_orders = ['philly cheese steak', 'meatball marinara', 'ruben']
finished_sandwiches = []

# Printing and using a loop to confirm sandwich is being made
for sandwich in sandwich_orders:
    print(f"I have made your {sandwich.title()} sandwich")

# Moving sandwich orders to finished sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nMoving your order for the {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)

# Printing that all sandwiches are used
for fnshd_sandwh in finished_sandwiches:
    print(f"\nYour {fnshd_sandwh.title()} sandwich order is complete")

# Asking for delivery
prompt = "Would you like delivery? (yes/ no)"
prompt += "Please type 'quit' if you don't want delivery"

while True:
    delivery = input("Enter 'yes' to add delivery to order, 'no' for no delivery, or 'quit' to exit: ").strip().lower()

    if delivery == 'quit':
        break
    elif delivery == 'yes':
        print("Adding delivery to order")
    elif delivery == 'no':
        print("Ok, no delivery")
    else:
        print("Invalid input. Please enter 'yes', 'no', or 'quit'.")


