from q9 import simplify_fraction

def test_simple_fraction():
    output = simplify_fraction(4, 8)
    print(output)
    expected_output = (1, 2)
    assert output == expected_output 

    
def test_larger_numerator():
    output = simplify_fraction(15, 5)
    print(output)
    expected_output = (3, 1)
    assert output == expected_output 
    
    
def test_large_factor():
    output = simplify_fraction(200, 300)
    print(output)
    expected_output = (2, 3)
    assert output == expected_output 


def test_no_simplification():
    output = simplify_fraction(7, 9)
    print(output)
    expected_output = (7, 9)
    assert output == expected_output 
    
    
if __name__ == "__main__":
    test_simple_fraction()
    test_larger_numerator()
    test_large_factor()
    test_no_simplification()
