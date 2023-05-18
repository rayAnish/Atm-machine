# Clear the file before starting the program
with open("registrations.txt", "w") as file:
    file.write("")

while True:
    print("Exam Registration Form")
    print("1. Register Student")
    print("2. View All Registrations")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        exam = input("Enter exam name: ")

        with open("registrations.txt", "a") as file:
            file.write(f"{name},{roll_number},{exam}\n")
            print("Registration successful!")

    elif choice == "2":
        print("Registered Students:")
        with open("registrations.txt", "r") as file:
            registrations = file.readlines()
            for registration in registrations:
                name, roll_number, exam = registration.strip().split(",")
                print(f"Name: {name}, Roll Number: {roll_number}, Exam: {exam}")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
