import os
from datetime import datetime
from pandas import read_csv

def format_usd(my_price):
    """
    Formats a number to USD price format with dollar sign and two decimals
    Example: 5.230 --> $5.23

    Params:
        my_price is numeric, like int or float, and is the number that you want to format
        
    Example:
        format_usd(2.378)
    """

    return f"${my_price:,.2f}"

def lookup_product(product_id, all_products):
    """
    Looks up the product ID entered by the user to ensure that it is in the product list

    Params:
        product_id (str) like "8"
        all_products (list of dict) each dict should have "id", "name", "department", "aisle", and "price" attributes

    Example:
        lookup_product(8, products)
    """
    matching_products = [p for p in all_products if str(p["id"]) == str(product_id)]
    if any(matching_products):
        return matching_products[0]
    else:
        return None


# Prevent all the application code from being imported
# But still be able to run it from the command line

if __name__ == "__main__":


    # READ INVENTORY OF PRODUCTS

    products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
    products_df = read_csv(products_filepath)
    products = products_df.to_dict("records")

    # CAPTURE PRODUCT SELECTIONS

    selected_products = []
    while True:
        selected_id = input("Please select a product identifier: ")
        if selected_id.upper() == "DONE":
            break
        else:
            matching_product = lookup_product(selected_id, products)
            
            if matching_product:
                selected_products.append(matching_product)
            else:
                print("OOPS, Couldn't find that product. Please try again.")

    now = datetime.now()

    subtotal = sum([float(p["price"]) for p in selected_products])
    tax = subtotal * 0.0875


    # PRINT RECEIPT

    print("---------")
    print("CHECKOUT AT: " + now.strftime("%d/%m/%Y %I:%M:%S %p"))
    print("---------")
    for p in selected_products:
        print("SELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))

    print("---------")
    print(f"SUBTOTAL: {format_usd(subtotal)}")
    print(f"TAX: {format_usd(tax)}")
    print(f"TOTAL: {format_usd((tax + subtotal))}")
    print("---------")
    print("THANK YOU! PLEASE COME AGAIN SOON!")
    print("---------")

    # WRITE RECEIPT TO FILE

    receipt_id = now.strftime("%d-%m-%Y %I-%M-%S")
    receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

    with open(receipt_filepath, "w") as receipt_file:
        receipt_file.write("------------------------------------------")
        for p in selected_products:
            receipt_file.write("\nSELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))

        receipt_file.write("\n---------")
        receipt_file.write(f"\nSUBTOTAL: {format_usd(subtotal)}")
        receipt_file.write(f"\nTAX: {format_usd(tax)}")
        receipt_file.write(f"\nTOTAL: {format_usd((tax + subtotal))}")
        receipt_file.write("\n---------")
        receipt_file.write("\nTHANK YOU! PLEASE COME AGAIN SOON!")
        receipt_file.write("\n---------")
