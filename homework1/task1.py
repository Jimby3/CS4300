def hello_world():
    print("Hello, World!")


# in all honesty wasn't sure how to capture console output from python
# used this for help: https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html
def test_hello_world(capsys):
    hello_world()
    out, err = capsys.readouterr()
    assert out.strip() == "Hello, World!"
