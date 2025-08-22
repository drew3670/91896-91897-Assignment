import pandas
import random


def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"


def int_check(question):
    """Checks users enter an integer / float that is more than zero (or the 'xxx' exit code)"""
    error = "Oops - please enter an integer."
    while True:
        response = input(question).lower()
        if response == "xxx":
            return response
        try:
            response = int(response)
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the first letter"""
    while True:
        response = input(question).lower()
        for item in valid_ans_list:
            if response == item or response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_ans_list}")


def not_blank(question):
    """Checks that a user response is not blank"""
    while True:
        response = input(question)
        if response != "":
            return response
        print("Sorry, this can't be blank. Please try again.")


def instructions():
    make_statement("Instructions", "ℹ️")
    print('''

For each flower order enter ...
- Name of Customer 
- Flowers of choice 
- Amount Wanted

Once you have bought all the flowers you want, enter
exit code ('xxx'), and the program will display the flower
sales information.


''')


# Program main heading
print(make_statement("Welcome to Planty Plants ", "🌸"))
print()
want_instructions = string_check("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()

# Get username and budget
while True:
    print()
    name = not_blank("Name: ")
    if name.lower() == "xxx":
        break
    budget = int_check("What's your Budget? - $")
    if budget < 4:
        print(f"${budget} isn't enough")
        print("Try entering a budget more than $4")
        continue
    elif budget < 100:
        print(f"Budget accepted: ${budget}")
        break
    else:
        print(f"${budget} is too much")
        print("Sorry there is a limit of $100 per customer")
        continue

print()

flower_list = {
    'Flower List': {
        1: ["Rose ", 15.00],
        2: ["Tulip ", 8.00],
        3: ["Sunflower ", 6.00],
        4: ["Lily ", 12.00],
        5: ["Daisy ", 4.00],
        6: ["Orchid ", 18.00],
        7: ["Lavender ", 5.00],
        8: ["Marigold ", 7.00],
        9: ["Peony ", 16.00],
        10: ["Daffodil ", 9.00]
    }
}

flower_order = {
    'Flower Order': {}
}

budget_left = budget

# ✅ LOOP until user says they are ready
while True:
    ready = input("Are you ready to order?: ").lower()
    if ready in ["yes", "y", "ye"]:
        break
    else:
        print("Ok! Please type 'yes' when you're ready to order.")

print("\n🌸🌸🌸 Flower List 🌸🌸🌸")
for number, info in flower_list['Flower List'].items():
    print(f"{number}. {info[0]} - ${info[1]:.2f}")

print()

# Start ordering loop
while True:
    side_choice = input("Enter the number of the flower you want or if you finished ordering type 'xxx': ")

    if side_choice == "xxx":
        break

    try:
        side_choice = int(side_choice)
    except:
        print("Please enter a valid number.")
        continue

    if side_choice not in flower_list['Flower List']:
        print("That flower is not on the list.")
        continue

    flower = flower_list['Flower List'][side_choice]
    name = flower[0]
    price = flower[1]

    quantity_input = input("How many " + name + "s would you like to purchase? ")

    try:
        quantity = int(quantity_input)
    except:
        print("Please enter a number.")
        continue

    if quantity < 1:
        print("Quantity must be at least 1.")
        continue

    total = price * quantity

    if total > budget_left:
        print("That costs $" + str(total) + ", but you only have $" + str(budget_left))
        print("Try entering a smaller amount.")
        continue

    print()
    budget_left -= total
    print("Added", quantity, name.strip() + "s to cart - Budget remaining: $" + str(budget_left))
    print()
