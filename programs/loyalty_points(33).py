try:
    grand_total = 0.0

    n = int(input("Enter number of items: "))

    if n <= 0:
        print("Number of items must be greater than 0.")
        exit()

    # ITEM ENTRY
    for i in range(1, n + 1):
        print(f"\nEnter details for Item {i}")

        item_code = input("Item code: ").strip().upper()
        quantity = int(input("Quantity: "))
        price = float(input("Price per item: "))

        if quantity < 0 or price < 0:
            print("Invalid quantity or price. Item skipped.")
            continue

        item_total = quantity * price

        # Promotional discount
        if item_code == "PROMO10":
            discount = item_total * 0.10
            item_total -= discount
            print("Promotional Discount Applied: -Rs.", round(discount, 2))

        grand_total += item_total

    print("\nSubtotal after discounts: Rs.", round(grand_total, 2))

    # TAX CALCULATION
    if grand_total < 5000:
        tax_rate = 0.05
    elif grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    tax_amount = grand_total * tax_rate
    final_total = grand_total + tax_amount

    # PAYMENT METHOD
    payment_method = input("Select payment method (cash/card): ").strip().lower()
    surcharge = 0.0

    if payment_method == "card":
        surcharge = final_total * 0.02
        final_total += surcharge

    if final_total < 500:
        print("\nMinimum purchase amount of ₹500 not met.")
        print("Invoice cannot be generated.")
        exit()

    # LOYALTY POINTS
    loyalty_points = int(final_total // 100)

    # INVOICE 
    print("\n=========== INVOICE ===========")
    print("Subtotal: Rs.", round(grand_total, 2))
    print(f"Tax ({int(tax_rate*100)}%): Rs.", round(tax_amount, 2))
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Final Payable Amount: Rs.", round(final_total, 2))
    print("Loyalty Points Earned:", loyalty_points)
    print("================================")

except ValueError:
    print("Invalid input! Please enter numeric values correctly.")
