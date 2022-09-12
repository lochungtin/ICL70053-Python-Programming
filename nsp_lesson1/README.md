# Introduction to NumPy and Matplotlib

## Ch2-6 NumPy Arrays

- **More efficient**
  - Use for large scale arrays / matrices
- Convert between `lists`
- `tolist()` and `np.array()`
- `.shape` check the dimensions
- `.dtype` check the data type of the elements
- `np.zeros()` creates an array filled with `0`s of the set shape
- `np.arange(n)` creates an array from `0` to `n-1`
- `np.linspace(s, e, num=g)` creates an array with elements, from `s` to `e` linearly separated with gap size `g`
- `+`, `-`, `+=`, and `-=` work elementwise
- **Boolean indexing**
  - `arr > n` Maps the array to booleans, compares them elementwise
  - `arr[arr > n]` keeps all elements that satisfy the condition
- **Array stacking**
  - `np.vstack()` - stack on vertical stack
  - `np.hstack()` - stack on horizontal stack
  - `np.dstack()` - stack on depth stack
- **Array concatenation**
  - Appends on the same axis, unlike stacking
- **Array splitting**
  - Can specify splitting at what positions
  - `np.vsplit()` - splits on vertical axis
  - `np.hsplit()` - splits on horizontal axis
  - `np.dsplit()` - splits on depth axis
- **Repeating arrays**
  - `np.repeat()` repeats items elementwise
    - Flattens array if no axis is specified
- **Nonzero searching**
  - `np.nonzero()` returns the indices in arrays
- **Unique filtering**
  - `np.unique()` returns the unique elements
    - Makes a set
- **Sorting**
  - `arr.sort()` is a mutator
  - `np.argsort` returns the sorted **indices**

## Ch7 MISC NumPy

- **Saving and loading**
  - Will save as `.npz`
  - Can also save as txt by `.savetxt()` and `.loadtxt()`
- **Random**
  - Seeding
    - `rg = default_rng(seed)`
  - Use `rg` for functions
    - `.random()`, `.integers()`
- **Print options**
  - `np.set_printoptions(threshold=x)`
    - Prints more items up to x
