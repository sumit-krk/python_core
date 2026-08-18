# Membership Operators in Python

Membership operators are used to check whether a value is **present inside a sequence or collection**.

Python provides two membership operators:

| Operator | Meaning |
|---|---|
| `in` | Checks whether a value is present |
| `not in` | Checks whether a value is not present |

Membership operators generally return a Boolean result:

```text
True
False
```

---

# 1. `in` Operator

The `in` operator checks whether a value exists inside another value or collection.

## Example With a String

```python
name = "Python"

print("P" in name)
```

Output:

```text
True
```

Why?

The character `"P"` is present inside `"Python"`.

We can think of it as:

```text
"P" in "Python"
True
```

---

# 2. Another Example

```python
language = "Python"

print("y" in language)
print("z" in language)
```

Output:

```text
True
False
```

Because:

```text
"y" is present in "Python"
"z" is not present in "Python"
```

---

# 3. `not in` Operator

The `not in` operator checks whether a value is **not present** inside another value or collection.

Example:

```python
language = "Python"

print("z" not in language)
```

Output:

```text
True
```

Because `"z"` is not present inside `"Python"`.

Another example:

```python
print("P" not in language)
```

Output:

```text
False
```

Because `"P"` is present.

---

# 4. Truth Table

Membership operators return either `True` or `False`.

| Expression | Result |
|---|---|
| `"P" in "Python"` | `True` |
| `"z" in "Python"` | `False` |
| `"P" not in "Python"` | `False` |
| `"z" not in "Python"` | `True` |

---

# 5. Membership Operators With Strings

Membership operators are commonly used with strings.

```python
text = "Hello Python"

print("H" in text)
print("Python" in text)
print("Java" in text)
```

Output:

```text
True
True
False
```

Here:

```text
"H"       -> present
"Python"  -> present
"Java"    -> not present
```

---

# 6. Case Sensitivity

Membership checking with strings is **case-sensitive**.

For example:

```python
language = "Python"

print("P" in language)
print("p" in language)
```

Output:

```text
True
False
```

Why?

The string contains:

```text
P
```

but not:

```text
p
```

Uppercase and lowercase characters are different.

---

# 7. More Case-Sensitive Examples

```python
word = "Python"

print("Python" in word)
print("python" in word)
print("PYTHON" in word)
```

Output:

```text
True
False
False
```

Membership operators do not automatically convert uppercase letters into lowercase letters.

---

# 8. Checking Words Inside a String

The value on the left side does not have to be a single character.

We can check for a complete substring.

```python
message = "I am learning Python"

print("Python" in message)
print("learning" in message)
print("Java" in message)
```

Output:

```text
True
True
False
```

---

# 9. Checking Multiple Characters

```python
text = "Programming"

print("Pro" in text)
print("gram" in text)
print("ming" in text)
```

Output:

```text
True
True
True
```

Membership operators can check whether a sequence of characters appears as a substring.

---

# 10. Important: Order Matters in Strings

Consider:

```python
text = "Python"

print("Py" in text)
print("yt" in text)
print("th" in text)
print("on" in text)
```

Output:

```text
True
True
True
True
```

But:

```python
print("Pt" in text)
```

Output:

```text
False
```

Why?

`P` and `t` both exist in `"Python"`, but `"Pt"` does not occur as a continuous substring.

Membership checking for strings checks for a **continuous sequence**.

---

# 11. `not in` With Strings

Example:

```python
text = "Python"

print("Java" not in text)
print("Python" not in text)
```

Output:

```text
True
False
```

Because:

```text
"Java" is not present
"Python" is present
```

---
# We will discuss points 12 to the end later, once Lists, Tuples, Dictionaries, and other related topics have been completed.

# 12. Membership Operators With Lists

Membership operators also work with lists.

```python
numbers = [10, 20, 30, 40, 50]

print(30 in numbers)
print(100 in numbers)
```

Output:

```text
True
False
```

Because `30` is an element of the list, while `100` is not.

---

# 13. `not in` With Lists

```python
numbers = [10, 20, 30, 40, 50]

print(100 not in numbers)
print(30 not in numbers)
```

Output:

```text
True
False
```

---

# 14. Membership Checks the Elements of a List

Consider:

```python
numbers = [10, 20, 30]

print(10 in numbers)
```

Output:

```text
True
```

But:

