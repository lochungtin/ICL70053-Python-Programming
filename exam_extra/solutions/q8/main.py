from q8 import Store

from client import ShoppingCart

def example_scenario():
    store = Store()
    store.init_from_json("products.json")
    print("Products loaded:")
    for product in store.products.values():
        print(product)
    print()
    
    cart = ShoppingCart()
    cart.add_product("1000", 4)
    cart.add_product("2000", 4)
    cart.add_product("5000", 2)
    cart.add_product("3800", 1)
    cart.add_product("3800", 1)
    cart.add_product("1000", 1)
    print(cart.items)
    
    store.checkout(cart)
    
   
if __name__ == "__main__":   
    example_scenario()