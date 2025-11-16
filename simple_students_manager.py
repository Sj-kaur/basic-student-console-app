students = []

while True:
    print("\n--- Student Record System (Simple) ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter marks: ")

        student = {
            "name": name,
            "marks": marks
        }

        students.append(student)
        print("Student added!")

    elif choice == "2":
        print("\n--- Student List ---")
        if len(students) == 0:
            print("No records available.")
        else:
            for s in students:
                print(f"Name: {s['name']} | Marks: {s['marks']}")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
