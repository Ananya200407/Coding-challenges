try:
    name = input("Enter student name: ").strip()
    
    if not all(char.isalpha() or char.isspace() for char in name) or len(name) == 0:
        print("Invalid name! Name should contain alphabets only.")
    else:
        marks1 = float(input("Enter marks for Subject 1: "))
        marks2 = float(input("Enter marks for Subject 2: "))
        marks3 = float(input("Enter marks for Subject 3: "))

        if not(0 <= marks1 <= 100 and 0 <= marks2 <= 100 and 0 <= marks3 <= 100):
            print("Invalid marks! Marks should be between 0 and 100.")
        else:
            total = marks1 + marks2 + marks3
            average = total / 3

            if average >= 60:
                student_class = "1st Class"
            elif average >= 50:
                student_class = "2nd Class"
            elif average >= 35:
                student_class = "Pass Class"
            else:
                student_class = "Fail"

            
            print("\nStudent Report Card")
            print("Name:", name)
            print("Total Marks:", total)
            print("Average Marks:", round(average, 2))
            print("Class Secured:", student_class)

except ValueError:
    print("Invalid input! Please enter numeric values for marks.")
