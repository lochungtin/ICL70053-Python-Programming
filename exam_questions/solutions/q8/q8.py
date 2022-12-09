import json


class Store:
    def __init__(self):
        # e.g. self.products["1000"] = Product("1000", "apple", 0.75, NoOffer())
        self.products = {}

    def init_from_json(self, json_filename):
        with open(json_filename) as jsonfile:
            products = json.load(jsonfile)

        for product in products:
            id_ = product["id"]
            name = product["name"]
            price = product["price"]
            if "offer" in product:
                if product["offer"]["type"] == "bnf1":
                    n = product["offer"]["n"]
                    offer = BuyNGet1FreeOffer(n)
                elif product["offer"]["type"] == "percent":
                    percent = product["offer"]["n"]
                    offer = PercentageReductionOffer(percent)
                else:
                    offer = NoOffer()
            else:
                offer = NoOffer()

            self.products[product["id"]] = Product(id_, name, price, offer)

    def checkout(self, shopping_cart):
        print("============================")
        total = 0
        for (product_id, quantity) in shopping_cart.items.items():
            product = self.products[product_id]
            cost = product.calculate_price(quantity)
            total += cost
            print(
                f"{product.name}\t£{product.price}\t{quantity}\t£{cost}\t{product.offer}"
            )
        print("============================")
        print(f"TOTAL:\t\t\t£{total}")
        print("============================")


class Product:
    def __init__(self, id_, name, price, offer=None):
        self.id = id_
        self.name = name
        self.price = price
        if offer == None:
            self.offer = NoOffer()
        else:
            self.offer = offer

    def __repr__(self):
        return f"<{self.id}: {self.name} (£{self.price}) {self.offer}>"

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.name == other.name
            and self.price == other.price
            and self.offer == other.offer
        )

    def calculate_price(self, quantity):
        return self.offer.calculate_total(self.price, quantity)


class NoOffer:
    def __init__(self):
        pass

    def __repr__(self):
        return f"(No offer)"

    def __eq__(self, other):
        return isinstance(other, NoOffer)

    def calculate_total(self, cost_per_item, quantity=1):
        return cost_per_item * quantity


class PercentageReductionOffer:
    def __init__(self, percent_discount=0.0):
        self.percent_discount = percent_discount

    def __repr__(self):
        return f"({self.percent_discount*100}% off)"

    def __eq__(self, other):
        return (
            isinstance(other, PercentageReductionOffer)
            and self.percent_discount == other.percent_discount
        )

    def calculate_total(self, cost_per_item, quantity=1):
        return cost_per_item * (1 - self.percent_discount) * quantity


class BuyNGet1FreeOffer:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"(Buy {self.n} Get 1 Free Offer)"

    def __eq__(self, other):
        return isinstance(other, BuyNGet1FreeOffer) and self.n == other.n

    def calculate_total(self, cost_per_item, quantity=1):
        quantity_to_pay = quantity - (quantity // (self.n + 1))
        return cost_per_item * quantity_to_pay
