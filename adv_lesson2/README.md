# Lesson 2 - Advanced Object-Oriented Programming

## Ch2 Polymorphism

- Pillars of OOP - **APIE**
  - Abstraction
  - Polymorphism
  - Inheritance
  - Encapsulation
- Ability to take **many forms**
- **Abstract class**
  - Have at least one **abstract method**
  - `NotImplementedError` raised when invoking an abstract method
  - `@abstractmethod` **decorator** declare abstract method
- **Duck typing**
  - Classify objects by their **behaviour**
    - Does it have a method
  - Iterables only need the `__iter__()` method
    - Which only requires `__next__()`
  - `Scikit-learn`
    - `Estimators` must have `fit()`
    - `Predictor` must have `predict()`
    - `Transformer` must have `transform()`
    - `Model` must have `score()`
- **Interfaces**
  - Not required, python is **dynamically typed**

## Ch3 Encapsulation

- Add `__var_name` double underscore before var to make `private`
  - Use **getters** and **setters** methods
- `@property` decorators
  - Allows reading of properties with syntax `obj.prop`
- `@prop.setter` decorator
  - Allows assigning of properties with syntax `obj.prop`
- **Private** vars are not accessible to sub-classes
  - Use one underscore instead
- Not strictly enforced

## Ch4 Class Attributes and Methods

- Defined **outside** the constructor
  - Accessed by `Class.prop_name`
- Define **constants** with all CAPS
- `@classmethod` decorator
  - Defines a class method
  - Equivalent to c++ static methods
  - Used as **constructor**
    - `create(cls, attr) return cls(attr)`
- `@staticmethod` decorator
  - Just a normal function defined in the class
  - Not **necessarily**

## Ch5 Advance Python Features

- **Type hinting**
  - Allows annotated functions
- **Named tuples**
  - `from collections import namedtuple`
  - Initialisation by `namedtuple("Name", "attr1, attr2")`
  - Allows access by `tup.attr1`
- **Data class**
  - `@dataclass` class decorator
  - Saves `__init__()` and `__repr__()` code
