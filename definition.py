import valuer as df # Importing custom module to store sales data

def name():
    """Starts the process by asking for the product name."""
    products1 = input("What product do you want to sell?: ")
    quantity(products1)

def quantity(products1):
    """Asks for quantity and ensures the input is a whole number (integer)."""
    try:
        quantity1 = int(input("How many would you like to purchase?: "))
        price(quantity1, products1)
    except ValueError:
        # Handles cases where the user enters text instead of a number
        print("Error, just enter integer numbers.")
        quantity(products1) # Restart this step on error

def price(quantity1, products1):
    """Asks for price, calculates total, and saves data to the 'df' module."""
    try:
        price1 = float(input("Enter the price of the product: "))
        total = price1 * quantity1

        # Appending data to the lists inside the imported 'df' module
        df.price.append(total)
        df.update.append(
            f"Product: {products1} | Quantity: {quantity1} | Total cost: {total}"
        )

        continuee()

    except ValueError:
        # Handles cases where the user enters non-numeric values for price
        print("Error, just enter numbers.")
        price(quantity1, products1)

def continuee():
    """Checks if the user wants to add more items or finish the sale."""
    want = input("Would you like to purchase another product? (yes/no): ")

    if want.lower() == "yes":
        name() # Loops back to the start
    elif want.lower() == "no":
        print("\nSale completed.")

        # Iterates through the stored records in df.update and prints them
        print("\nSales record:")
        for sale in df.update:
            print(sale)
    else:
        # Validates that the user only types 'yes' or 'no'
        print("Invalid option.")
        continuee()

# Main entry point to start the program
name()
