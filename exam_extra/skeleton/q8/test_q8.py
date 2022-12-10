from q8 import Store, Product, NoOffer, PercentageReductionOffer, BuyNGet1FreeOffer

def test_init_from_json():
    json_filename = "products.json"
    store = Store()
    store.init_from_json(json_filename)

    expected_values = {
        "1000": Product("1000", "apple", 0.75, BuyNGet1FreeOffer(3)),
        "2000": Product("2000", "banana", 1.00, PercentageReductionOffer(0.25)),
        "1200": Product("1200", "pear", 0.85, NoOffer()),
        "3000": Product("3000", "mango", 1.50, BuyNGet1FreeOffer(4)),
        "4000": Product("4000", "orange", 0.50, NoOffer()),
        "3300": Product("3300", "pineapple", 1.25, BuyNGet1FreeOffer(2)),
        "5000": Product("5000", "plum", 0.60, NoOffer()),
        "5400": Product("5400", "nectarine", 0.70, PercentageReductionOffer(0.10)),
        "6000": Product("6000", "kiwi", 1.00, NoOffer()),
        "3800": Product("3800", "papaya", 2.00, BuyNGet1FreeOffer(1))
    }

    assert store.products == expected_values


def test_percent_offer():
    eps = 0.000001

    offer = PercentageReductionOffer(0.5)
    total = offer.calculate_total(1.2, 15)
    print(total)
    assert is_close(total, 9)

    offer = PercentageReductionOffer(0.25)
    total = offer.calculate_total(1.2, 15)
    print(total)
    assert is_close(total, 13.5)

    offer = PercentageReductionOffer(0.10)
    total = offer.calculate_total(1.2, 15)
    print(total)
    assert is_close(total, 16.2)

    offer = PercentageReductionOffer(0.75)
    total = offer.calculate_total(1.2, 15)
    print(total)
    assert is_close(total, 4.5)
    
    offer = PercentageReductionOffer(0.90)
    total = offer.calculate_total(1.2, 15)
    print(total)
    assert is_close(total, 1.8)

    offer = PercentageReductionOffer(0.)
    total = offer.calculate_total(1.2, 15)
    print(total)
    assert is_close(total, 18)
    
    offer = PercentageReductionOffer(1.)
    total = offer.calculate_total(1.2, 15)
    print(total)
    assert is_close(total, 0)


def test_buy_n_get_1_free_offer():
    n = 1
    offer = BuyNGet1FreeOffer(n)
    total = offer.calculate_total(1.0, 1)
    print(total)
    assert is_close(total, 1.0)

    n = 1
    offer = BuyNGet1FreeOffer(n)
    total = offer.calculate_total(1.0, 2)
    print(total)
    assert is_close(total, 1.0)

    n = 1
    offer = BuyNGet1FreeOffer(n)
    total = offer.calculate_total(1.0, 3)
    print(total)
    assert is_close(total, 2.0)
    
    n = 2
    offer = BuyNGet1FreeOffer(n)
    total = offer.calculate_total(0.5, 4)
    print(total)
    assert is_close(total, 1.5)

    n = 2
    offer = BuyNGet1FreeOffer(n)
    total = offer.calculate_total(0.5, 15)
    print(total)
    assert is_close(total, 5)

    n = 3
    offer = BuyNGet1FreeOffer(n)
    total = offer.calculate_total(2.0, 3)
    print(total)
    assert is_close(total, 6.0)

    n = 3
    offer = BuyNGet1FreeOffer(n)
    total = offer.calculate_total(2.0, 4)
    print(total)
    assert is_close(total, 6.0)


def is_close(x, y):
    eps = 0.0000001
    return abs(y - x) < eps    


if __name__ == "__main__":
    test_init_from_json()
    test_percent_offer()
    test_buy_n_get_1_free_offer() 
