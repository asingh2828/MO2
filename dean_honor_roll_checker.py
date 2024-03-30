# Amanpreet Singh
# dean_honor_roll_checker.py
# This Python app accepts student names and GPAs and tests if the student qualifies for either the Dean's List or the Honor Roll.

def main():
    print("Welcome to the Dean's List and Honor Roll Checker!")
    print("Enter 'ZZZ' as the last name to quit.")

    while True:
        last_name = input("Enter student's last name: ")
        if last_name == 'ZZZ':
            print("Exiting the program...")
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} did not qualify for Dean's List or Honor Roll.")

if __name__ == "__main__":
    main()
