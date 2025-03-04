import pyjokes


# This library returns a joke as a string if you call get_joke() function

def get_joke():
    return pyjokes.get_joke()


def is_joke_funny(joke):
    return False


def test_get_joke():
    assert len(pyjokes.get_joke()) > 0
    assert is_joke_funny(pyjokes.get_joke()) == False