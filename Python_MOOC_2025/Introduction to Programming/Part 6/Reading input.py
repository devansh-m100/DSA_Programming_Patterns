# Write your solution here
def read_input(input_str: str, lower_bound, upper_bound):
    while True:
        try:
            user_input = int(input(input_str))
            if lower_bound <= user_input <= upper_bound:
                return user_input
            else:
                print(f"You must type in an integer between {lower_bound} and {upper_bound}")
        except ValueError:
            print(f"You must type in an integer between {lower_bound} and {upper_bound}")
