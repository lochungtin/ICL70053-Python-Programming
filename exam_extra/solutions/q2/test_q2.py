from q2 import filter_e

def test_simple():
    output = filter_e("I swear by the moon and the stars in the sky")
    print(output)

    expected_output = "I by moon and stars in sky"

    assert output == expected_output 
    

def test_one_word_left():
    output = filter_e("She sells sea shells by the sea shore")
    print(output)

    expected_output = "by"

    assert output == expected_output 


def test_numbers():
    output = filter_e("1 22 333 4444 55555")
    print(output)

    expected_output = "1 22 333 4444 55555"

    assert output == expected_output 


def test_empty_string():
    output = filter_e("")
    print(output)

    expected_output = ""

    assert output == expected_output 


if __name__ == "__main__":
    test_simple()
    test_one_word_left()
    test_numbers()
    test_empty_string()

