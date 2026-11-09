
def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        subtotal = subtotal + item["price"] * item["quantity"]

    return subtotal


def calculate_discount(subtotal):
    if subtotal >= 3000:
        discount = subtotal * 0.10
    elif subtotal >= 1000:
        discount = subtotal * 0.05
    else:
        discount = 0

    return discount


def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate / 100
    return tax


def generate_receipt(items, tax_rate):
    # Check tax rate
    if tax_rate < 0 or tax_rate > 100:
        print("Error: Invalid tax rate.")
        return

    # Check prices and quantities
    for item in items:
        if item["price"] < 0:
            print("Error: Price cannot be negative.")
            return

        if item["quantity"] < 0:
            print("Error: Quantity cannot be negative.")
            return

    # Calculate receipt
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)

    amount_after_discount = subtotal - discount
    tax = calculate_tax(amount_after_discount, tax_rate)

    final_amount = amount_after_discount + tax

    # Display receipt
    print("\n========== SHOPPING RECEIPT ==========")

    for item in items:
        item_total = item["price"] * item["quantity"]

        print(item["name"])
        print("Price:", item["price"], "Birr")
        print("Quantity:", item["quantity"])
        print("Total:", item_total, "Birr")
        print("--------------------------------------")

    print("Subtotal:", subtotal, "Birr")
    print("Discount:", discount, "Birr")
    print("Tax:", tax, "Birr")
    print("Final Amount:", final_amount, "Birr")

    print("======================================")


# Main program
items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

tax_rate = 15

generate_receipt(items, tax_rate)
