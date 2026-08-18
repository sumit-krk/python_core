# Logical Operators in Python

Logical operators are used when we want to work with **more than one condition or expression**.

Python provides three logical operators:

| Operator | Meaning |
|---|---|
| `and` | Both conditions must be `True` |
| `or` | At least one condition must be `True` |
| `not` | Reverses the Boolean result |

---

# 1. `and` Operator

The `and` operator returns `True` only when **both conditions are True**.

## Example

```python
age = 20

print(age > 18 and age < 25)
```

Both conditions are `True`, so the result is:

```text
True
```

---

# 2. Truth Table of `and`

| Condition 1 | Condition 2 | Result |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

Rule:

> For `and`, both conditions must be `True` for the final result to be `True`.

Example:

```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
```

Output:

```text
True
False
False
False
```

---

# 3. `or` Operator

The `or` operator returns `True` when **at least one condition is True**.

## Example

```python
age = 20

print(age < 18 or age > 18)
```

The first condition is `False`, but the second condition is `True`.

Therefore:

```text
False or True
```

Result:

```text
True
```

---

# 4. Truth Table of `or`

| Condition 1 | Condition 2 | Result |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

Rule:

> For `or`, at least one condition must be `True` for the final result to be `True`.

Example:

```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
```

Output:

```text
True
True
True
False
```

---

# 5. `not` Operator

The `not` operator reverses a Boolean result.

```python
print(not True)
print(not False)
```

Output:

```text
False
True
```

In simple terms:

```text
not True  -> False
not False -> True
```

---

# 6. Truth Table of `not`

| Condition | Result |
|---|---|
| `True` | `False` |
| `False` | `True` |

Example:

```python
x = 10

print(x > 5)
print(not (x > 5))
```

Output:

```text
True
False
```

---

# 7. Comparing the Three Logical Operators

## `and`

```text
True and True -> True
```

Both must be `True`.

## `or`

```text
True or False -> True
```

At least one must be `True`.

## `not`

```text
not True -> False
```

It reverses the result.

---

# 8. Logical Operators With Comparison Operators

Logical operators are commonly combined with comparison operators.

```python
age = 20

print(age >= 18 and age <= 25)
```

Python first evaluates:

```text
age >= 18
20 >= 18
True
```

and:

```text
age <= 25
20 <= 25
True
```

Then:

```text
True and True
```

Result:

```text
True
```

---

# 9. Another Example

```python
marks = 85

print(marks >= 40 and marks <= 100)
```

Both comparisons are `True`:

```text
85 >= 40 -> True
85 <= 100 -> True
```

Therefore:

```text
True and True
```

Output:

```text
True
```

---

# 10. Important: `and` and `or` Do Not Always Return Boolean Values

Many beginners think that:

```python
and
or
```

always return `True` or `False`.

That is **not always true in Python**.

When used with ordinary values, `and` and `or` can return one of the actual values.

Example:

```python
result = "Coffee" or "Code"

print(result)
```

Output:

```text
Coffee
```

The result is:

```text
"Coffee"
```

not:

```text
True
```

This happens because Python evaluates the **truthiness** of values.

---

# 11. Truthy and Falsy Values

Python values can behave like `True` or `False` in logical operations.

Some common **falsy** values are:

```python
False
None
0
0.0
""
[]
()
{}
```

Many other values are **truthy**.

For example:

```python
1
10
-5
"Python"
[1, 2, 3]
```

are truthy.

Remember:

> Falsy values behave like `False`, while truthy values behave like `True` in logical operations.

---

# 12. Understanding `or` With Values

Consider:

```python
result = "Coffee" or "Code"

print(result)
```

`"Coffee"` is a non-empty string, so it is truthy.

Therefore Python returns:

```text
Coffee
```

Another example:

```python
result = "" or "Code"

print(result)
```

The first value is an empty string, which is falsy.

Python therefore evaluates the second value.

Output:

```text
Code
```

---

# 13. Important Rule for `or`

For:

```python
A or B
```

Python generally:

- Returns `A` if `A` is truthy.
- Otherwise evaluates and returns `B`.

Examples:

```python
print("Coffee" or "Code")
print("" or "Code")
print(100 or 200)
print(0 or 200)
```

Output:

```text
Coffee
Code
100
200
```

---

# 14. Understanding `and` With Values

Consider:

```python
result = 0 and 50

print(result)
```

`0` is falsy.

Therefore Python stops at `0` and returns it.

Output:

```text
0
```

Another example:

```python
result = 10 and "Python"

print(result)
```

`10` is truthy.

Python therefore continues to the second value and returns:

```text
Python
```

---

# 15. Important Rule for `and`

For:

```python
A and B
```

Python generally:

- Returns `A` if `A` is falsy.
- Otherwise evaluates and returns `B`.

Examples:

