
def add_product(products, name, price, stock):
    if name == "":
        print("Error: Product name cannot be empty.")
        return

    # Check for duplicate product names
    for product in products:
        if product["name"].lower() == name.lower():
            print("Error: Product already exists.")
            return

    if price < 0:
        print("Error: Price cannot be negative.")
        return

    if stock < 0:
        print("Error: Stock cannot be negative.")
        return

    new_product = {
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(new_product)
    print("Product added successfully.")


def search_product(products, name):
    for product in products:
        if product["name"].lower() == name.lower():
            print("Product found:")
            print("Name:", product["name"])
            print("Price:", product["price"], "Birr")
            print("Stock:", product["stock"])
            return product

    print("Product not found.")
    return None


def update_price(products, name, new_price):
    if new_price < 0:
        print("Error: Price cannot be negative.")
        return

    for product in products:
        if product["name"].lower() == name.lower():
            product["price"] = new_price
            print("Price updated successfully.")
            return

    print("Product not found.")


def increase_stock(products, name, quantity):
    if quantity <= 0:
        print("Error: Quantity must be greater than zero.")
        return

    for product in products:
        if product["name"].lower() == name.lower():
            product["stock"] = product["stock"] + quantity
            print("Stock increased successfully.")
            return

    print("Product not found.")


def sell_product(products, name, quantity):
    if quantity <= 0:
        print("Error: Sale quantity must be greater than zero.")
        return

    for product in products:
        if product["name"].lower() == name.lower():

            if quantity > product["stock"]:
                print("Error: Not enough stock available.")
                return

            product["stock"] = product["stock"] - quantity

            print("Sale successful.")
            print("Remaining stock:", product["stock"])
            return

    print("Product not found.")


def calculate_inventory_value(products):
    total_value = 0

    for product in products:
        total_value = total_value + (
            product["price"] * product["stock"]
        )

    return total_value


def low_stock_report(products):
    print("\n========== LOW STOCK REPORT ==========")

    found = False

    for product in products:
        if product["stock"] < 5:
            print("Product:", product["name"])
            print("Remaining stock:", product["stock"])
            print("--------------------------------------")
            found = True

    if found == False:
        print("No low-stock products.")

    print("======================================")


# Main program

products = [
    {"name": "Notebook", "price": 80, "stock": 10},
    {"name": "Pen", "price": 15, "stock": 3},
    {"name": "Bag", "price": 500, "stock": 7}
]

# Add a new product
add_product(products, "Pencil", 10, 20)

# Search for a product
search_product(products, "Notebook")

# Update product price
update_price(products, "Notebook", 90)

# Increase stock
increase_stock(products, "Pen", 5)

# Sell a product
sell_product(products, "Bag", 2)

# Calculate total inventory value
total = calculate_inventory_value(products)

print("\nTotal inventory value:", total, "Birr")

# Display low-stock report
low_stock_report(products)
