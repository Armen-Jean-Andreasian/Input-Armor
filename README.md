# Input Armor

## About 

---

### InputArmor is designed to help you protect your Python applications from malicious input. 

#### It provides protection from SQL-injections, DOM-manipulation (HTML injections), CMD injections, and almost all types of injections, and potential security vulnerabilities, raising `AssertionError` when invalid input is detected.


### InputArmor provides three checkup methods:

1. **Advanced check**
   - Check for non-utf-8 encoding of user input
   - Check for unsatisfying length of user input
   - Check for threats in a single word input
   - Check for most common keywords in user input
   - Check for punctuation symbols in user input
   - Check for undefined value as user input
2. **Sql Injection check**
3. **HTML Injection (DOM-Manipulation) check**


Both **Sql Injection** and **HTML Injection** checks:
- Have two levels:
    - soft check: Checks against a basic small list.
      - The small list of Sql Injection consists of 13 items.
      - The small list of HTML Injection (DOM-Manipulation) consists of 44 items.

    - deep check: check against a large list.
      - The large list of Sql Injection consists of 159 items.
      - The large list of HTML Injection consists of 127 items.

- Support:
  - white_list: An iterable with custom values that are allowed to have.
  - black_list: An iterable with custom values that are not allowed to have.

The package operates in a specific way. It doesn't return `True` or `False`.
- If the test passes: `None` will be returned.
- If the test fails:  `AssertionError` will be raised with a reason in the error body.

The package tests only the input in `str` type. 
Also, the user input that gotta be tested is called `rabbit`.

---

---
# The options provided by Advanced check:


> ## Check for non-utf-8 encoding

#### Raises AssertionError if the encoding is not utf-8.

```python
from input_armor import InputArmor


user_input = "й, ў, ї"

try:
    InputArmor.advanced_check(rabbit=user_input)
except AssertionError as details:
    # failure logic
    print(details)
    print(False)
else:
    # success logic
    print(True)
```

---

> ## Check for unsatisfying input length

#### Check if the input has the given length or doesn't exceed it
#### Raises an AssertionError either if the input has no length or consists of whitespaces only.

```python
from input_armor import InputArmor


user_input = "login"
max_length = 3

try:
    InputArmor.advanced_check(rabbit=user_input, check_length=True, max_length=max_length)
except AssertionError as details:
    # failure logic
    print(details)
    print(False)
else:
    # success logic
    print(True)
```
Similarly to this example, you can check for long input as well. 

---
> ## Check for threats in a single word input

#### Specially designed to detect one-word threats. Works only with a single word with no spaces.

```python
from input_armor import InputArmor


user_input = "1=1"

try:
    InputArmor.advanced_check(rabbit=user_input)
except AssertionError as details:
    # failure logic
    print(details)
    print(False)
else:
    # success logic
    print(True)
```
Similarly to wrong encoding check, no need to additional arguments to `.advanced_check()` method.
These are basic checks that should be done on any type of user input.

---

> ## Check for most common keywords 

####  Elementary check for most frequently used keywords in the user input.

The keywords are `while`, `as`, `if`, `else`, `import`, `select`, `do`


```python
from input_armor import InputArmor


user_input = "while true do something"

try:
    InputArmor.advanced_check(rabbit=user_input, check_for_keywords=True)
except AssertionError as details:
    # failure logic
    print(details)
    print(False)
else:
    # success logic
    print(True)
```
Similarly to wrong encoding check, no need to additional arguments to `.advanced_check()` method.
These are basic checks that should be done on any type of user input.

---

> ## Check for punctuation symbols

#### This check raises an AssertionError if **_any_** kind of non-alpha (non-letter) and non-numeric (non-number) symbol found in the input.

```python
from input_armor import InputArmor


user_input = "-- ls"


try:
    InputArmor.advanced_check(rabbit=user_input, check_for_punctuation_symbols=True)
except AssertionError as details:
    # failure logic
    print(details)
    print(False)
else:
    # success logic
    print(True)
```
---

> ## Check for undefined value as user input

#### Useful in situations when you have a pool of pre-defined values. 

If the user input is not found in your pool of `possible_values`, the check raises `AssertionError`.

`possible_values` should be any `Iterable` type.

```python
from input_armor import InputArmor


user_input = "banana"
pool = ("TNT", "ginger")

try:
    InputArmor.advanced_check(rabbit=user_input, check_for_undefined_value=True, possible_values=pool)
except AssertionError as details:
    # failure logic
    print(details)
    print(False)
else:
    # success logic
    print(True)
```

---

# Usage of Sql Injection check

> ## Sql Injection check. Soft mode

```python
from input_armor import InputArmor


user_input = "drop table"

try:
    InputArmor.sql_injection_check(rabbit=user_input, check_level=1)
except AssertionError as details:
    # failure logic
    print(details)
    print(False)
else:
    # success logic
    print(True)
```

**Important note**: Check the lists of each mode, to adjust the security maximally. However, if you have your list of keywords, feel free to use them by providing them as `white_list` or `black_list`.

> ## Sql Injection check. Deep mode

```python
from input_armor import InputArmor


user_input = "update string"

try:
    InputArmor.sql_injection_check(user_input, check_level=2)
except AssertionError as details:
    # failure logic
    print(details)
    print(False)
else:
    # success logic
    print(True)
```

---

# Usage of HTML Injection (DOM-Manipulation) check

Similarly to Sql Injection check

> ## HTML Injection check. Soft mode
> 
```python
from input_armor import InputArmor


user_input = "getElementById"

try:
    InputArmor.html_injection_check(rabbit=user_input, check_level=1)
except AssertionError as details:
    # failure logic
    print(details)
    print(False)
else:
    # success logic
    print(True)
```

**Important note**: Check the lists of each mode, to adjust the security maximally. However, if you have your list of keywords, feel free to use them by providing them as `white_list` or `black_list`.

> ## HTML Injection check. Deep mode

```python
from input_armor import InputArmor


user_input = "localStorage"

try:
    InputArmor.html_injection_check(user_input, check_level=2)
except AssertionError as details:
    # failure logic
    print(details)
    print(False)
else:
    # success logic
    print(True)
```

---

## Author

- [Armen-Jean Andreasian](https://github.com/Armen-Jean-Andreasian/)

-- -

### Links:
- [GitHub Repository](https://github.com/Armen-Jean-Andreasian/Input-Armor.git)
- [PyPI Package](https://pypi.org/project/Input-Armor/)

---