# Comparison (Relational) Operators in Python

## 1. What Are Comparison Operators?

Comparison operators, also called **relational operators**, are used to compare two values or expressions.

The result of a comparison is always a **Boolean value**:

- `True`
- `False`

For example:

```python
x = 10
y = 20

print(x < y)
```

Output:

```text
True
```

Here, Python compares `10` and `20`. Since `10` is less than `20`, the result is `True`.

---

## 2. Comparison Operators in Python

Python provides six commonly used comparison operators:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `10 == 10` | `True` |
| `!=` | Not equal to | `10 != 20` | `True` |
| `>` | Greater than | `20 > 10` | `True` |
| `<` | Less than | `10 < 20` | `True` |
| `>=` | Greater than or equal to | `20 >= 20` | `True` |
| `<=` | Less than or equal to | `10 <= 20` | `True` |

---

## 3. Equal To (`==`)

The `==` operator checks whether two values are equal.

```python
a = 10
b = 10

print(a == b)
```

Output:

```text
True
```

Because both values are `10`, the result is `True`.

### Important: `=` vs `==`

These two operators have different purposes.

```python
x = 10
```

Here, `=` is the **assignment operator**. It assigns `10` to `x`.

```python
x == 10
```

Here, `==` is the **comparison operator**. It checks whether `x` is equal to `10`.

Remember:

```text
=   -> Assignment
==  -> Comparison
```

---

## 4. Not Equal To (`!=`)

The `!=` operator checks whether two values are different.

```python
a = 10
b = 20

print(a != b)
```

Output:

```text
True
```

Because `10` and `20` are different, the result is `True`.

If both values are the same:

```python
print(10 != 10)
```

Output:

```text
False
```

---

## 5. Greater Than (`>`)

The `>` operator checks whether the value on the left is greater than the value on the right.

```python
age = 20

print(age > 18)
```

Output:

```text
True
```

Because `20` is greater than `18`.

---

## 6. Less Than (`<`)

The `<` operator checks whether the value on the left is less than the value on the right.

```python
age = 16

print(age < 18)
```

Output:

```text
True
```

Because `16` is less than `18`.

---

## 7. Greater Than or Equal To (`>=`)

The `>=` operator checks whether the left value is:

1. Greater than the right value, or
2. Equal to the right value.

For example:

```python
marks = 40

print(marks >= 40)
```

Output:

```text
True
```

Here, `40` is equal to `40`, so the result is `True`.

Another example:

```python
marks = 50

print(marks >= 40)
```

Output:

```text
True
```

Here, `50` is greater than `40`.

---

## 8. Less Than or Equal To (`<=`)

The `<=` operator checks whether the left value is less than or equal to the right value.

```python
age = 18

print(age <= 18)
```

Output:

```text
True
```

Because `18` is equal to `18`.

Another example:

```python
age = 15

print(age <= 18)
```

Output:

```text
True
```

Because `15` is less than `18`.

---

# 9. A Real-Life Example: Comparing Marks

Suppose we have the marks of two students and want to compare them.

```python
rahul = 75
aman = 60

print(rahul > aman)
```

Output:

```text
True
```

Here Python compares:

```python
75 > 60
```

Since `75` is greater than `60`, the result is `True`.

---

# 11. Comparing Two Variables

Comparison operators can also be used with variables.

```python
a = 50
b = 30

print(a > b)
print(a < b)
print(a == b)
print(a != b)
```

Output:

```text
True
False
False
True
```

Let's understand each comparison:

```text
50 > 30   -> True
50 < 30   -> False
50 == 30  -> False
50 != 30  -> True
```

---

# 12. Comparing Strings

Comparison operators can also be used with strings.

```python
name1 = "Rahul"
name2 = "Rahul"

print(name1 == name2)
```

Output:

```text
True
```

Python checks whether the two strings contain the same value.

Another example:

```python
name1 = "Rahul"
name2 = "Aman"

print(name1 == name2)
print(name1 != name2)
```

Output:

```text
False
True
```

---

# 13. Important Tricky Example

Consider this code:

```python
x = 10

print(x == 10)
print(x = 10)
```

The first line is correct:

```python
print(x == 10)
```

It checks whether `x` is equal to `10`.

The second line is incorrect:

```python
print(x = 10)
```

The `=` operator is used for assignment, not comparison. Python will produce a `SyntaxError`.

Remember:

```text
=   -> Assignment
==  -> Comparison
```

---

# 14. Comparison Operators Return Boolean Values

Comparison expressions always produce either `True` or `False`.

```python
a = 10
b = 20

result = a < b

print(result)
print(type(result))
```

Output:

```text
True
<class 'bool'>
```

The result is stored in the variable `result`, and its data type is `bool`.

---

# 15. A Good Example to Understand All Operators

Let's take two students and compare their marks.

```python
rahul = 75
aman = 60

print("Rahul > Aman:", rahul > aman)
print("Rahul < Aman:", rahul < aman)
print("Rahul == Aman:", rahul == aman)
print("Rahul != Aman:", rahul != aman)
print("Rahul >= Aman:", rahul >= aman)
print("Rahul <= Aman:", rahul <= aman)
```

Output:

```text
Rahul > Aman: True
Rahul < Aman: False
Rahul == Aman: False
Rahul != Aman: True
Rahul >= Aman: True
Rahul <= Aman: False
```

### Understand It Step by Step

Given:

```text
Rahul = 75
Aman  = 60
```

Python checks:

```text
75 > 60    -> True
75 < 60    -> False
75 == 60   -> False
75 != 60   -> True
75 >= 60   -> True
75 <= 60   -> False
```

