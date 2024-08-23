#order_processing module
def take_orders(number_of_products):
    if number_of_products>0:
        print(f"deliver {number_of_products} products to the customer ")
    else:
        print(f" cancel order for {abs(number_of_products)} products")    
    return  'thankyou for trusting our brand'       