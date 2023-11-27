# Convert temperature from Celsius to Fahrenheit.
# Bonus: Convert temperature from Fahrenheit to Celsius if user provides celcius instead.

def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius

if __name__ == '__main__':
    try:
        user_input = input('Please enter a temperature in form of [23C] or [23F]: ')
        while user_input.lower() != 'exit':
            if 'C' in user_input:
                celcius = float(user_input[:-1])
                fahrenheit = celcius_to_fahrenheit(celcius)
                print(f"{celcius}C is equivalent to {fahrenheit}F")
            elif 'F' in user_input:
               fahrenheit = float(user_input[:-1])
               celcius = fahrenheit_to_celcius(fahrenheit)
               print(f"{fahrenheit}F is equivalent to {celcius}C")
            else:
               print('Please enter a temperature in form of [23C] or [23F]')
            user_input = input('Please enter a temperature (or type "exit" to end): ')
    except ValueError:
        print("Please enter only numbers, dont ruin my program")
    except Exception as e:
        print(f"Something went wrong: {e}")
        