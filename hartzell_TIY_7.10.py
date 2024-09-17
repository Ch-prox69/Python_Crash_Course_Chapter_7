# Dictionary to store our vacation responses
vacation_responses = {}
onePlace_responses = {}

# Allowing Polling
polling_active = True

# Prompt for the name and response of the user
while polling_active:
    name = input("\nWhat's your name, o dear one?")
    response = input(f"What is your dream location {name}?")
    where = input(f"If you could visit one place {name}, where would it be?")

    # Storing the names
    vacation_responses[name] = response
    onePlace_responses[where] = where

    # Asking if another user wants to use poll
    repeat = input("Would you like to let someone else take the poll? (yes/ no)")
    if repeat == 'no':
        polling_active = False

        # Showing the results
        print("\n ---:) Poll Results:)--- ")
        for name in vacation_responses.items():
            print(f"{name} would like to visit {response}")
        for where in onePlace_responses.items():
            print(f"If {name} could visit one place they'd never been to before, it'd be {where}")