```python
print(1 in numbers)
```

Output:

```text
False
```

Even though `1` appears inside `10`, the list contains the integer `10`, not the integer `1`.

Membership operators check **complete elements** in a list.

---

# 15. String vs Integer in a List

Consider:

```python
numbers = [10, 20, 30]

print(10 in numbers)
print("10" in numbers)
```

Output:

```text
True
False
```

Why?

These are different values and different data types:

```text
10    -> integer
"10"  -> string
```

The list contains the integer `10`, not the string `"10"`.

---

# 16. Membership Operators With Tuples

Membership operators work with tuples as well.

```python
colors = ("red", "green", "blue")

print("red" in colors)
print("yellow" in colors)
```

Output:

```text
True
False
```

---

# 17. Membership Operators With Sets

Membership operators work with sets.

```python
numbers = {10, 20, 30, 40}

print(20 in numbers)
print(100 in numbers)
```

Output:

```text
True
False
```

Because `20` exists in the set and `100` does not.

---

# 18. Membership Operators With Dictionaries

Membership operators behave differently with dictionaries.

When using `in` with a dictionary, Python checks the **keys** by default.

Example:

```python
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("name" in student)
print("age" in student)
print("Rahul" in student)
```

Output:

```text
True
True
False
```

Why?

The dictionary keys are:

```text
"name"
"age"
"course"
```

`"Rahul"` is a value, not a key.

Therefore:

```text
"Rahul" in student
False
```

---

# 19. Checking Dictionary Values

If we specifically want to check values, we can use `.values()`.

```python
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("Rahul" in student.values())
print("Python" in student.values())
```

Output:

```text
True
True
```

Now Python searches through the dictionary values.

---

# 20. Checking Dictionary Keys Explicitly

We can also use `.keys()`.

```python
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("name" in student.keys())
print("Rahul" in student.keys())
```

Output:

```text
True
False
```

Normally, `.keys()` is not necessary because:

```python
"name" in student
```

already checks dictionary keys.

---

# 21. Membership With `range`

Membership operators can also be used with `range`.

```python
numbers = range(1, 11)

print(5 in numbers)
print(15 in numbers)
```

Output:

```text
True
False
```

Because `5` is within the range from `1` to `10`.

---

# 22. `not in` With `range`

```python
numbers = range(1, 11)

print(15 not in numbers)
print(5 not in numbers)
```

Output:

```text
True
False
```

---

# 23. Membership Operators With Different Data Types

Membership operators can be used with many iterable objects.

Common examples include:

```text
str
list
tuple
set
dictionary
range
```

Example:

```python
print("a" in "apple")
print(20 in [10, 20, 30])
print("red" in ("red", "blue"))
print(50 in {10, 20, 50})
print("name" in {"name": "Amit"})
print(5 in range(1, 10))
```

Output:

```text
True
True
True
True
True
True
```

---

# 24. Membership Operators Return Boolean Values

Unlike some uses of `and` and `or`, membership operators return a Boolean result.

Example:

```python
result = "Python" in "I love Python"

print(result)
print(type(result))
```

Output:

```text
True
<class 'bool'>
```

So:

```python
"Python" in "I love Python"
```

produces a Boolean value.

---

# 25. Membership Operator With Variables

The values can be stored in variables.

```python
name = "Python"
character = "P"

print(character in name)
```

Output:

```text
True
```

Another example:

```python
numbers = [10, 20, 30, 40]
number = 50

print(number in numbers)
```

Output:

```text
False
```

---

# 26. Membership Operators With `and`

Membership operators can be combined with logical operators.

```python
text = "Python Programming"

print("Python" in text and "Programming" in text)
```

First:

```text
"Python" in text
True
```

Second:

```text
"Programming" in text
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

This combines two different operator concepts:

```text
Membership operator + Logical operator
```

---

# 27. Membership Operators With `or`

Example:

```python
text = "Python Programming"

print("Java" in text or "Python" in text)
```

First:

```text
"Java" in text
False
```

Second:

```text
"Python" in text
True
```

Therefore:

```text
False or True
```

Result:

```text
True
```

---

# 28. Membership Operators With `not`

Example:

```python
text = "Python"

print(not ("Java" in text))
```

First:

```text
"Java" in "Python"
False
```

Then:

```text
not False
True
```

Output:

```text
True
```

There is also a direct and simpler form:

```python
print("Java" not in text)
```

Both produce:

```text
True
```

---

# 29. `in` vs `not in`

Consider:

```python
text = "Python"

