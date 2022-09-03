singers = [
    ("Michael", "Jackson"),
    ("Billy", "Joel"),
    ("Lionel", "Richie"),
    ("Tina", "Turner"),
    ("Luther", "Vandross"),
]

singers.sort(key=lambda name: name[1][-1])

assert singers == [
    ("Lionel", "Richie"),
    ("Billy", "Joel"),
    ("Michael", "Jackson"),
    ("Tina", "Turner"),
    ("Luther", "Vandross"),
]
