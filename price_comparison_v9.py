import pandas

import numpy


def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"


def int_check(question, low, high):
    """Checks users enter an integer / float that is more than zero (or the 'xxx' exit code)"""
    error = f"Oops - please enter a number between {low} and {high} ."
    while True:
        response = input(question).lower()
        if response == "xxx":
            return response
        try:
            response = int(response)
            if low <= response <= high:
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
- Enter your name and budget
- View the different flower options
- Enter the  number of the item you want to purchase
- Confirm and then your budget will update
- Continue shopping till ready to Checkout 

''')


# Variables

keep_going = "yes"

user_purchased_flowers = []
user_purchased_flower_prices = []
user_purchased_flowers_quantity = []
user_purchased_total = []
budget_left = []

# Lists & Dictionaries

flowers = ['Rose', 'Tulip', 'Sunflower', 'Lily', 'Daisy', 'Orchid', 'Lavender', 'Marigold', 'Clover', 'Daffodil']
flower_prices = [15, 8, 6, 12, 4, 18, 5, 7, 16, 9]

flower_dict = {
    'Flower': flowers,
    'Prices': flower_prices
}

user_flower_dict = {
    'Flower': user_purchased_flowers,
    'Prices': user_purchased_flower_prices,
    'Quantity': user_purchased_flowers_quantity,
    'Total Price': user_purchased_total
}

# create dataframe / table from dictionary
planty_plants_frame = pandas.DataFrame(flower_dict)

# Rearranging index
planty_plants_frame.index = numpy.arange(1, len(planty_plants_frame) + 1)

# Program main heading
print(make_statement("Welcome to Planty Plants ", "🌸"))
print()

want_instructions = string_check("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()

# Get username and budget

print()
name = not_blank("Name: ")

print(f"Welcome {name}")

budget = int_check("What's your Budget? - $", 4, 100)
print("Budget Accepted")

print()

budget_left = budget

print("\n🌸🌸🌸 Flower List 🌸🌸🌸")
# for number, info in flower_list['Flower List'].items():
# #print(f"{number}. {info[0]} - ${info[1]:.2f}")

print(planty_plants_frame)

print()

while keep_going == "yes":

    # Start ordering loop
    while True:

        side_choice = int_check("Enter the number of the flower you want or if you finished ordering type 'xxx': ", 1,
                                10)

        if side_choice == "xxx":
            break

        user_selected_flower = flowers[side_choice - 1]
        user_selected_flower_price = flower_prices[side_choice - 1]

        quantity_input = int_check(f"How many {user_selected_flower}'s would you like to purchase? ", 1, 2)

        # Calculate the total amount of purchased flowers
        total_selected_amount = user_selected_flower_price * quantity_input

        if total_selected_amount > budget_left:
            print(f"That costs $ {total_selected_amount}, but you only have $ {budget_left}")
            print("Try entering a smaller amount.")
            continue

        else:
            user_purchased_flowers.append(user_selected_flower)
            user_purchased_flower_prices.append(user_selected_flower_price)
            user_purchased_flowers_quantity.append(quantity_input)
            user_purchased_total.append(user_selected_flower_price * quantity_input)

            budget_left = budget_left - total_selected_amount

            print(
                f"Added {quantity_input} {user_selected_flower}'s to cart - The total cost so far is $"
                f"{sum(user_purchased_total)}")
            print(f"Budget remaining: $ {budget_left}")
            print()

        if budget_left <= 3:
            print(f"Your remaining budget was ${budget_left} which is to small to make"
                  f" any more purchases, so your receipt will be printed")
            keep_going = "no"
            break

    # create dataframe from user dictionary
    user_plants_frame = pandas.DataFrame(user_flower_dict)

    # Rearranging index
    user_plants_frame.index = numpy.arange(1, len(user_plants_frame) + 1)

    if keep_going == "yes":
        print(f"You have ${budget_left} remaining")
        keep_going = string_check("Do you want to order any more flowers? ")
    else:
        break

print()
print(user_plants_frame)
print()
print(f"The total cost is ${sum(user_purchased_total)}")
print("Thank you for purchasing from Planty Plants 🌸")
