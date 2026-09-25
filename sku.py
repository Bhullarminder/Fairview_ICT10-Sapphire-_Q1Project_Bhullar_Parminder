from pyscript import display, document


def generate_sku(e):
    # Clears the div content
    document.getElementById("sku_receipt").innerHTML = ""

    # Gets the category 
    category = document.getElementById("category").cheked

    # Gets the product name
    product_name = document.getElementById("product_name").checked

    # Gets the stock quantity
    stock_qty = document.getElementById("stock_qty").value

    # Creates the SKU itself
    SKU = category[:3].upper() + "-" + product_name[:4].upper() + "-" + stock_qty

    # Displays the SKU
    display("SKU: " + SKU, target="sku_receipt")