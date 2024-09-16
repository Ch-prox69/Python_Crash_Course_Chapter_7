numb_people = input("How many people are in your dinner group?")
numb_people = int(numb_people)

if numb_people <= 8:
    print("\nTable ready")
else:
    print(f"\nSorry, you'll have to wait for a table, we currently don't have any to accommodate, {numb_people} of guests")