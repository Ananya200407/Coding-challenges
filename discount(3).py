def calculate_discount(total_amount, discount_percent):
    discount = (total_amount * discount_percent) / 100
    final_amount = total_amount - discount
    return discount, final_amount


try:
    total = float(input("Enter total amount: "))
    discount_percent = float(input("Enter discount percentage: "))

    # Validation
    if total < 0 or discount_percent < 0:
        print("Total amount and discount percentage must be non-negative.")
    elif discount_percent > 100:
        print("Discount percentage cannot exceed 100%.")
    else:
        discount, payable = calculate_discount(total, discount_percent)
        print("Discount Amount =", discount)
        print("Final Amount to Pay =", payable)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
