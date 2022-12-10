# Minimal Solutions

## Q1

```py
def odd_even_swap(word):
    w, l = word, len(word) - 1
    return "".join(w[i + 1] + w[i] for i in range(0, l, 2)) + (not l % 2) * word[l]
```

## Q2

```py
def closest_pair(coord_list):
    d = [((a, b), zip(a, b)) for a in coord_list for b in coord_list if a != b]
    return set(min(((sum(map(lambda x: (x[0] - x[1]) ** 2, q)), p)) for p, q in d)[1])
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
    s = [set(board[i][i] for i in range(l)), set(board[i][l - i - 1] for i in range(l))]
    s += [set(board[j][i] for j in range(l)) for i in range(l)]
    s += [set(r) for r in board]
    for w in [list(r)[0] for r in s if len(r) == 1 and " " not in r]:
        return w
    if any(map(lambda x: x == " ", [c for r in board for c in r])):
        return None
    return "draw"
```
