appointments = []

teachers = [
    ["T001", "Ms. Maria Santos", "Maria Santos", "maria123"],
    ["T002", "Mr. John Reyes", "jreyes", "john123"],
    ["T003", "Ms. Angela Cruz", "acruz", "angela123"]
]


# =========================
# MAIN MENU
# =========================

def main_menu():
    print()
    print("===== APPOINTMENT SCHEDULER =====")
    print("[1] teacher")
    print("[2] student")
    print("[3] exit")


# =========================
# TEACHER LOGIN
# =========================

def teacher_login():
    print()
    print("===== TEACHER LOGIN =====")

    username = input("Username: ")
    password = input("Password: ")

    for teacher in teachers:

        if teacher[2] == username and teacher[3] == password:

            print()
            print("Login successful!")
            print("Welcome,", teacher[1])

            teacher_menu(teacher)
            return

    print("Invalid username or password.")


# =========================
# TEACHER MENU
# =========================

def teacher_menu(teacher):

    while True:

        print()
        print(teacher[1], "- teacher")
        print("[1] View appointments")
        print("[2] Approve appointment")
        print("[3] Cancel appointment")
        print("[4] exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_teacher_appointments(teacher)

        elif choice == "2":
            approve_appointment(teacher)

        elif choice == "3":
            cancel_appointment(teacher)

        elif choice == "4":
            print("Logging out...")
            break

        else:
            print("Invalid choice.")


# =========================
# STUDENT MENU
# =========================

def student_menu():

    while True:

        print()
        print("student - menu")
        print("[1] add appointment")
        print("[2] view status of appointment")
        print("[3] edit appointment")
        print("[4] exit")

        choice = input("Choose an option: ")

        if choice == "1":
            book_appointment()

        elif choice == "2":
            view_student_appointments()

        elif choice == "3":
            edit_appointment()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


# =========================
# BOOK APPOINTMENT
# =========================

def book_appointment():

    print()
    print("--- ADD APPOINTMENT ---")

    name = input("Enter your name: ")
    student_id = input("Enter your student ID: ")

    if name == "" or student_id == "":
        print("Please complete your information.")
        return

    print()
    print("Available Teachers:")

    for teacher in teachers:
        print(teacher[0], "-", teacher[1])

    teacher_id = input("Enter teacher ID: ")

    selected_teacher = None

    for teacher in teachers:

        if teacher[0] == teacher_id:
            selected_teacher = teacher
            break

    if selected_teacher is None:
        print("Teacher ID not found.")
        return

    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time: ")
    purpose = input("Enter purpose: ")

    if date == "" or time == "" or purpose == "":
        print("Please complete all appointment details.")
        return

    # Check if the selected teacher already has an appointment
    for appointment in appointments:

        if (appointment[3] == teacher_id and
            appointment[4] == date and
            appointment[5] == time and
            appointment[7] != "Cancelled"):

            print()
            print("This teacher already has an appointment at this time.")
            print("Please choose another date or time.")
            return

    appointment_id = len(appointments) + 1

    new_appointment = [
        appointment_id,
        name,
        student_id,
        teacher_id,
        date,
        time,
        purpose,
        "Pending"
    ]

    appointments.append(new_appointment)

    print()
    print("Appointment added successfully!")
    print("Appointment ID:", appointment_id)
    print("Teacher:", selected_teacher[1])
    print("Status: Pending")


# =========================
# STUDENT VIEW APPOINTMENT
# =========================

def view_student_appointments():

    print()
    print("--- VIEW STATUS OF APPOINTMENT ---")

    student_id = input("Enter your student ID: ")

    found = False

    for appointment in appointments:

        if appointment[2] == student_id:

            found = True

            teacher_name = ""

            for teacher in teachers:

                if teacher[0] == appointment[3]:
                    teacher_name = teacher[1]
                    break

            print()
            print("----------------------------")
            print("Appointment ID:", appointment[0])
            print("Name:", appointment[1])
            print("Teacher:", teacher_name)
            print("Date:", appointment[4])
            print("Time:", appointment[5])
            print("Purpose:", appointment[6])
            print("Status:", appointment[7])

    if found == False:
        print("No appointments found.")


# =========================
# EDIT APPOINTMENT
# =========================

def edit_appointment():

    print()
    print("--- EDIT APPOINTMENT ---")

    student_id = input("Enter your student ID: ")

    found = False

    for appointment in appointments:

        if (appointment[2] == student_id and
            appointment[7] == "Pending"):

            found = True

            print()
            print("Appointment ID:", appointment[0])
            print("Current date:", appointment[4])
            print("Current time:", appointment[5])
            print("Current purpose:", appointment[6])

            new_date = input("Enter new date: ")
            new_time = input("Enter new time: ")
            new_purpose = input("Enter new purpose: ")

            if (new_date == "" or
                new_time == "" or
                new_purpose == ""):

                print("Please complete all details.")
                return

            appointment[4] = new_date
            appointment[5] = new_time
            appointment[6] = new_purpose

            print("Appointment updated successfully.")
            return

    if found == False:
        print("No pending appointment found.")


# =========================
# TEACHER VIEW APPOINTMENTS
# =========================

def view_teacher_appointments(teacher):

    print()
    print("--- MY APPOINTMENTS ---")

    found = False

    for appointment in appointments:

        # IMPORTANT:
        # The teacher can ONLY see appointments
        # assigned to their own teacher ID.

        if appointment[3] == teacher[0]:

            found = True

            print()
            print("----------------------------")
            print("Appointment ID:", appointment[0])
            print("Student:", appointment[1])
            print("Student ID:", appointment[2])
            print("Date:", appointment[4])
            print("Time:", appointment[5])
            print("Purpose:", appointment[6])
            print("Status:", appointment[7])

    if found == False:
        print("You have no appointments.")


# =========================
# APPROVE APPOINTMENT
# =========================

def approve_appointment(teacher):

    print()
    print("--- APPROVE APPOINTMENT ---")

    try:
        appointment_id = int(input("Enter appointment ID: "))

    except ValueError:
        print("Please enter a valid number.")
        return

    for appointment in appointments:

        # IMPORTANT:
        # Teacher can only approve their OWN appointments.

        if (appointment[0] == appointment_id and
            appointment[3] == teacher[0]):

            if appointment[7] == "Pending":

                appointment[7] = "Approved"

                print()
                print("Appointment approved successfully.")

            elif appointment[7] == "Approved":

                print("Appointment is already approved.")

            elif appointment[7] == "Cancelled":

                print("Appointment is already cancelled.")

            return

    print("Appointment not found in your appointments.")


# =========================
# CANCEL APPOINTMENT
# =========================

def cancel_appointment(teacher):

    print()
    print("--- CANCEL APPOINTMENT ---")

    try:
        appointment_id = int(input("Enter appointment ID: "))

    except ValueError:
        print("Please enter a valid number.")
        return

    for appointment in appointments:

        # IMPORTANT:
        # Teacher can only cancel their OWN appointments.

        if (appointment[0] == appointment_id and
            appointment[3] == teacher[0]):

            if appointment[7] == "Cancelled":

                print("Appointment is already cancelled.")

            else:

                appointment[7] = "Cancelled"

                print()
                print("Appointment cancelled successfully.")

            return

    print("Appointment not found in your appointments.")


# =========================
# MAIN PROGRAM
# =========================

def main():

    while True:

        main_menu()

        choice = input("Choose an option: ")

        if choice == "1":

            teacher_login()

        elif choice == "2":

            student_menu()

        elif choice == "3":

            print()
            print("Thank you for using the system!")
            break

        else:

            print("Invalid choice.")


main()