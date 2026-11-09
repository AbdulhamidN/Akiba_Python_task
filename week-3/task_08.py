
def validate_units(units):
    if units < 0:
        return False
    else:
        return True


def calculate_first_tier(units):
    if units > 50:
        units = 50

    charge = units * 0.50

    return charge


def calculate_second_tier(units):
    if units <= 50:
        return 0

    if units > 150:
        units = 150

    second_tier_units = units - 50

    charge = second_tier_units * 0.75

    return charge


def calculate_third_tier(units):
    if units <= 150:
        return 0

    third_tier_units = units - 150

    charge = third_tier_units * 1.20

    return charge


def calculate_total_bill(units, service_fee=0):
    if validate_units(units) == False:
        return -1

    if service_fee < 0:
        return -1

    first_charge = calculate_first_tier(units)
    second_charge = calculate_second_tier(units)
    third_charge = calculate_third_tier(units)

    total = first_charge + second_charge + third_charge

    total = total + service_fee

    return total


def generate_billing_summary(units, service_fee=0):
    if validate_units(units) == False:
        print("Error: Units consumed cannot be negative.")
        return

    if service_fee < 0:
        print("Error: Service fee cannot be negative.")
        return

    first_charge = calculate_first_tier(units)
    second_charge = calculate_second_tier(units)
    third_charge = calculate_third_tier(units)

    total = calculate_total_bill(units, service_fee)

    print("\n========== ELECTRICITY BILL ==========")

    print("Units consumed:", units)

    print("\nFirst 50 units:")
    print("Charge:", first_charge, "Birr")

    print("\nNext 100 units:")
    print("Charge:", second_charge, "Birr")

    print("\nAbove 150 units:")
    print("Charge:", third_charge, "Birr")

    print("\nService fee:", service_fee, "Birr")

    print("--------------------------------------")
    print("Total bill:", total, "Birr")
    print("======================================")


# Main program

units = 180

generate_billing_summary(units)

# Example with an optional service fee
generate_billing_summary(180, 20)