```python
print(0 and 50)
print(10 and "Python")
print("" and "Code")
print("Hello" and "Python")
```

Output:

```text
0
Python

Python
```

The third result is an empty string.

---

# 16. Understanding Common Examples

## Example 1

```python
result_1 = "Coffee" or "Code"
print(result_1)
```

Output:

```text
Coffee
```

Because `"Coffee"` is truthy.

## Example 2

```python
result_2 = 0 and 50
print(result_2)
```

Output:

```text
0
```

Because `0` is falsy.

## Example 3

```python
result_3 = 10 and "Python"
print(result_3)
```

Output:

```text
Python
```

Because `10` is truthy.

## Example 4

```python
result_4 = "Coffee" and "" and "Code"
print(result_4)
```

Output:

```text

```

The result is an empty string because Python stops at the first falsy value.

## Example 5

```python
result_5 = "" or "Code"
print(result_5)
```

Output:

```text
Code
```

## Example 6

```python
result_6 = "" and "Coffee" and "Code"
print(result_6)
```

Output:

```text

```

The first value is already falsy, so Python stops there.

---

# 17. Short-Circuit Evaluation

The behavior described above is called **short-circuit evaluation**.

Python does not always evaluate every part of an `and` or `or` expression.

For `and`:

```python
A and B
```

If `A` is falsy, Python does not need to evaluate `B`.

For `or`:

```python
A or B
```

If `A` is truthy, Python does not need to evaluate `B`.

---

# 18. A Very Important Example: Division by Zero

Consider:

```python
items = 0
total_weight = 500
```

Now:

```python
print(total_weight / items > 10)
```

causes:

```text
ZeroDivisionError
```

Why?

Python tries to calculate:

```text
500 / 0
```

Division by zero is not allowed.

---

# 19. Using `and` to Avoid the Division

Now consider:

```python
items = 0
total_weight = 500

is_heavy = (items > 0) and (total_weight / items > 10)

print(is_heavy)
```

Output:

```text
False
```

Step by step:

```text
items > 0
0 > 0
False
```

So Python now has:

```text
False and (total_weight / items > 10)
```

Because the first operand of `and` is already `False`, Python stops.

It does **not** evaluate:

```python
total_weight / items
```

Therefore the division by zero never happens.

This is an example of **short-circuit evaluation**.

---

# 20. Why Parentheses Are Useful

Compare:

```python
items > 0 and total_weight / items > 10
```

with:

```python
(items > 0) and (total_weight / items > 10)
```

The second version is often easier for beginners to understand because each condition is clearly separated.

```python
(items > 0)
```

is the first condition.

```python
(total_weight / items > 10)
```

is the second condition.

Then:

```text
condition 1 and condition 2
```

Parentheses are not always required, but they can make complex expressions easier to read.

---

# 21. `and` vs `or`

Compare:

```python
print(False and True)
print(False or True)
```

Output:

```text
False
True
```

For `and`:

```text
False and True
```

Result:

```text
False
```

For `or`:

```text
False or True
```

Result:

```text
True
```

---

# 22. `not` With Comparison Operators

Example:

```python
age = 15

print(age > 18)
print(not (age > 18))
```

First:

```text
15 > 18
False
```

Then:

```text
not False
True
```

Output:

```text
False
True
```

---

# 23. Operator Precedence

For the operators discussed so far, a useful simplified order is:

```text
1. Comparison operators
2. not
3. and
4. or
```

Example:

```python
print(10 > 5 and 20 > 10)
```

Python first evaluates:

```text
10 > 5
True
```

and:

```text
20 > 10
True
```

Then:

```text
True and True
```

Result:

```text
True
```

Using parentheses can make the intended grouping clearer.

---

# 24. `and` / `or` vs `&` / `|`

Do not confuse:

```python
and
or
```

with:

```python
&
|
```

They are different operators.

For now, focus on:

```python
and
or
not
```

Bitwise operators such as `&` and `|` are a separate topic.

---

# 25. Quick Summary Table

| Operator | Basic Meaning | Example | Result |
|---|---|---|---|
| `and` | Both must be True | `True and True` | `True` |
| `or` | At least one must be True | `True or False` | `True` |
| `not` | Reverses Boolean result | `not True` | `False` |

For values:

| Expression | Result |
|---|---|
| `"Coffee" or "Code"` | `"Coffee"` |
| `"" or "Code"` | `"Code"` |
| `0 and 50` | `0` |
| `10 and "Python"` | `"Python"` |
| `"Coffee" and "" and "Code"` | `""` |
| `"" and "Coffee" and "Code"` | `""` |

---

# 26. Key Points to Remember

