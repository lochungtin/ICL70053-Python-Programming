singers = [
    ("Michael", "Jackson"),
    ("Billy", "Joel"),
    ("Lionel", "Richie"),
    ("Tina", "Turner"),
    ("Luther", "Vandross"),
]

vowel_most_singer = max(
    singers, key=lambda name: sum([ch in "aeiouAEIOU" for ch in name[0] + name[1]])
)

assert vowel_most_singer == ("Lionel", "Richie")
