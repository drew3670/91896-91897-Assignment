

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
print()
name = not_blank("Name: ")

print(f"Welcome {name}")

budget = int_check("What's your Budget? - $", 4, 100)
print("Budget Accepted")

print()

