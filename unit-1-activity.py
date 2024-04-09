# Function to calculate the square of a number
# Aaron Xiao
# March 12 2024


def calculate_square(number):
    return number ** 2

# Main program
def main():
    # Input from the user
    user_input = float(input("Enter a number: "))

    # Conditional statement using if, elif, and else
    if user_input > 0:
        result = calculate_square(user_input)
        print(f"The square of {user_input} is: {result}")
    elif user_input == 0:
        print("You entered zero.")
    else:
        print("You entered a negative number.")

if __name__ == "__main__":
    main()


