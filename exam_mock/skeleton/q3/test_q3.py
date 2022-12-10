from q3 import top5_bigram_frequency


def test_small():
    freq_dict = top5_bigram_frequency("baby.txt")
    print(freq_dict)
    expected = {'baby baby': 36, 
                'like baby': 14, 
                'yeah yeah': 12, 
                'baby oh': 9, 
                "i 'm": 9
               }
    assert freq_dict == expected


def test_large():
    freq_dict = top5_bigram_frequency("frankenstein.txt")
    print(freq_dict)
    expected = {'of the': 527, 
                'of my': 272, 
                'in the': 263, 
                'i was': 228, 
                'i had': 218
               }
    assert freq_dict == expected


if __name__ == "__main__":
    test_small()
    test_large()

