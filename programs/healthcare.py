# LEVEL 7: ADMIN SETS SERVICES OF THE DAY 
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]


# INPUT VALIDATION FUNCTIONS
def get_valid_name():
    while True:
        name = input("Enter Name: ").strip()
        if name.replace(" ", "").isalpha() and len(name) > 0:
            return name
        print("Invalid name! Use alphabets only.")


def get_valid_age():
    while True:
        try:
            age = int(input("Enter Age: "))
            if age > 0:
                return age
            print("Age must be positive.")
        except ValueError:
            print("Enter numeric value only.")


def get_valid_gender():
    while True:
        gender = input("Enter Gender (Male/Female/Other): ").strip()
        if gender.isalpha():
            return gender
        print("Invalid gender input.")


def get_valid_contact():
    while True:
        contact = input("Enter Contact Number: ")
        if contact.isdigit() and len(contact) == 10:
            return contact
        print("Contact must be a 10-digit number.")


# LEVEL 1: PATIENT DETAILS 
print("\n--- HealWell Care Hospital ---")
print("Patient Registration\n")

name = get_valid_name()
age = get_valid_age()
gender = get_valid_gender()
contact = get_valid_contact()


# LEVEL 2: DISPLAY SERVICES
print("\nAvailable Services:")
for i in range(len(services)):
    print(f"{i + 1}. {services[i]} - ₹{costs[i]}")


# MENU-DRIVEN SERVICE SELECTION
selected_services = []
selected_costs = []

while True:
    try:
        choice = int(input("\nEnter service number to add (0 to finish): "))
        if choice == 0:
            break
        if 1 <= choice <= len(services):
            selected_services.append(services[choice - 1])
            selected_costs.append(costs[choice - 1])
            print("Service added successfully.")
        else:
            print("Invalid service number.")
    except ValueError:
        print("Enter numeric value only.")


# LEVEL 4: TOTAL COST CALCULATION
subtotal = sum(selected_costs)


# LEVEL 8: DISCOUNTS
discount = 0

# Senior Citizen Discount
if age >= 60:
    discount += subtotal * 0.10

# High Bill Discount
if subtotal > 5000:
    discount += (subtotal - discount) * 0.05

amount_after_discount = subtotal - discount


# LEVEL 5: GST CALCULATION 
gst = amount_after_discount * 0.18
grand_total = amount_after_discount + gst


#  LEVEL 6: INVOICE GENERATION 
print("\n-----------------------------------------------")
print("HealWell Care Hospital")
print("Patient Invoice")
print("-----------------------------------------------")

print("\nPatient Information:")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Gender : {gender}")
print(f"Contact: {contact}")

print("\nServices Availed:")
for i in range(len(selected_services)):
    print(f"{i + 1}. {selected_services[i]} : ₹{selected_costs[i]}")

print(f"\nSubtotal           : ₹{subtotal:.2f}")
print(f"Discount Applied   : ₹{discount:.2f}")
print(f"GST (18%)          : ₹{gst:.2f}")
print(f"Grand Total        : ₹{grand_total:.2f}")

print("\nThank you for choosing HealWell Care Hospital!")