print("P" in text)
print("P" not in text)
```

Output:

```text
True
False
```

They are opposite checks.

```text
"P" in text
```

asks:

> Is `"P"` present?

While:

```text
"P" not in text
```

asks:

> Is `"P"` absent?

---

# 30. Important Difference: String Search vs List Membership

This is a very important concept.

With a string:

```python
print("py" in "python")
```

This checks whether `"py"` exists as a substring.

With a list:

```python
print("py" in ["python", "java"])
```

This checks whether `"py"` is a complete element of the list.

Output:

```text
False
```

because the list contains:

```text
"python"
"java"
```

but not:

```text
"py"
```

---

# 31. Another Tricky Example

```python
numbers = [10, 20, 30]

print(10 in numbers)
print("10" in numbers)
print(1 in numbers)
```

Output:

```text
True
False
False
```

Remember:

```text
10    -> integer
"10"  -> string
1     -> integer
```

The list contains only the integer `10`, not `"10"` or `1`.

---

# 32. Empty Collections

Membership operators can also be used with empty collections.

```python
numbers = []

print(10 in numbers)
print(10 not in numbers)
```

Output:

```text
False
True
```

There is nothing inside the list, so `10` cannot be present.

---

# 33. Nested Lists

Be careful when working with nested lists.

```python
numbers = [[10, 20], [30, 40]]

print(10 in numbers)
print([10, 20] in numbers)
```

Output:

```text
False
True
```

Why?

The elements of the outer list are:

```text
[10, 20]
[30, 40]
```

The integer `10` is inside the first inner list, but it is not an element of the outer list.

Therefore:

```text
10 in numbers
False
```

But:

```text
[10, 20] in numbers
True
```

---

# 34. Membership and Case Sensitivity

For strings, membership is case-sensitive.

```python
text = "Python Programming"

print("Python" in text)
print("python" in text)
print("PROGRAMMING" in text)
print("Programming" in text)
```

Output:

```text
True
False
False
True
```

---

# 35. Important Rules to Remember

1. Python has two membership operators: `in` and `not in`.
2. `in` checks whether a value is present.
3. `not in` checks whether a value is absent.
4. Membership operators return `True` or `False`.
5. Strings perform substring membership checking.
6. String membership is case-sensitive.
7. Lists check their individual elements.
8. Tuples check their individual elements.
9. Sets check their individual elements.
10. Dictionaries check keys by default.
11. Dictionary values can be checked using `.values()`.
12. `range` can also be used with membership operators.
13. `10` and `"10"` are different values.
14. In a list, `1 in [10, 20, 30]` is `False`.
15. In nested lists, membership checks the immediate elements of the collection.
16. `in` and `not in` are opposite membership checks.
17. Membership operators can be combined with logical operators.

---

# 36. Quick Summary Table

| Data Type | Example | What Is Checked? |
|---|---|---|
| String | `"a" in "apple"` | Substring |
| List | `10 in [10, 20]` | Elements |
| Tuple | `10 in (10, 20)` | Elements |
| Set | `10 in {10, 20}` | Elements |
| Dictionary | `"name" in student` | Keys |
| Dictionary | `"Rahul" in student.values()` | Values |
| Range | `5 in range(1, 10)` | Range values |

---

# 37. Practice Problems

Try to predict the output before running each program.

Do not immediately execute the code. First understand what the membership operator is checking.

## Basic Practice

### Problem 1

```python
print("a" in "apple")
```

### Problem 2

```python
print("z" in "apple")
```

### Problem 3

```python
print("a" not in "apple")
```

### Problem 4

```python
print("z" not in "apple")
```

### Problem 5

```python
print("Python" in "I love Python")
```

### Problem 6

```python
print("Java" in "I love Python")
```

### Problem 7

```python
print("P" in "Python")
print("p" in "Python")
```

### Problem 8

```python
print("py" in "Python")
print("Py" in "Python")
```

---

# 38. List Practice

### Problem 9

```python
numbers = [10, 20, 30, 40]

print(20 in numbers)
```

### Problem 10

```python
numbers = [10, 20, 30, 40]

print(50 in numbers)
```

### Problem 11

```python
numbers = [10, 20, 30, 40]

