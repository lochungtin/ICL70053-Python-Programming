from q1 import longest_word

def test_simple():
    words = ["I", "love", "Python", "programming", "the", "most"]
    output = longest_word(words)
    print(output)

    expected_output = ("programming", 11)

    assert output == expected_output 
    

def test_queen():
    words = ["Caught", "in", "a", "landslide", "no", "escape", "from", 
             "reality"]
    output = longest_word(words)
    print(output)

    expected_output = ("landslide", 9)

    assert output == expected_output 


def test_single():
    words = ["Llanfairpwllgwyngyll"]
    output = longest_word(words)
    print(output)

    expected_output = ("Llanfairpwllgwyngyll", 20)

    assert output == expected_output 


def test_same_max_length():
    words = ["laugh", "reach", "go", "climb", "jump"]
    output = longest_word(words)
    print(output)

    expected_output = ("laugh", 5)

    assert output == expected_output 


def test_empty_strings():
    words = ["", "", "", "", ""]
    output = longest_word(words)
    print(output)

    expected_output = ("", 0)

    assert output == expected_output 


if __name__ == "__main__":
    test_simple()
    test_queen()
    test_single()
    test_same_max_length()
    test_empty_strings()

