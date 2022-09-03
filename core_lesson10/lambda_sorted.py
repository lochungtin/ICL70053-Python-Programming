singers = [
    ("Michael", "Jackson"),
    ("Billy", "Joel"),
    ("Lionel", "Richie"),
    ("Tina", "Turner"),
    ("Luther", "Vandross"),
]

sorted_singers = sorted(
    singers, key=lambda name: (len(name[0]) + len(name[1]), name[0])
)

assert sorted_singers == [
    ("Billy", "Joel"),
    ("Tina", "Turner"),
    ("Lionel", "Richie"),
    ("Luther", "Vandross"),
    ("Michael", "Jackson"),
]
