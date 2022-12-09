# Minimal Solutions

## Q1

```py
def longest_word(words):
    return max(map(lambda x: (x, len(x)), words), key=lambda x: x[1])
```

## Q2

```py
def filter_e(string):
    return " ".join(filter(lambda x: "e" not in x, string.split(" ")))
```

## Q3

```py
def count_repeats(word):
    c = {}
    [c.update({l: c.get(l, 0) + 1}) for l in word]
    return list(c.values())[0] * (len(set(c.values())) == 1)
```

## Q4

```py
def convert(seconds):
    return seconds // 3600, (seconds % 3600) // 60, seconds % 60
```

## Q5

```py
def minmax_swap(number):
    c = set()
    for i, h in enumerate(str(number)):
        for j, k in enumerate(str(number)):
            m, m[i], m[j] = list(str(number)), k, h
            if m[0] != "0":
                c.add(int("".join(m)))
    return min(c), max(c)
```

## Q6

```py
def most_frequent_common_word(filename1, filename2):
    c = {}
    for f in (filename1, filename2):
        for l in open("q6/" + f, "r").readlines():
            [c.update({w: c.get(w, 0) + 0.5}) for w in l.strip().split(" ")]
    return sorted(c.items(), key=lambda x: x[1], reverse=True)[0]
```

## Q7

```py
class CashAccount(BankAccount):
    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)
        self.w = -4

    def withdraw(self, amount):
        super().withdraw(amount)
        self.w += 1

    def deduct_monthly_fees(self):
        super().withdraw(max(self.w, 0))
        self.w = -4
```

## Q8

```py
def init_from_json(self, json_filename):
    for i in load(open("q8/" + json_filename, "r")):
        self.products[i["id"]] = Product(i["id"], i["name"], i["price"])
        if "offer" in i and i["offer"]["type"] == "percent":
            self.products[i["id"]].offer = PercentageReductionOffer(i["offer"]["n"])
        elif "offer" in i:
            self.products[i["id"]].offer = BuyNGet1FreeOffer(i["offer"]["n"])

def calculate_total(self, cost_per_item, quantity=1): # precent
    return quantity * cost_per_item * (1 - self.percent_discount)

def calculate_total(self, cost_per_item, quantity=1): # bn1f
    return cost_per_item * (quantity - (quantity // (self.n + 1)))
```

## Q9

```py
def simplify_fraction(numerator, denominator):
    n = set([n for n in range(1, numerator + 1) if numerator % n == 0])
    d = set([n for n in range(1, denominator + 1) if denominator % n == 0])
    c = sorted(n & d, reverse=True)[0]
    return numerator // c, denominator // c
```

## Q10

```py
def c(l):
    nums = [n for n in l if n in "123456789"]
    return (len(nums) == len(set(nums))) and all(c in "123456789." for c in l)

def is_sudoku_board_valid(board):
    return all(
        c([board[i][j] for j in range(9)])
        and c([board[j][i] for j in range(9)])
        and c([board[(i // 3) * 3 + j // 3][(i % 3) * 3 + j % 3] for j in range(9)])
        for i in range(9)
    )
```
