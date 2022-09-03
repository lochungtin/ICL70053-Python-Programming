# Lesson 7 - Objects and Dictionaries

## Ch2 Object Identity

- Each python object has an **identity**
  - Unique integer ID for the object
- Can use `is`, `is not` operators to check
- `id()` returns the unique ID

## Ch4 Dictionaries

- **Lookup table** with **keys** to retrieve **values**
- Keys should not be mutable
  - Don't use tuples apparently `-_-`
- `get()` can have default values if key doesn't exist
- `key()` retrieves all the keys, returns a list
- `value()` retrieves all the values, returns a list
- `extend()` concatenates dicts
- `setdefault()`, like get, but adds the entry if it doesn't exist

## Ch6 Recursion

- Requires a **base condition** to stop the recursion

## Ch7 Exception Handling

- **Runtime errors**, wrap code with `try ... except` blocks
- The `finally` must run
- Bare `except` clause is **not** recommended
