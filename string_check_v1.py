def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the first letter"""
    while True:
        response = input(question).lower()
        for item in valid_ans_list:
            if response == item or response == item[num_letters]:
                return item
        print(f"Please choose an option from {valid_ans_list}")


want_instructions = string_check("Do you want to see the instructions? ")
