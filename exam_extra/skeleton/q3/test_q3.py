from q3 import count_repeats


def test():
    answer = count_repeats("byebye")
    print(answer)
    assert answer == 2

    answer = count_repeats("cake")
    print(answer)
    assert answer == 1

    answer = count_repeats("aabbcacbabcc")
    print(answer)
    assert answer == 4

    answer = count_repeats("12345678")
    print(answer)
    assert answer == 1

    answer = count_repeats("yaba1yaba1")
    print(answer)
    assert answer == 0

    answer = count_repeats("dingdong")
    print(answer)
    assert answer == 0
    
    
if __name__ == "__main__":
    test()
