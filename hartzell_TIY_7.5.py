prompt = "PLEASE INSERT AGE:"
prompt += "\nEnter 'quit' when done."

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("You get free tickets")
    elif age < 13:
        print("Ticket cost is $10.")
    else:
        print("Ticket cost is $15.")