def integer():
    # the meaning of life obviously
    return 42


def float_num():
    return 69.420


def string():
    return "wazzup"


def boolean():
    return False


def test_integer():
    assert integer() == 42


def test_float_num():
    assert float_num() == 69.420


def test_string():
    assert string() == "wazzup"


def test_boolean():
    assert boolean() == False
