from q1 import odd_even_swap


def test_odd():
    word = "abcdefghi"
    swapped = odd_even_swap(word)
    expected = "badcfehgi"
    print(swapped)
    assert swapped == expected


def test_even():
    word = "Python Programming"
    swapped = odd_even_swap(word)
    expected = "yPhtnoP orrgmaimgn"
    print(swapped)
    assert swapped == expected


if __name__ == "__main__":
    test_odd()
    test_even()

