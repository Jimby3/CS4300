books = [
    {"title": "bible", "author": "jesus"},
    {"title": "whatever textbook for this class", "author": "Dr. Thomas Hastings"},
    {"title": "How to Code for dummies", "author": "some guy/girl"},
    {"title": "I dont read", "author": "person"},
    {"title": "Insert Book Here", "author": "guy"}
]

student_db = {
    "Jimmy": 12345,
    "Jenna": 67890,
    "Thomas": 11111,
    "Jordan": 69420,
    "Nick": 00000
}


def print_first_three_books(books):
    three_books = books[:3]
    for book in three_books:
        print(book["title"])
    return three_books


def test_student_db():
    assert student_db["Jimmy"] == 12345
    assert student_db["Jenna"] == 67890
    assert student_db["Thomas"] == 11111
    assert student_db["Jordan"] == 69420
    assert student_db["Nick"] == 00000


def test_print_first_three_books():
    returned_books = print_first_three_books(books)

    assert len(returned_books) == 3
    assert returned_books[0]["title"] == "bible"
    assert returned_books[1]["title"] == "whatever textbook for this class"
    assert returned_books[2]["title"] == "How to Code for dummies"
