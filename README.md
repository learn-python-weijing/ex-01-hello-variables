# Exercise 01 — Hello, World & Variables

## What you'll learn
- How to print output
- How to declare and use variables
- Python's basic data types: `str`, `int`, `float`, `bool`
- Writing simple unary functions (one input, one output)
- Composing functions together using `chain`

---

## How to run the tests

```bash
pytest
```

You'll see which tests pass ✅ and which fail ❌. Your goal is to make **all tests pass**.

Before running ```pytest```, please run ```pip install -r requirements.txt``` in your terminal.

---

## Task 1 — Basic functions

Implement the following functions in `solution.py`:

- `greet(name)` — return the string `"Hello, <name>!"`
- `add(a, b)` — return the sum of `a` and `b`
- `is_even(n)` — return `True` if `n` is even, `False` otherwise
- `circle_area(radius)` — return the area of a circle using `pi = 3.14159`, rounded to 2 decimal places

**Hints**
- A string in Python uses `"double"` or `'single'` quotes
- `type(x)` tells you the type of any value
- You can do maths directly: `2 + 2`, `10 / 3`, `10 // 3` (integer division)

**Example**
```python
name = "Alice"
age = 30
print(f"Hello, {name}! You are {age} years old.")
```

---

## Task 2 — Unary functions

A **unary function** takes exactly one input and returns exactly one output.

Implement these unary functions in `solution.py`:

- `double(x)` — return `x` multiplied by 2
- `square(x)` — return `x` squared
- `negate(x)` — flip the sign of `x` (e.g. `negate(-1)` → `1`)
- `increment(x)` — return `x + 1`
- `decrement(x)` — return `x - 1`

**Example**
```python
double(3)     # 6
square(4)     # 16
negate(-5)    # 5
increment(9)  # 10
decrement(2)  # 1
```

---

## Task 3 — Compose functions with `compose`

The `compose` function is already written for you — **do not change it**.

```python
def chain(f1, f2):
    return lambda x: f2(f1(x))
```

It takes two unary functions and returns a new function that runs `f1` first, then passes the result into `f2`.

Using only `chain` and the unary functions you wrote in Task 2, create the following composed functions:

| Name | Example |
|---|---|
| `double_then_square` | `3 → 36` |
| `square_then_double` | `3 → 18` |
| `negate_then_square` | `-4 → 16` |
| `increment_then_double` | `4 → 10` |
| `double_then_negate` | `5 → -10` |

Then try chaining **more than two** functions by chaining your chains:

| Name | Example |
|---|---|
| `double_square_negate` | `3 → -36` |
| `inc_inc_double` | `3 → 10` |

Rule: each function should only consist of 1 return statement
