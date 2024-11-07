import sqlite3 # Imports the SQLite DB Library


def get_input(): # Separate function to keep main clean
    # Give the user options to query and gather user input. (Ensure it is an int)
    while True:
        try:
            userInput = int(input("Enter a number from 1-6: \n"))
            break
        except ValueError:
            print("Invalid Entry Try Again.\n")

    return userInput


def main(): # Begin main()
    print("Welcome to the Veterinary Clinic Database")
    print("Please select from one of the following queries: \n")
    print(" 1. Query 1\n", "2. Query 2\n", "3. Query 3\n", "4. Query 2\n", "5. Query 2\n", "6. EXIT\n")

    # Call for user input
    userInput = get_input()

    # The user can query until they're satisfied
    while(userInput != 6):

        # I put this here temporarily for debugging purposes
        print("You selected", userInput)

        # Switch statement to match user input (Actions are temporarily print statements to show concept)
        match userInput:
            case 1:
                print("Execute Query 1\n")
            case 2:
                print("Execute Query 2\n")
            case 3:
                print("Execute Query 3\n")
            case 4:
                print("Execute Query 4\n")
            case 5:
                print("Execute Query 5\n")
            case 6:
                break
            case _:
                print("Invalid Entry Try Again.\n")

        # Get user's next input (Ensure it is an int)
        userInput = get_input()

    # Signify that the program has ended
    print("Goodbye!")


if __name__ == "__main__":
    main()
