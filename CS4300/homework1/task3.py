def check_sign(num):
    if num == 0:
        return "zero"
    elif num > 0:
        return "positive"
    else:
        return "negative"


# https://www.cuemath.com/prime-numbers-formula/
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def first_10_prime_for_loop():
    primes = []
    num = 2  # Start with the first prime number
    while len(primes) < 10:
        if is_prime(num):
            primes.append(num)
            print(num)
        num += 1


def sum_while_loop():

    total = 0
    num = 0
    while num < 101:
        total += num
        num += 1

    return total

def test_check_sign():
    assert check_sign(10) == "positive"
    assert check_sign(-5) == "negative"
    assert check_sign(0) == "zero"
def test_sum_while_loop():
    assert sum_while_loop() == 5050

def test_first_10_prime_for_loop(capfd):
    first_10_prime_for_loop()
    captured = capfd.readouterr()
    assert captured.out.strip() == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29"