print(50 not in numbers)
```

### Problem 12

```python
numbers = [10, 20, 30, 40]

print("20" in numbers)
```

### Problem 13

```python
numbers = [10, 20, 30, 40]

print(2 in numbers)
```

### Problem 14

```python
numbers = [10, 20, 30, 40]

print(10 in numbers)
print(10 not in numbers)
```

---

# 39. Tuple and Set Practice

### Problem 15

```python
colors = ("red", "green", "blue")

print("green" in colors)
```

### Problem 16

```python
colors = ("red", "green", "blue")

print("yellow" not in colors)
```

### Problem 17

```python
numbers = {10, 20, 30, 40}

print(30 in numbers)
```

### Problem 18

```python
numbers = {10, 20, 30, 40}

print(50 not in numbers)
```

---

# 40. Dictionary Practice

### Problem 19

Predict the output:

```python
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("name" in student)
```

### Problem 20

```python
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("Rahul" in student)
```

### Problem 21

```python
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("Rahul" in student.values())
```

### Problem 22

```python
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("course" in student.keys())
```

---

# 41. Tricky Practice

### Problem 23

Predict the output:

```python
numbers = [10, 20, 30]

print(1 in numbers)
print(10 in numbers)
print("10" in numbers)
```

### Problem 24

Predict the output:

```python
numbers = [[10, 20], [30, 40]]

print(10 in numbers)
print([10, 20] in numbers)
```

### Problem 25

Predict the output:

```python
text = "Python"

print("Py" in text)
print("Pt" in text)
print("yth" in text)
```

### Problem 26

Predict the output:

```python
text = "Python Programming"

print("Python" in text)
print("python" in text)
print("Programming" in text)
print("programming" in text)
```

### Problem 27

Predict the output:

```python
numbers = []

print(10 in numbers)
print(10 not in numbers)
```

### Problem 28

Predict the output:

```python
print(5 in range(1, 10))
print(10 in range(1, 10))
print(15 not in range(1, 10))
```

---

# 42. Combined Operator Practice

### Problem 29

Predict the output:

```python
text = "Python Programming"

print("Python" in text and "Programming" in text)
```

### Problem 30

Predict the output:

```python
text = "Python Programming"

print("Java" in text or "Python" in text)
```

---

# 43. Final Challenge

Predict all outputs without running the program:

```python
text = "Python Programming"
numbers = [10, 20, 30, 40]

print("Python" in text)
print("Java" not in text)

print(20 in numbers)
print(50 not in numbers)

print("python" in text)
print("Py" in text)

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("name" in student)
print("Rahul" in student)
print("Rahul" in student.values())

print("Python" in text and 20 in numbers)
print("Java" in text or 30 in numbers)
```

---

# 44. Final Concept Check

Answer these questions in your own words:

1. What is a membership operator?
2. What are the two membership operators in Python?
3. What does `in` do?
4. What does `not in` do?
5. Do membership operators return `True` or `False`?
6. How does membership work with strings?
7. How does membership work with lists?
8. Why is `10 in [10, 20, 30]` `True`?
9. Why is `"10" in [10, 20, 30]` `False`?
10. Why is `1 in [10, 20, 30]` `False`?
11. Why is `"P" in "Python"` `True`?
12. Why is `"p" in "Python"` `False`?
13. What does `in` check when used with a dictionary?
14. How can you check dictionary values?
15. What happens when membership is used with an empty list?
16. What happens when membership is used with a nested list?
17. What is the difference between `"py" in "Python"` and `"py" in ["Python"]`?
18. Can membership operators be combined with logical operators?
19. What is the difference between `in` and `not in`?
20. Give three real examples of where membership operators can be useful.

---

# 45. Final Summary

The two membership operators in Python are:

```python
in
not in
```

The basic idea is simple:

```text
value in collection
```

asks:

> Is this value present?

And:

```text
value not in collection
```

asks:

> Is this value absent?

Examples:

```python
"a" in "apple"
10 in [10, 20, 30]
"red" in ("red", "blue")
20 in {10, 20, 30}
"name" in {"name": "Rahul"}
5 in range(1, 10)
```

Membership operators are especially useful when working with:

```text
Strings
Lists
Tuples
Sets
Dictionaries
Ranges
```

The most important thing to remember is:

> **Membership operators check whether a value exists inside a collection or sequence.**
