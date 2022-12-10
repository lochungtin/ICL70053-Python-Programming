# Minimal Solutions

## Q1

```py
def odd_even_swap(word):
    w, l = word, len(word) - 1
    return "".join(w[i + 1] + w[i] for i in range(0, l, 2)) + ((l + 1) % 2) * word[l]
```

## Q2

```py
from math import sqrt

def closest_pair(coord_list):
    s = set()
    for i, a in enumerate(coord_list):
        for b in map(lambda x: coord_list[x], range(i + 1, len(coord_list))):
            s.add((sqrt(sum(map(lambda x: (x[0] - x[1]) ** 2, zip(a, b)))), a, b))
    return list(map(lambda x: {x[1], x[2]}, [min(s, key=lambda x: x[0])]))[0]
```

## Q3

```py
def top5_bigram_frequency(filename):
    c = {}
    for l in map(lambda x: x.strip().lower().split(" "), open("q3/" + filename)):
        for i in range(len(l) - 1):
            c[" ".join(l[i : i + 2])] = c.get(" ".join(l[i : i + 2]), 0) + 1
    return dict(sorted(c.items(), key=lambda x: x[1], reverse=True)[0:5])
```

## Q4

```py
def get_winner(board):
    l = len(board)
    for i in range(l):
        if len(set(board[i][j] for j in range(l))) == 1 and board[i][0] != " ":
            return board[i][0]
        if len(set(board[j][i] for j in range(l))) == 1 and board[0][i] != " ":
            return board[0][i]
    if len(set(board[i][i] for i in range(l))) == 1 and board[0][0] != " ":
        return board[0][0]
    if len(set(board[i][l - i - 1] for i in range(l))) == 1 and board[0][l - 1] != " ":
        return board[0][l - 1]
    if any(map(lambda x: x == " ", [c for r in board for c in r])):
        return None
    return "draw"
```
