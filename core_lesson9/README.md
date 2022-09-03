# Lesson 9 - No Object is an Island

## Ch2 Object Interactions

- **Dependency** when an object method **requires another** object
- **Aggregation** or **Composition**
  - When an object is **part of** another
  - Initialising
    - Aggregation
      - Passing an instance to a constructor
      - **Less exclusive**
    - Composition
      - Create the object inside the constructor
      - **Completely exclusive**
- **Association**
  - **"has a"** relationship, not ownership

## Ch5 Comprehensions

- Set comprehension
  - `{val for val in s}`
- Dict comprehension
  - `{k: v for (k, v) in d.items()}`
- **Generator expressions**
  - If values aren't needed to be pre-stored
  - `gen = (n ** 2 for n in range(10)`
  - `next(gen)`, ...
  - Generators are **iterable**

## Ch6 JSON

- `json.load` loads file object into data object
- `json.loads` loads json string into data object
  - **Deserialisation**
- `json.dump` loads data object into string, then writes into file object
  - **Serialisation**

## Ch8 Python Packages

- **Namespace packages**
  - Allows files to be spread across directories
  - Import by
    - `sys.path.append(loc)`
- **Regular packages**
  - Must include a `__init__.py` after python3.3
    - Usually **empty** or some magic variable initialisation code
    - `__version__` version data
    - `__author__` author name
    - `__all__` allow `import *` and define what is included
  - Mutually exclusive with namespace packages

## Ch9 Exception Instances

- **Index** arguments in an error by `args = error.args`
