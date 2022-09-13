import pandas as pd

pokemon_df = pd.read_csv("nsp_lesson2/pokemon.csv", index_col="Name")

filtered_df = pokemon_df[
    (pokemon_df["Type 2"] == "Electric") | (pokemon_df["Type 2"] == "Ice")
]

print(filtered_df)
