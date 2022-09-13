# Introduction to Pandas

## Ch2 Series

- **1D** data stream
  - Form of `np.array`, `iterable`, `dict`, or `scalar`
  - Contains an **index** for each element
    - A.k.a axis labels
    - Indices follow the `keys` of the `dict` if given a `dict` when initialising
  - Contains a **name**

## Ch3-6 DataFrame

- **2D** data table
  - Consists of a **collection** of series
  - Columns are tied together by an index
  - Creation using a **list of tuples** / **dictionary of lists**
  - From csv
    - `df = pd.read_cv(dtype=str, index_col=n)`
- Index columns by `df.iloc[]`  with index
- Index columns by `df.iloc[]`  with "name"
  - **Slicing** can be applied
- **Iteration**
  - By KV pair `.iteritems()`
  - By index row pair `.iterrows()`
  - By tuples `.itertuples()`
- **Filtering**
  - `.drop_duplicates(inplace=True)`
    - `inplace=True` option **mutates** the table
  - Apply condition to `[]`
- **Missing data**
  - `.isna().sum()` or `.isnull().sum()` to see missing data summary
  - `.dropna(inplace=True)` removes all rows with null
  - `.dropna(axis=1)` remove all columns with null
- **Mutating**
  - `.apply()` can apply lambda functions to all elements / columns
