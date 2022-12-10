def longest_word(words):
    longest_word = words[0]
    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    return (longest_word, len(longest_word))


# Alternative solution
def longest_word_v2(words):
    items = [(word, len(word)) for word in words]
    max_tuple = max(items, key=lambda x: x[1])
    return max_tuple


# Alternative solution
def longest_word_v3(words):
    items = [(word, len(word)) for word in words]
    items.sort(key=lambda x: x[1], reverse=True)
    return items[0]
