# Lesson 5 - Writing Reusable and Self-explanatory Programs

## Ch2 Shortcut Assignments

- Swapping `x, y = y, x`
- Augmented assignment operators
  - `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

## Ch4 Refactoring

- **Break down** program into smaller, manageable, and reusable chunks
- Chunks should be **independent**
- Function naming
  - **Verb** phrases
    - Indicates return value (bools)
      - `has_something`
      - `is_something`
- **Top down** approach to designing the program
- One function should focus on **one** thing

## Ch5 Advanced Function Features

- **Default arguments**, so that users don't have to explicitly provide a value for everything
  - Non-default followed by default
- **Keyword arguments**, specify which default value to override
- **Multiple returns**
  - Returns a **Tuple** object
    - Made up of more than one basic object

## Ch6 Function Scope

- Any variables created inside a function is **local** to the function
  - Can't be seen or used **outside** the function definition
- **Global scope**
  - When the program is ran
    - Python gives you a **box** named global (officially named **stack frames**)
    - Every **name** (including functions) will be put into the box
    - List of names in each box is called the **namespace**
- **Local scope**
  - When python identifies a function
    - A new **local box** is created
      - Local to the function
    - Global will be made as the new box's **parent**
      - Since the function is defined in the global namespace
- Finding variables
  - If a name is not found in the local namespace
    - Python will go to the global namespace to fetch the name

## Ch7 Styling

- `lowercase_with_underscores()`
- Use verbs / verb phrases for names
- No spaces before parenthesis
- No spaces around `=`
- Surround top-level function definition with 2 blank lines
- **Indentation**
  - Align with opening bracket
  - Next line, one tab over
- **Returns**
  - Function must return an expression or never return an expression
- **Docstrings**
  - Google style

```python
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value
    """
```

## Ch8 Git Branch

- A **branch** is a pointer to the last commit
- Can have multiple branches in one repo
  - Each with its own name
- The **head** indicates which branch you are on
- To create a branch
  - `git branch branch_name`
- To rename a branch from master to main
  - `git branch -m master main`
- Always default to `main`
  - `git config --global init.defaultBranch main`
- Switching branches
  - `git checkout branch_name`
- Visual branches
  - `git log --oneline --all --graph`
- Merge branches
  - Checkout to the branch to be merged into
    - `git checkout main`
  - Merge
    - `git merge branch_name -m "message"`

## Ch10 Assert Statement

- Makes sure condition is true
  - Stop the program with an error message
- **Defensive programming**
