import pytest


# I couldnt find too much on how to solve this without already having the hardcoded values for the length of the text
# this is chatgpt's solution though: (https://chatgpt.com/share/67b55887-98d4-8013-b507-6ca09357e9d9)


# Function to count the words in a file
import pytest

# Function to count the words in a file
def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)


# Dynamically generate test functions based on the filenames
def generate_test_function(file_name):
    def test_word_count():
        word_count = count_words_in_file(file_name)
        # Check that word count is greater than 0 (it should be non-zero for a real text file)
        assert word_count > 0, f"Word count for {file_name} is 0, but it shouldn't be"

    # Set the test function name based on the file name
    test_word_count.__name__ = f"test_word_count_{file_name.replace('.txt', '')}"
    return test_word_count


# Dynamically create the test case for task6_read_me.txt
test_task6_read_me = generate_test_function('task6_read_me.txt')


# Add the generated test to pytest collection
@pytest.mark.parametrize("test_func", [test_task6_read_me])
def test_all(test_func):
    test_func()

