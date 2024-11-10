import sqlite3 # Imports the SQLite DB Library

def clean(con):
    con.close()
    print("Goodbye!")
    exit(0)

def queryOptions():
    print("Select one of the following query options by entering its corresponding number 1-5. You may enter 0 at any time to exit the program.")
    print("\t1 Find the first, middle, and last names of owners who own more than {positive integer} pet(s).")
    print("\t2 Find the average age of all {cats, dogs, birds, hares} served by the veterinary clinic.")
    print("\t3 Find the first, middle, and last names of owners who own a {cat, dog, bird, hare} but not a {cat, dog, bird, hare}.")
    print("\t4 Find the first, middle, and last names of salaried employees with a monthly salary of at least ${positive integer}.")
    print("\t5 Find the average cost of {treatments, prescriptions} at the vet clinic.")

def get_menu_input(): # Separate function to keep main clean
    # Give the user options to query and gather user input. (Ensure it is an int)
    while True:
        try:
            userInput = int(input("\nEnter a number from 0-5 (0 to Exit): \n"))
            break
        except ValueError:
            print("Invalid Entry Try Again.\n")

    return userInput

def get_pos_input(num): # Separate function to keep main clean
    # Gather a positive integer from user input. (Ensure it is a positive int)
    while True:
        try:
            userInput = int(input("Enter a positive integer within the appropriate range: \n"))
            if num == 0:
                if userInput >= 0:
                    if userInput == 0:
                        clean(con)
                    else:
                        return userInput
                else:
                    print("Integer must be positive.")
            else:
                if userInput >= 0 and userInput <= num:
                    if userInput == 0:
                        clean(con)
                    else:
                        return userInput
                else:
                    print("Integer must be positive and within the appropriate range.")
        except ValueError:
            print("Invalid Entry Try Again.\n")

def select_animal():
    print("\t\t1 Cats")
    print("\t\t2 Dogs")
    print("\t\t3 Birds")
    print("\t\t4 Hares")
    animal = get_pos_input(4)
    if animal == 1:
        return "Cat"
    elif animal == 2:
        return "Dog"
    elif animal == 3:
        return "Bird"
    else:
        return "Hare"


def select_treatment_prescription():
    print("\t\t1 Treatments")
    print("\t\t2 Prescriptions")
    return get_pos_input(2)


def query1(cur):
    print("\t1 Find the first, middle, and last names of owners who own more than {positive integer} pet(s).")
    numPets = get_pos_input(0)

    test = cur.execute("select owner_fname, owner_mname, owner_lname, pet_count from (select owner.owner_id, owner.owner_fname, owner.owner_mname, owner.owner_lname, count(pet.pet_id) as pet_count from owner, pet where owner.owner_id = pet.owner_id group by owner.owner_fname, owner.owner_mname, owner.owner_lname) where pet_count > ?",
            (numPets,))

    for row in cur.execute(
            "select owner_fname, owner_mname, owner_lname, pet_count from (select owner.owner_id, owner.owner_fname, owner.owner_mname, owner.owner_lname, count(pet.pet_id) as pet_count from owner, pet where owner.owner_id = pet.owner_id group by owner.owner_fname, owner.owner_mname, owner.owner_lname) where pet_count > ?",
            (numPets,)):

        print(row)

def query2(cur):
    print("\t2 Find the average age of all {cats, dogs, birds, hares} served by the veterinary clinic.")
    pet1 = select_animal()
    for row in cur.execute("select avg(pet.pet_age) from pet where pet.pet_species = ?", (pet1,)):
        print(row)


def query3(cur):
    print(
        "\t3 Find the first, middle, and last names of owners who own a {cat, dog, bird, hare} but not a {cat, dog, bird, hare}.")
    pet1 = select_animal()
    pet2 = select_animal()
    for row in cur.execute(
            "select owner.owner_fname, owner.owner_mname, owner.owner_lname from owner natural join pet where pet.pet_species = ? except select owner.owner_fname, owner.owner_mname, owner.owner_lname from owner natural join pet where pet.pet_species = ?; ",
            (pet1, pet2,)):
        print(row)


def query4(cur):
    print(
        "\t4 Find the first, middle, and last names of salaried employees with a monthly salary of at least ${positive integer}.")
    monthlySalary = get_pos_input(0)
    for row in cur.execute(
            "select employee.employee_fname, employee.employee_mname, employee.employee_lname from employee natural join veterinarian where veterinarian.vet_salary / 12 >= ? union select employee.employee_fname, employee.employee_mname, employee.employee_lname from employee natural join other_salaried where other_salaried.salaried_salary / 12 >= ?",
            (monthlySalary, monthlySalary,)):
        print(row)


def query5(cur):
    print("\t5 Find the average cost of {treatments, prescriptions} at the vet clinic.")
    service = select_treatment_prescription()
    if service == 1:
        for row in cur.execute("select avg(treatment.treatment_cost) from Treatment"):
            print(row)
    else:
        for row in cur.execute("select avg(prescription.prescription_cost) from Prescription"):
            print(row)


def main(): # Begin main()
    print("Welcome to the Veterinary Clinic Database\n")

    # Declare global con to let user exit at any time
    global con

    # Connect to DB
    con = sqlite3.connect("Swanson_Futakami.db")
    cur = con.cursor()

    # Print query options for the user
    queryOptions()

    # Call for user input
    userInput = get_menu_input()

    # The user can query until they're satisfied
    while(userInput != 0):

        # Switch statement to match user input (Actions are temporarily print statements to show concept)
        match userInput:
            case 1:
                print("Execute Query 1\n")
                query1(cur)

            case 2:
                print("Execute Query 2\n")
                query2(cur)

            case 3:
                print("Execute Query 3\n")
                query3(cur)

            case 4:
                print("Execute Query 4\n")
                query4(cur)
            case 5:
                print("Execute Query 5\n")
                query5(cur)

            case 0:
                break
            case _:
                print("Invalid Entry Try Again.\n")

        # Get user's next input (Ensure it is an int)
        userInput = get_menu_input()

    # close the connection & signify that the program has ended
    clean(con)


if __name__ == "__main__":
    main()
