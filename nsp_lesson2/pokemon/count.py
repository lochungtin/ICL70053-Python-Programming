import pandas as pd

pokemon_df = pd.read_csv("nsp_lesson2/pokemon/data.csv")

print(pokemon_df["Legendary"].value_counts())
