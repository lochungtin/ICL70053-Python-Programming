def load_unique_lyrics(filename):
    rt = set()
    for line in open(filename):
        for word in line.strip().split(" "):
            rt.add(word)

    return rt


def get_overlapping_words(file1, file2):
    l1 = load_unique_lyrics(file1)
    l2 = load_unique_lyrics(file2)

    return l1.intersection(l2)


overlap = get_overlapping_words(
    "lesson8/lyrics_mini_project/let_it_go.txt",
    "lesson8/lyrics_mini_project/into_the_unknown.txt",
)
print(overlap)
print(len(overlap))
