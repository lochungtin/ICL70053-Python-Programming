import pandas as pd

pokemon_df = pd.read_csv("nsp_lesson2/pokemon.csv", index_col="Name")

cols = pokemon_df.columns
print(len(cols))
print(cols.tolist())

dtypes = pokemon_df.dtypes
print(dtypes.to_numpy())

rows = pokemon_df.shape
print(rows)

print(pokemon_df.head(20))
print(pokemon_df.tail(10))
