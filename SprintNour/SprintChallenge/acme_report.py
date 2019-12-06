from acme import Product

def generate_products(time=30):
    li = []
    for i in range(time +1):
        li.append(Product(str(i)))
    return li
