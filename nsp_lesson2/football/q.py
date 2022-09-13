import pandas as pd

# q1
df = pd.read_csv("nsp_lesson2/football/data.csv", index_col="Team")

# q2
print(df.shape[0])

# q3
print(df)

# q4
print(df[["Red Cards", "Yellow Cards"]])

# q5
print(df[df["Goals"] > 5])

# q6
print(df[df["Goals"] > 5].sort_values("Goals"))

# q7
print(df[df["Shots on target"] > df["Shots off target"]])

# q8
print(df[df["Red Cards"] + df["Yellow Cards"] > 7])
