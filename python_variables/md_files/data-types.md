# 1. 🗃️ Variables Can Store Different Types of Data

| Type | Example | Used for |
|---|---|---|
| `int` | `age = 20` | Whole numbers |
| `float` | `price = 99.50` | Decimal numbers |
| `str` | `name = "Rahul"` | Text |
| `bool` | `is_student = True` | True/False |
| `NoneType` | `result = None` | No value / empty state |

Example:

```python
age = 20
height = 5.8
name = "Rahul"
is_student = True
result = None
```
# 2. 🐍 Python Is Dynamically Typed

Python does not require us to declare the type separately.

```python
value = 10
```

Python understands that the value is an integer.

Later:

```python
value = "Hello"
```

Now it refers to a string.

```python
value = 10
print(type(value))

value = "Hello"
print(type(value))
```

Output:

```text
<class 'int'>
<class 'str'>
```

> 🎯 **Dynamic typing:** Python determines the type of the value at runtime.

---

## 🔍 Checking the Type

Use `type()`:

```python
age = 20

print(type(age))
```

Output:

```text
<class 'int'>
```

Another example:

```python
name = "Rahul"

print(type(name))
```

Output:

```text
<class 'str'>
```

---