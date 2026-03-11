import valuer as df

def name():
    try:
        products1 = input("What product do you to sell?: ")
        quantity(products1)
    except ValueError:
        print("Error")

def quantity(products1):
    attemps = input("Enter “s” if you wish to continue: ")
    while attemps.lower() == "s":    
        try:
            quantity1 = int(input("How many would you like purchase?: "))
            attemps = "r"
            price(quantity1, products1)
        except ValueError:
            print("Error, just enter integer numbers.")

def price(quantity1, products1):
    attemps = input("Enter “s” if you wish to continue: ")
    while attemps.lower() == "s":
        try:
            price1 = float(input("enter the price of the product: "))
            price2 = price1 * quantity1
            df.price.append(price2)
            df.update.append(f"name the product: {products1} | quantity: {quantity1} ")
            attemps = "r"
            continuee()
        except ValueError:
            print("Error, just enter numbers.")

def continuee():
    attemps = input("Enter “s” if you wish to continue: ")
    while attemps.lower() == "s":
        want = input("Would you like to purchase another product?(yes or no): ")
        if want.lower() == "yes":
            attemps = "r"
            name()
        elif want.lower() == "no":
            print("sale completed.")
            attemps = "r"
        else:
            print("Invalid option.")
            