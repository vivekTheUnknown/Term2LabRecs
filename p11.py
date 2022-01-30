no_of_times = int(input("enter the no. of products u want: "))
products = {}
for p in range(1, no_of_times+1):
    product_name = input("enter the name of ur product: ")
    product_price = int(input("enter the price of said product: "))
    products[product_name] = product_price
print(products)