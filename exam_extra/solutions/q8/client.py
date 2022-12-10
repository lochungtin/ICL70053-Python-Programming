class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product_id, count=1):
        self.items[product_id] = self.items.get(product_id, 0) + count

    def remove_product(self, product_id, count=1):
        if product_id in self.items:
            self.items[product_id] = self.items[product_id] - count
            if self.items[product_id] <= 0:
                del self.items[product_id]
