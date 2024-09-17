prompt = "PLEASE INSERT AGE:"
prompt += "\nEnter 'quit' when done."

# Control the loop
active = True

# Loop exicution
while active:
    age = input(prompt)
    
    # allowing the 'quit' function to work
    if age == 'quit':
        break
    
    # Using int
    age = int(age)
    
    # printing based on age 
    if age < 3:
        print("You get free tickets")
    elif age < 13:
        print("Ticket cost is $10.")
    else:
        print("Ticket cost is $15.")
    
    

