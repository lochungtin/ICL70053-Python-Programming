from q5 import minmax_swap

def test_5_digits():
    output = minmax_swap(31572)
    print(output)
    expected_output = (13572, 71532)
    assert output == expected_output 

    
def test_repeated_digits():
    output = minmax_swap(91213)
    print(output)
    expected_output = (11293, 93211)
    assert output == expected_output 


def test_no_max_swap():
    output = minmax_swap(9876)
    print(output)
    expected_output = (6879, 9876)
    assert output == expected_output 


def test_two_digits():
    output = minmax_swap(27)
    print(output)
    expected_output = (27, 72)
    assert output == expected_output 
    

def test_no_leading_zeros():
    output = minmax_swap(400)
    print(output)
    expected_output = (400, 400)
    assert output == expected_output 


def test_single_digit():
    output = minmax_swap(5)
    print(output)
    expected_output = (5, 5)
    assert output == expected_output 


if __name__ == "__main__":
    test_5_digits()
    test_repeated_digits()
    test_no_max_swap()
    test_two_digits()
    test_no_leading_zeros()
    test_single_digit()

