from collections import Counter


def most_frequent_common_word(filename1, filename2):
    with open(filename1) as file1, open(filename2) as file2:
        # Compute frequency dictionary of words in file1
        file1_word_freq = {}
        for line in file1:
            words = line.strip().split()
            for word in words:
                file1_word_freq[word] = file1_word_freq.get(word, 0) + 1

        # Compute frequency dictionary of words in file2
        # Using a different way to calculate frequencies just as a demonstration
        file2_words = []
        for line in file2:
            file2_words.extend(line.strip().split())
        counter = Counter(file2_words)
        file2_word_freq = dict(counter)

    # Get words in common in both files
    common_words = file1_word_freq.keys() & file2_word_freq.keys()

    # Get average frequency of common words in both files
    average_freq = {}
    for word in common_words:
        freq_in_file1 = file1_word_freq.get(word, 0)
        freq_in_file2 = file2_word_freq.get(word, 0)
        average_freq[word] = (freq_in_file1 + freq_in_file2) / 2

    # For investigation purposes
    # print(sorted(average_freq.items(), key=lambda x:x[1], reverse=True))

    max_item = max(average_freq.items(), key=lambda x: x[1])
    return max_item
