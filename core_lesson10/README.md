# Lesson 10 - I am Your Father

## Ch2 Inheritance

- **Subclass** (child)
- **Superclass** (parent)
  - Subclass inherits from superclass
- First line in subclass constructor `super().__init__(args...)`\
- **Method overriding**
  - To **add specifics** relating to the subclass(es)

## Ch4 More Functions

- `any([...])` returns True if **at least one** is True
- `all([...])` returns False if **at least one** is False
- `*` wildcard number of **args**
  - `fn(*args)`, `args` will be a tuple
- `**` wildcard number of **keyword args**
  - `fn(**kwargs)`, `kwargs` will be a dict
    - Key is the keyword
    - Value is the argument value
- **Forcing** keyword / positional args
  - `fn(a, *, b)` forces `b` to be a keyword arg
  - `fn(a, /, b)` forces `a` to be a positional arg

## Ch5 Lambda

- Only have **one expression**, no statements
- Sorting
  - Use tuples to sorting hierarchy

## Ch6 Higher Order Functions

- Functions that **take functions are arguments**

## Ch7 More File Handling

- `pickle` module, serialises and deserialises data into binary files
- Warning
  - Only specific to python
  - Same python version across pickles
  - Don't unpickle files from untrusted sources
- **CSV** is a plain text file
  - Structures data in a **tabular** form
  - Default **delimiter**: `,`
    - Other delimiters: `\t`, `:`, `;`
- Other modules
  - `xml.etree.ElemenTree`, creating and reading XML files
  - `wave` and `aifc`, reading and writing audio files
  - `tarfile`, reading and writing tar archives
  - `zipfile`, working with zip archives
  - `configparser`, creating and parsing configuration files
  - `PyYAML`, process YAML
  - `PyPDF2`, PDF toolkit
  - `Pillow`, image reading and manipulation

## Ch8 Unit Testing

- `unittest` built-in unit testing module
- Create test class extending `unittest.TestCase`
  - All test functions start with `test_`
  - `main()` function runs all tests
  - `-v` verbose flag allows for more error logs
- Custom assertions
  - `.assertEqual()`
  - `.assertTrue()`
  - `.assertIsInstance()`
  - `.assertIn()`
  - `.assertIsNone()`
  - `.assertLess()`
  - `.assertAlmostEqual()`
- Testing **fixtures**
  - Setup instance of object `def setUp(self)`
  - Teardown after test `def tearDown(self)`
  - Reusable
- Other testing modules
  - `pytest`
  - `doctest`

## Ch9 User-defined Exceptions

- `Exception` is a **superclass** of all other exceptions
  - Having `Exception` has the first `except` clause will forbid any of the other clauses to fire
- Raising custom exceptions
  - `class CustomException(Exception)`
