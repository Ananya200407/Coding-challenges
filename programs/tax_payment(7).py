try:
    name = input("Enter your name: ").strip()

    if not all(char.isalpha() or char.isspace() for char in name) or len(name) == 0:
        print("Invalid name! Name should contain alphabets only.")
    else:
        salary = float(input("Enter your salary (in Rs): "))

        if salary < 0:
            print("Salary cannot be negative.")
        else:
            if salary > 300000:
                print(f"{name} must pay tax.")
            else:
                print(f"{name} does not need to pay tax.")

except ValueError:
    print("Invalid input! Please enter numeric value for salary.")
