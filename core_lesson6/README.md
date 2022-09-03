# Lesson 6 - Dealind with Sequences of Objects

## Ch2-3 Lists

- `list("string") => ['s', 't', 'r', ...]`
- Each item in a list is called an **element**
  - Can be accessed by referring to its **index**
- **Slicing**
  - `[start, end]`
  - **Does not** include the element at index `end`
- **Nested lists**
  - Lists containing another list
- **Mutable** - can be altered
  - `del list[1]` removes the element at index 1
- **Overloaded operators**
  - Concatenation `+`
  - Repetition `*`
  - *Note to self, strings are character arrays*
- **Membership**
  - `in`
    - checks if element is in the list

## Ch4 For Loops

- Iterate over a collection of objects
- `continue`
  - Jumps back to the beginning of the loop
- `range(start, end)`
  - Ending number not included in the "range"
- VS `while`
  - Use for when iterating over a **fixed collection**
  - Don't modify the list while iterating
  - `while` loops give more control

## Ch6 Git Snapshots

- **Detached head**
  - unreachable without commit hash

## Ch7 Tuples

- Tuples are **immutable**
  - Can't be changed
  - Can't add elements, remove elements, nor change elements
- Single element tuple `(1,)`
  - Add comma
- Overloaded operators
  - Same as lists `+`, `*`

## Ch8 Strings

- Strings are **immutable**

## Ch9 Testing

- **Test driven development**
- Write test cases before writing the function
- Convention
  - Start function names with `test_`
- Focus on **edge cases**
  - Think of all possible cases that could go wrong
- **Unit testing**
  - Testing the correctness of a single unit of the code
- **Debug mode**
  - Pausing at certain lines
    - Setting **breakpoints**
      - `breakpoint()`

## Ch10 Styling

- No spaces before opening bracker
- No spaces immediately inside bracket
- Spaces in slicing operations
- Trailing commas
  - Useful when list is expected to be extended
  - No space between trailing comma and closing parenthesis
- Aligning brackets
