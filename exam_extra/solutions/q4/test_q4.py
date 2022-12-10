from q4 import convert

def test_second():
    output = convert(38)
    print(output)
    expected_output = (0, 0, 38)
    assert output == expected_output 

    
def test_minute():
    output = convert(176)
    print(output)
    expected_output = (0, 2, 56)
    assert output == expected_output 


def test_hour():
    output = convert(3823)
    print(output)
    expected_output = (1, 3, 43)
    assert output == expected_output 


def test_zero():
    output = convert(0)
    print(output)
    expected_output = (0, 0, 0)
    assert output == expected_output 


if __name__ == "__main__":
    test_second()
    test_minute()
    test_hour()
    test_zero()

