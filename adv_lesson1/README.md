# Lesson 1 - Regex

## Ch2-3 Regex Basics

- Basic syntax
  - `re.match(query, search_text)`
- **Escape character** `\`
- **Any character** - wild card `.`
  - Matches any character
- **Set of characters** `[Aa]`
  - Matches *A* and *a*
- **Do not match a set** `[^Aa]`
  - Doesn't match *A* and *a*
- **Range** `[A-z]`
  - Matches all capital and lowercase letters
- **Or** `a|b`
  - Matches *a* or *b*
- **Kleene star** `a*`
  - Matches zero or more *a* characters
- **Kleene plus** `a+`
  - Matches one or more *a* characters
- **Optional** `some?`
  - Matches both *som* and *some*
- **Bounded repetitions** `ba{1,3}`
  - Matches both *ba*, *baa*, *baa*
- **Grouping** `()`

## Ch4 Boundaries

- `search()` search anywhere in the string
  - Add `^` marks the start of the sentence
  - Add `$` marks the end of the sentence
  - Add `\b` to signify the end of a word
  - **Special characters**
    - `\d` digits
    - `\D` non-digits
    - `\s` all white spaces
    - `\S` all non-white spaces
    - `\w` a word
    - `\W` all non-words

## Ch6 Patterns

- `re.finditer` finds multiple
- Pre-compile to object
  - `re.compile`
- **Non-greedy**
  - Add an extra `?`

## Ch7 Groups

- `match.groups()` retrieves the values of the group
- `P<name>` assigns a *name* to the group
  - Retrieved by `match.group("name")`
- Non-capture groups are specified by `(?: )`
- **Backreferences** `\\1` refers the first group that was captured
- **Find and replace** `.sub(ptr, rplc, str)`
- **Split by** `.split(ptr, str)`
