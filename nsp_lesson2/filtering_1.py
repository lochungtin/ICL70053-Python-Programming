import pandas as pd

pokemon_df = pd.read_csv("nsp_lesson2/pokemon.csv", index_col="Name")

filtered_df = pokemon_df[
    (pokemon_df["Type 1"] == "Water") & (pokemon_df["Type 2"] == "Dragon")
]

print(filtered_df)
