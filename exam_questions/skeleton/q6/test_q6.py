from q6 import most_frequent_common_word

def test_short_poetry():
    (word, freq) = most_frequent_common_word("princeton.txt", 
                                             "peace_in_a_palace.txt")
    print(word, freq)
    assert word == "the"
    assert freq == 33.5


def test_long_poetry():
    (word, freq) = most_frequent_common_word("copernicus.txt", 
                                             "michael_oaktree.txt")
    print(word, freq)
    assert word == "the"
    assert freq == 121.5


if __name__ == "__main__":
    test_short_poetry()
    test_long_poetry()

