# Calculate the sum of two numbers entered by the user.

def sum_of_two_numbers(user_input):
    """
    Calculates the sum of two numbers provided as a string separated by a comma.

    Parameters:
    - user_input (str): A string containing two numbers separated by a comma.

    Returns:
    None

    Prints the sum of the two numbers if they are valid floats. If the input is not a valid string of numbers separated by a comma, it prints an error message. If any other exception occurs, it prints the error message.

    Example:
    sum_of_two_numbers("1.5,2.7")
    Output: The sum of 1.5,2.7 is: 4.2
    """
    try:
        processed_input = list(map(float, user_input.split(","))) # map() is not subscriptable, so to index the elements directly with [] we use list()
        sum_of_two_numbers = (processed_input[0] + processed_input[1])
        print(f"The sum of {user_input} is: {sum_of_two_numbers}")
    except ValueError:
        print("Please enter only numbers, dont ruin my program")
    except Exception as e:
        print(f"Something went wrong: {e}")
        
if __name__ == "__main__":
    user_input = input("Please enter two numbers separated by comma: ")

    while user_input.lower() != exit:
        sum_of_two_numbers(user_input)
        user_input = input("Please enter two numbers separated by comma: ")
   
