prompt = "\nEnter your toppings for the pizza:"
prompt += "\nType 'quit' to stop the program"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("\nYou added\n" + topping + "\nto your special pizza.")
    else:
        break