1. Python has three logical operators: `and`, `or`, and `not`.
2. `and` requires both operands to be truthy to continue to the second operand.
3. `or` stops when it finds a truthy operand.
4. `not` reverses the Boolean meaning of an expression.
5. `and` and `or` do not always return `True` or `False`.
6. `and` and `or` can return one of their actual operands.
7. `0`, `""`, `None`, `False`, and empty collections are common falsy values.
8. Non-empty strings and non-zero numbers are generally truthy.
9. Python uses **short-circuit evaluation** for `and` and `or`.
10. With `and`, a falsy value can stop evaluation.
11. With `or`, a truthy value can stop evaluation.
12. Short-circuit evaluation can prevent unnecessary calculations or errors.
13. Comparison operators are commonly combined with logical operators.
14. Parentheses can make complex logical expressions easier to understand.
15. `and`, `or`, and `not` are different from bitwise operators such as `&` and `|`.

---

# 27. Practice Problems

Try to solve these problems yourself before running them.

The main goal is to understand:

- `and`
- `or`
- `not`
- Truthy and falsy values
- Short-circuit evaluation
- What value `and` or `or` actually returns

## Basic Practice

### Problem 1

Predict the output:

```python
print(True and True)
```

### Problem 2

Predict the output:

```python
print(True and False)
```

### Problem 3

Predict the output:

```python
print(False or True)
```

### Problem 4

Predict the output:

```python
print(False or False)
```

### Problem 5

Predict the output:

```python
print(not True)
print(not False)
```

---

# 28. Truth Table Practice

### Problem 6

Predict all four outputs:

```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
```

### Problem 7

Predict all four outputs:

```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
```

### Problem 8

Predict the output:

```python
print(not (10 > 5))
```

### Problem 9

Predict the output:

```python
print(not (10 < 5))
```

### Problem 10

Predict the output:

```python
a = 20
b = 30

print(a < b and b > 25)
```

---

# 29. `and` With Values

### Problem 11

Predict the output:

```python
print(10 and 20)
```

### Problem 12

Predict the output:

```python
print(0 and 20)
```

### Problem 13

Predict the output:

```python
print("Python" and "Java")
```

### Problem 14

Predict the output:

```python
print("" and "Python")
```

### Problem 15

Predict the output:

```python
print(100 and 0)
```

---

# 30. `or` With Values

### Problem 16

Predict the output:

```python
print(10 or 20)
```

### Problem 17

Predict the output:

```python
print(0 or 20)
```

### Problem 18

Predict the output:

```python
print("Python" or "Java")
```

### Problem 19

Predict the output:

```python
print("" or "Python")
```

### Problem 20

Predict the output:

```python
print(0 or "")
```

---

# 31. Tricky Practice

### Problem 21

Predict the output:

```python
result = "Hello" and "Python" and "World"

print(result)
```

### Problem 22

Predict the output:

```python
result = "Hello" and "" and "World"

print(result)
```

### Problem 23

Predict the output:

```python
result = "" or "Python" or "Java"

print(result)
```

### Problem 24

Predict the output:

```python
result = 0 or "" or "Python"

print(result)
```

### Problem 25

Predict the output:

```python
result = 10 and 20 and 30

print(result)
```

### Problem 26

Predict the output:

```python
result = 10 and 0 and 30

print(result)
```

### Problem 27

Predict the output:

```python
result = 0 and 10 or 20

print(result)
```

### Problem 28

Predict the output:

```python
result = 10 or 0 and 20

print(result)
```

Be careful about operator precedence.

---

# 32. Short-Circuit Practice

### Problem 29

Predict the output:

```python
items = 0
total_weight = 500

result = (items > 0) and (total_weight / items > 10)

print(result)
```

Explain why this code does not produce `ZeroDivisionError`.

### Problem 30

Predict what happens:

```python
items = 0
total_weight = 500

result = (total_weight / items > 10) and (items > 0)

print(result)
```

Explain why this version behaves differently from Problem 29.

---

# 33. Final Challenge

Predict every output without running the code:

```python
print(True and False)
print(True or False)
print(not True)

print("Coffee" or "Code")
print("" or "Code")

print(0 and 50)
print(10 and "Python")

print("Coffee" and "" and "Code")
print("" and "Coffee" and "Code")

a = 20
b = 30

print(a > 10 and b > 20)
print(a > 50 or b > 20)
print(not (a == b))
```

After predicting the outputs, run the program and check your answers.

---

# 34. Final Challenge: Explain the Result

Consider:

```python
items = 0
total_weight = 500

is_heavy = (items > 0) and (total_weight / items > 10)

print(is_heavy)
```

Answer these questions:

1. What is the value of `items > 0`?
2. Is the first operand of `and` truthy or falsy?
3. Does Python evaluate `total_weight / items > 10`?
4. Why does the program not produce `ZeroDivisionError`?
5. What is the final value of `is_heavy`?

Try to explain the complete execution step by step in your own words.