This is the basic idea behind comparison operators.

---

# 16. Quick Practice Example

Try to predict the output before running the code:

```python
a = 15
b = 10

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
```

Expected output:

```text
True
False
False
True
True
False
```

---

# 17. Quick Summary

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `3 <= 5` | `True` |

---

# 18. Key Points to Remember

1. Comparison operators are used to **compare values**.
2. They return a Boolean value: `True` or `False`.
3. `==` means **equal to**, while `=` means **assignment**.
4. `!=` means **not equal to**.
5. `>` means **greater than**.
6. `<` means **less than**.
7. `>=` means **greater than or equal to**.
8. `<=` means **less than or equal to**.
9. Comparison operators can be used directly inside `print()` to see their Boolean result.
10. Comparison operators are commonly used to compare numbers, strings, and other comparable values.

---

# 19. Practice Problems

Try to solve these problems yourself before checking the output. The goal is to understand **which comparison operator should be used** and predict whether the result will be `True` or `False`.

## Basic Practice

### Problem 1

Predict the output:

```python
a = 10
b = 20

print(a == b)
```

### Problem 2

Predict the output:

```python
x = 50
y = 50

print(x == y)
```

### Problem 3

Predict the output:

```python
a = 25
b = 15

print(a > b)
print(a < b)
```

### Problem 4

Predict the output:

```python
x = 100
y = 200

print(x != y)
```

### Problem 5

Predict the output:

```python
a = 40
b = 40

print(a >= b)
print(a <= b)
```

## Intermediate Practice

### Problem 6

Write a program to compare two numbers and print the result of all six comparison operators.

Use:

```python
a = 25
b = 30
```

### Problem 7

Predict the output:

```python
a = 15
b = 10
c = 15

print(a == b)
print(a == c)
print(a != b)
```

### Problem 8

Predict the output:

```python
x = 75

print(x > 75)
print(x >= 75)
print(x < 75)
print(x <= 75)
```

### Problem 9

Predict the output:

```python
a = 5
b = 10
c = 15

print(a < b)
print(b < c)
print(a > c)
```

### Problem 10

Write a program that stores two students' marks in variables and compares their marks using `>`, `<`, `==`, and `!=`.

Use:

```python
rahul = 82
aman = 76
```

### Problem 11

Predict the output:

```python
a = 30
b = 20

result1 = a > b
result2 = a == b
result3 = a != b

print(result1)
print(result2)
print(result3)
```

### Problem 12

Write a program to check whether two numbers are equal.

Use:

```python
x = 100
y = 100
```

The program should print the Boolean result directly.

### Problem 13

Write a program to check whether one number is greater than another.

Use:

```python
a = 45
b = 30
```

### Problem 14

Write a program to check whether a number is less than or equal to another number.

Use:

```python
x = 25
y = 25
```

### Problem 15

Predict the output:

```python
a = 90
b = 100

print(a >= b)
print(a <= b)
print(b >= a)
print(b <= a)
```

## String Comparison Practice

### Problem 16

Predict the output:

```python
name1 = "Python"
name2 = "Python"

print(name1 == name2)
```

### Problem 17

Predict the output:

```python
name1 = "Python"
name2 = "Java"

print(name1 == name2)
print(name1 != name2)
```

### Problem 18

Write a program to compare two strings using `==` and `!=`.

Use:

```python
city1 = "Delhi"
city2 = "Mumbai"
```

### Problem 19

Predict the output:

```python
x = "apple"
y = "apple"
z = "banana"

print(x == y)
print(x != z)
```

## Tricky Practice

### Problem 20

Predict the output:

```python
x = 10
y = 10.0

print(x == y)
print(x != y)
```

### Problem 21

Predict the output:

```python
a = 10
b = 20

print(a > b)
print(not (a > b))
```

### Problem 22

Find the error in the following code and correct it:

```python
x = 25
print(x = 25)
```

### Problem 23

Find the error in the following code and correct it:

```python
a = 10
b = 20

print(a = b)
```

### Problem 24

Predict the output carefully:

```python
a = 5
b = 5
c = 10

print(a == b)
print(a != c)
print(c > b)
print(a >= b)
print(b <= c)
```

### Problem 25

Without running the code, write the output:

```python
a = 20
b = 20

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
```

### Problem 26

Create two variables containing different numbers. Use all six comparison operators and print each result with a meaningful label.

Example format:

```text
Greater than: True
Less than: False
Equal to: False
Not equal to: True
Greater than or equal to: True
Less than or equal to: False
```

### Problem 27

Take the following values:

```python
maths = 85
physics = 85
chemistry = 78
```

Write comparison expressions to check:

1. Whether Maths and Physics marks are equal.
2. Whether Maths marks are greater than Chemistry marks.
3. Whether Chemistry marks are less than Maths marks.
4. Whether Physics marks are not equal to Chemistry marks.

### Problem 28

Predict every output before running the program:

```python
a = 100
b = 50

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= 100)
print(b <= 50)
```

### Problem 29

Create two variables:

```python
temperature1 = 30
temperature2 = 35
```

Compare them using all six comparison operators and observe the Boolean results.

### Problem 30

Create your own example using two numbers and write **six different comparison expressions** using `==`, `!=`, `>`, `<`, `>=`, and `<=`.

Before executing the program, predict the result of every expression.

---

# 20. Challenge: Predict Without Running

Try this final challenge without executing the code:

```python
a = 20
b = 30
c = 20

print(a == c)
print(a != b)
print(b > a)
print(a < c)
print(b >= 30)
print(c <= a)
```

Write down all six outputs first, then run the program and check your answers.