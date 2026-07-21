def check_borrowing(overdue_books, status):
    if overdue_books == "yes":
        return "Not allowed: overdue books"
    elif status == "suspended":
        return "Not allowed: suspended account"
    else:
        return "Borrowing allowed"


allowed_students = 0

while True:
    print("\n=== Library Borrowing Kiosk ===")

    name = input("Enter student name (or type 'exit' to quit): ").strip()

    if name.lower() == "exit":
        break

    overdue_books = input("Do you have overdue books? (yes/no): ").strip().lower()
    status = input("Enter borrower status (active/suspended): ").strip().lower()

    result = check_borrowing(overdue_books, status)

    if result == "Borrowing allowed":
        books = int(input("How many books do you want to borrow? "))

        if books <= 0:
            print( "You must borrow at least 1 book.")
        elif books > 3:
            print("Sorry, You can only borrow up to 3 books.")
            print("Borrowing allowed for 3 books only.")
            allowed_students += 1
        else:
            print(f"Borrowing allowed for {books} book(s).")
            allowed_students += 1
    else:
        print(result)

print("\nLibrary kiosk session ended.")
print("Total students allowed to borrow books:", allowed_students)