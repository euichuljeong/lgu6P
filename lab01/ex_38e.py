products = [
    {
        "category": "Electronics",
        "items": [
            {"name": "Laptop", "price": 1200, "stock": 5},
            {"name": "Smartphone", "price": 800, "stock": 10}
        ]
    },
    {
        "category": "Home Appliances",
        "items": [
            {"name": "Vacuum Cleaner", "price": 150, "stock": 7},
            {"name": "Air Conditioner", "price": 500, "stock": 3}
        ]
    }
]

# result = {
#     "Laptop": {"price": 1200, "stock": 5},
#     "Smartphone": {"price": 800, "stock": 10},
#     "Vacuum Cleaner": {"price": 150, "stock": 7},
#     "Air Conditioner": {"price": 500, "stock": 3}
# }

# products : [0]    [1]
# laptop = products[0][1]V[0]V
# laptop_ps = products[0][1]V([1],[2])

def convert_data(products):
    result = {}
    for product in products:
        for item in product['items']:
            #>여기까지 이렇게 잘라짐 item: {"name": "Laptop", "price": 1200, "stock": 5}
            # name = item.pop('name')
            # # del item['name']
            # result[ name ] = item

             result[ item['name'] ] = {'price': item['price'], 'stock': item['stock']}
    return result


print(convert_data(products))