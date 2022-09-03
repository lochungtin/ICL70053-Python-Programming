# Lesson 8 - Making Objects the Main Star

## Ch2 Sets

- A **set** is a sequential data structure
  - Order is not important
  - Doesn't have duplicates
- Denoted with `{}`
- Convert list to set by `set([...])`
- **Not subscriptable**
- **Fast** to check if element is in set
  - Use of hashing
- Set operations
  - **Union** `a | b`, `a.union(b)`
  - **Intersection** `a & b`, `a.intersection(b)`
  - **Difference** `a \ b`,  `a.difference(b)`
  - **Symmetric difference** `a ^ b`, `a.symmetric_difference(b)`
  - **Membership** `x in a`, `x not in a`
  - **Proper subset / superset** `a < b`, `a > b`
  - **Subset / superset** `a <= b`, `a >= b`, `a.issubset(b)`, `a.issuperset(b)`
- **Frozen set**
  - Immutable version of sets

## Ch3 Classes

- Create a **definition**
  - Then **instantiate** a **class instance**
    - A.k.a **object**
- Has **instance variables / attributes**
- Convention
  - Use **CamelCase** for class names
- `isinstance` to check if an object is of a given class
- **Constructors**
  - `__init__()`
    - Will actually call `__new__()` first
    - Is a magic method

## Ch4 Python Modules

- A **module** is just a `.py` file
  - A script that can be imported
- Put all the imports on top of he file
- `__name__` special variable
  - Will have value `__main__` when run as script
- **Pathing**
  - Python will first search current directory
  - Then search for `sys.path`

## Ch5 Git Add Remote

- Connect local to remote repo `git remote add origin URL`
- Push to remote `git push -u origin --all`
- Remove origin `git remote remove origin`

## Ch6-8 Object Methods

- Methods represent **behaviour**
- **Magic methods** / **dunder** (double underscore)
  - `__str__` return a more readable string than the address
  - `__add__` overload the `+` operator
    - Same with `__sub__`, `__mul__`, `__truediv__`, and`__pow__`
    - Also comparison operators
      - `__lt__`, `__le__`, `__gt__`, `__ge__`, `__eq__`, and `__ne__`
  - More dunders (out c)
    - `__len__`, `__contains__`, `__getitem__`, `__setitem__`, and `__iter__`

## Ch9 File Handling

- Python handles 2 types of files
  - **Binary**
  - **Text**
- `open(filename, option)`
  - Option
    - `r`: read only mode
    - `rb`: read binary mode (read values in **bytes**)
    - `w`: write mode
      - `a`: append mode
      - `r+`: allows reading and writing at the same time
      - `w+`: clears the file and rewrites
  - Returns file object
    - `.read(n)` reads n characters
    - `.readline()` reads a line until `\n`
    - `.write()` writes line file
    - `.close()` good practice, prevents memory leaks
      - Use `with` statement instead of explicitly closing the file
    - `.tell()` return position of file pointer
    - `.seek()` move file pointer
- `tempfile` module, to create temporary files
- `shutil` module, provides high level operations
- `os` module, provides low level functions for file and directory manipulation
- `os.path` module, provides functions to deal with paths
- `pathlib` module,`os.path` but OOP

## Ch10 Input Validation

- **Defensive programming** aka **look before you leap**
- Python recommends
  - **Easier to Ask for Forgiveness than for Permission**
    - Trust that they will do what they are supposed to do
    - Wraps statements with `try ... except` clauses
    - Maintains readability
    - Slightly more efficient
      - Not actively checking
