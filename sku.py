from pyscript import display, document


def generate_sku(e):
    # Clears the div content
    document.getElementById("sku_receipt").innerHTML = ""

    # Gets the category
    category = document.getElementById("category").value

    # Gets the product name
    product_name = document.getElementById("product_name").value

    # Gets the stock quantity
    stock_qty = document.getElementById("stock_qty").value

    # Creates the SKU itself
    SKU = category[:4].upper() + "-" + product_name[:5].upper() + "-" + stock_qty

    # Displays the SKU
    display("SKU: " + SKU, target="sku_receipt")