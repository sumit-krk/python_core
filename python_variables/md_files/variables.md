# 1. What Is a Variable?

A **variable** is a **name that refers to a value** in a Python program.

### Think of it like a labeled box

Imagine you have three boxes:

| Label | Value inside |
|---|---|
| `name` | `"Rahul"` |
| `age` | `18` |
| `marks` | `85.5` |

In Python:

```python
name = "Rahul"
age = 18
marks = 85.5
```

You can visualize it like this:

```text
name  ───────► "Rahul"
age   ───────► 18
marks ───────► 85.5
```

### Simple definition

> **A variable is a meaningful name used to refer to a value so that we can use that value later in our program.**

---

## Real-Life Example

Suppose a college has a student record:

```text
Name   → Rahul
Age    → 18
Marks  → 85
```

Instead of repeatedly writing the actual values, we give them meaningful names:

```python
name = "Rahul"
age = 18
marks = 85
```

Now:

```python
print(name)
print(age)
print(marks)
```

Output:

```text
Rahul
18
85
```

---
# 2. Creating a Variable
The basic syntax is:

```text
variable_name = value
```

Example:

```python
name = "Rahul"
age = 18
city = "Patna"
```

There are two important parts:

```text
age = 18
│     │
│     └── Value
└──────── Variable name
```
## What Does `=` Mean?

In Python, `=` is called the **assignment operator**.

It means:

> **"Assign this value to this variable."**

For example:

```python
age = 18
```

Read it as:

> **"Assign 18 to age."**
# 3. Variable Naming Rules

Python has specific rules for variable names.

## Rule 1 — Letters Are Allowed ✅

```python
name = "Rahul"
student = "Aman"
city = "Patna"
```

---

## Rule 2 — Numbers Are Allowed, But Not at the Beginning ⚠️

### ✅ Valid

```python
student1 = "Rahul"
marks10 = 95
room2 = "Lab"
```

### Invalid

```python
1student = "Rahul"
10marks = 95
2room = "Lab"
```

> **Remember:** A variable name can contain numbers, but it cannot **start** with a number.

```text
student1   ✅
1student   ❌
```

---

## Rule 3 — Underscore `_` Is Allowed ✅

```python
_student = "Rahul"
student_name = "Rahul"
student_name_1 = "Rahul"
```

---

## Rule 4 — Spaces Are NOT Allowed ❌

Invalid:

```python
student name = "Rahul"
```

Correct:

```python
student_name = "Rahul"
```

```text
student name   ❌
student_name   ✅
```

---

## Rule 5 — Special Characters Are NOT Allowed ❌

Avoid:

```text
@  #  $  %  &  -  !  ?
```

Invalid:

```python
age$ = 26
age@ = 75
student-name = "Rahul"
```

Correct:

```python
age = 26
marks = 75
student_name = "Rahul"
```

> ⚠️ **Exception:** `_` is allowed.

---

## Rule 6 — Python Keywords Cannot Be Used ❌

Python has reserved words called **keywords**:

```text
if
else
elif
for
while
def
class
return
import
True
False
None
```

These already have special meanings.

Invalid:

```python
if = 10
for = 10
class = 5
```

You can see Python's keywords using:

```python
import keyword

print(keyword.kwlist)
```

---
# 4. Python Is Case-Sensitive
Python treats uppercase and lowercase letters as different.

```python
age = 20
Age = 30
AGE = 40
```

These are **three different variables**.

```python
print(age)
print(Age)
print(AGE)
```

Output:

```text
20
30
40
```

### Best practice

Avoid confusing names such as:

```python
age
Age
AGE
```

Prefer clear names:

```python
student_age = 20
teacher_age = 30
```

---
# 5. Good vs Bad Variable Names

### Less meaningful

```python
x = 80
y = 18
z = "Rahul"
```

### Meaningful

```python
marks = 80
age = 18
name = "Rahul"
```

Ask yourself:

```python
x = 80
```

What is `80`?

It could be marks, age, temperature, or price.

But:

```python
marks = 80
```

immediately tells us what the value represents.

> **Golden rule:** Choose variable names that explain the data.

---
# 6. Python Naming Convention: `snake_case`

Python commonly uses **snake_case** for variables.

Words are written in lowercase and separated by underscores.

### Recommended

```python
student_name = "Rahul"
total_marks = 450
first_name = "Rahul"
last_name = "Kumar"
account_balance = 5000
phone_number = "9876543210"
```

### Avoid these styles for normal Python variables

```python
studentName
StudentName
student-name
student name
```

`studentName` is technically valid Python, but the common Python convention is:

```python
student_name
```

---
# 7. Variable Naming Rules — Quick Reference

| Rule | Example | Valid? |
|---|---|:---:|
| Letters | `name` | ✅ |
| Letters + numbers | `student1` | ✅ |
| Starts with number | `1student` | ❌ |
| Underscore | `student_name` | ✅ |
| Starts with `_` | `_name` | ✅ |
| Contains spaces | `student name` | ❌ |
| Contains `-` | `student-name` | ❌ |
| Contains `@` | `student@name` | ❌ |
| Python keyword | `class` | ❌ |
| Case-sensitive | `age` vs `Age` | ✅ Different |

---
# 8. Practice — Valid or Invalid?

> **Try these yourself before checking the answer key.**

Given:

```python
name = "Raj"
name2 = "Raj"
3name = "Raj"
_age = 26
class_name = "Section 4B"
if = 2
for = 10
class name = "Section-3"
age$ = 26
age@ = 75
calss@name = "8"
```

Fill in:

| Variable | Valid / Invalid | Why? |
|---|:---:|---|
| `name` | ? | ? |
| `name2` | ? | ? |
| `3name` | ? | ? |
| `_age` | ? | ? |
| `class_name` | ? | ? |
| `if` | ? | ? |
| `for` | ? | ? |
| `class name` | ? | ? |
| `age$` | ? | ? |
| `age@` | ? | ? |
| `calss@name` | ? | ? |

---
# 9. Practice Answer Key

Check only after attempting the exercise.

| Variable | Answer | Reason |
|---|:---:|---|
| `name` | ✅ | Valid letters |
| `name2` | ✅ | Number is allowed after letters |
| `3name` | ❌ | Cannot start with a number |
| `_age` | ✅ | Underscore is allowed |
| `class_name` | ✅ | Valid `snake_case` name |
| `if` | ❌ | `if` is a Python keyword |
| `for` | ❌ | `for` is a Python keyword |
| `class name` | ❌ | Spaces are not allowed |
| `age$` | ❌ | `$` is not allowed |
| `age@` | ❌ | `@` is not allowed |
| `calss@name` | ❌ | `@` is not allowed |

### ⭐ Important observation

```python
class_name = "Section 4B"
```

is valid.

But:

```python
class = 10
```

is invalid because `class` is a Python keyword.

So:

> A keyword can appear as part of a larger variable name, but the complete variable name cannot be a keyword.

---
# 10. 🎯 Practice — Create Variable Names

Convert these descriptions into proper Python variable names.

| Description | Your answer |
|---|---|
| Student name | `__________` |
| Student age | `__________` |
| Total marks | `__________` |
| Phone number | `__________` |
| Account balance | `__________` |
| First name | `__________` |
| Date of birth | `__________` |

Example:

```text
Student name → student_name
```

---