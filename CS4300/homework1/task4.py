def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)
    return round(final_price, 2)


# i should probably have made these seperate cases.. but i'm lazy
def test_calculate_discount():
    # ints
    assert calculate_discount(100, 30) == 70
    assert calculate_discount(200, 50) == 100
    assert calculate_discount(69, 0) == 69
    assert calculate_discount(55, 50) == 27.5

    # floats
    assert calculate_discount(150.5, 50) == 75.25
    assert calculate_discount(250.99, 15.25) == 212.71  # Corrected expected value
    assert calculate_discount(99.99, 5.5) == 94.49

    # ints and floats mixed
    assert calculate_discount(100, 20.5) == 79.5
    assert calculate_discount(150.50, 25) == 112.88
