import os


def clear_screen():
    return os.system("clear || cls")


def menu():
    clear_screen()
    print("\nWelcome to FizzBuzz. All numbers are between 1 and 100.")

    user_options = {
        'fizz': [number for number in range(1,101) if number % 3 == 0],
        'buzz': [number for number in range(1,101) if number % 5 == 0],
        'fizzbuzz': [number for number in range(1,101) if number % 3 == 0 and number % 5 == 0]
    }

    while True:
        user_input = input(
            "\nWhat would you like to do?"
            "\n- Enter 'fizz' to see numbers divisible by 3"
            "\n- Enter 'buzz' to see numbers divisible by 5"
            "\n- Enter 'fizzbuzz' to see numbers divisible by 3 AND 5"
            "\n- Enter 'clear' to clear the terminal screen"
            "\n- Enter 'quit' to exit the program: "
        ).lower()
    
        if user_input == 'fizz':
            clear_screen()
            print(f"Printing numbers from 1 to 100 that are divisible by 3:\n{user_options['fizz']}")
        elif user_input == 'buzz':
            clear_screen()
            print(f"Printing numbers from 1 to 100 that are divisible by 5:\n{user_options['buzz']}")
        elif user_input == 'fizzbuzz':
            clear_screen()
            print(f"Printing numbers from 1 to 100 that are divisible by 3 AND 5:\n{user_options['fizzbuzz']}")
        elif user_input == 'clear':
            clear_screen()
        elif user_input == 'quit':
            clear_screen()
            print("\nThanks for using FizzBuzz. Have a good day.\n")
            break
        else:
            clear_screen()
            print("\nUnknown input. Try again.")


menu()