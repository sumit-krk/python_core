# 🐍 Python Operators

# 1. What is an Operator?

An **operator** is a symbol or keyword used to perform an operation.

Example:

```python
10 + 5
```

Here:

```text
10   +   5
│    │   │
│    │   └── Operand
│    └────── Operator
└─────────── Operand
```

### 🧠 Easy way to remember

> **Operator = What operation to perform?**  
> **Operand = On which value?**

---

# 2. Types of Operators

| Type | Purpose | Examples |
|---|---|---|
| Arithmetic | Mathematical calculations | `+ - * / % // **` |
| Assignment | Assign/update values | `= += -= *=` |
| Comparison | Compare values | `== != > < >= <=` |
| Logical | Combine conditions | `and or not` |
| Membership | Check if a value exists | `in`, `not in` |

> ⭐ Today: **Arithmetic Operators**

---

# 3. Arithmetic Operators

Arithmetic operators are used for mathematical calculations.

| Operator | Name | Example | Result |
|---|---|---:|---:|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `%` | Modulus | `10 % 3` | `1` |
| `//` | Floor Division | `10 // 3` | `3` |
| `**` | Power | `2 ** 3` | `8` |

---

# 4. ➕ Addition `+`

Adds two values.

```python
a = 10
b = 5

print(a + b)
```

Output:

```text
15
```

### 🎤 Capsule

> `+` → **Add**

---

# 5. ➖ Subtraction `-`

Subtracts one value from another.

```python
print(10 - 5)
```

Output:

```text
5
```

### 🎤 Capsule

> `-` → **Subtract**

---

# 6. ✖️ Multiplication `*`

Multiplies values.

```python
price = 50
quantity = 4

total = price * quantity

print(total)
```

Output:

```text
200
```

### 🎤 Capsule

> `*` → **Multiply**

---

# 7. ➗ Division `/`

Performs normal division.

```python
print(10 / 5)
print(7 / 2)
```

Output:

```text
2.0
3.5
```

### ⚠️ Important

Python's `/` returns a **float**.

```text
10 / 5 → 2.0
```

not:

```text
2
```

### 🎤 Capsule

> `/` → **Normal Division**

🧠 **Memory:** Single slash `/` → Normal division.

---

# 8. `%` Modulus — Remainder

Returns the **remainder** after division.

```python
print(10 % 3)
```

Output:

```text
1
```

Because:

```text
10 ÷ 3

3 × 3 = 9
10 - 9 = 1
```

### 🎯 Common use: Even / Odd

```python
number = 8

print(number % 2)
```

Output:

```text
0
```

If:

```python
number % 2 == 0
```

→ **Even**

Otherwise → **Odd**

### 🎤 Capsule

> `%` → **Remainder**

---

# 9. `//` Floor Division

Returns the **floor value** of a division.

```python
print(7 / 2)
print(7 // 2)
```

Output:

```text
3.5
3
```

### ⭐ Best way to understand `//` and `%`

Suppose:

```python
students = 23
students_per_group = 5
```

Complete groups:

```python
print(students // students_per_group)
```

Output:

```text
4
```

Remaining students:

```python
print(students % students_per_group)
```

Output:

```text
3
```

Remember:

> `//` → **Complete groups**  
> `%` → **Remaining items**

### ⚠️ Important: Negative Numbers

`//` does **not** simply remove the decimal.

```python
print(-7 / 2)
print(-7 // 2)
```

Output:

```text
-3.5
-4
```

Why?

> Floor division moves toward **negative infinity**.

### 🎤 Capsule

> `//` → **Floor / lower value**

---

# 10. ⚡ Power `**`

Used for exponentiation.

```python
print(2 ** 3)
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2 = 8
```

Another example:

```python
print(5 ** 2)
```

Output:

```text
25
```

### 🎤 Capsule

> `**` → **Power**

🧠 **Memory:** Double star `**` → Power.

---

# 11. 🧠 `/` vs `//` vs `%`

Suppose:

```python
a = 23
b = 5
```

| Operator | Meaning | Result |
|---|---|---:|
| `/` | Normal division | `4.6` |
| `//` | Complete/lower groups | `4` |
| `%` | Remaining value | `3` |

Think:

```text
23 ÷ 5

Exact result       → 4.6   → /
Complete groups    → 4     → //
Remaining          → 3     → %
```

---

# 12. 🧮 Operator Precedence

What will this print?

```python
result = 10 + 5 * 2
print(result)
```

Output:

```text
20
```

Why?

Multiplication happens before addition:

```text
10 + (5 × 2)
10 + 10
= 20
```

But:

```python
print((10 + 5) * 2)
```

Output:

```text
30
```

### Basic priority

```text
()
**
*  /  //  %
+  -
```

### 🎤 Capsule

> **Bracket → Power → Multiply/Divide → Add/Subtract**

---

# 13. 🧵 Bonus: `+` with Strings

`+` can also join strings.

```python
first_name = "Rahul"
last_name = "Kumar"

print(first_name + " " + last_name)
```

Output:

```text
Rahul Kumar
```

Remember:

```text
Numbers → + means Addition
Strings → + means Concatenation
```

---

# 14. ⚠️ Common Beginner Mistakes

| Mistake | Correct |
|---|---|
| `/` gives an integer | `/` normally gives a float |
| `%` means percentage | `%` means remainder |
| `//` simply removes decimals | `//` means floor division |
| `**` means multiplication | `**` means power |
| `10 / 5` → `2` | `10 / 5` → `2.0` |
| `10 % 2` → `5` | `10 % 2` → `0` |

---

# 15. 📝 Practice — Predict the Output

**Try first. Don't run the code immediately.**

### Q1

```python
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
```

### Q2

```python
print(10 / 2)
print(10 // 2)
print(10 % 2)
```

### Q3

```python
print(17 % 5)
print(20 % 6)
```

### Q4

```python
print(2 ** 4)
print(5 ** 2)
```

### Q5 — Tricky

```python
print(-7 / 2)
print(-7 // 2)
```

### Q6 — Precedence

```python
print(10 + 5 * 2)
print((10 + 5) * 2)
```

---

# 16. 📝 Practice — Write a Program

### Q1. Even or Odd

Given:

```python
number = 27
```

Use `%` to check whether the number is **Even or Odd**.

---

### Q2. Shopping Bill

Given:

```python
price = 80
quantity = 6
```

Calculate the total price.

---

### Q3. Group Problem

Given:

```python
students = 37
students_per_group = 6
```

Find:

- Complete groups
- Remaining students

Use:

```python
//
%
```

Expected:

```text
Complete Groups: 6
Remaining Students: 1
```

---

### Q4. Rectangle

Given:

```python
length = 12
width = 5
```

Calculate:

```text
Area = length × width
Perimeter = 2 × (length + width)
```

---

### Q5. Time Converter ⭐

Given:

```python
total_seconds = 367
```

Find:

- Minutes
- Remaining seconds

Expected:

```text
Minutes: 6
Seconds: 7
```

Hint:

```python
minutes = total_seconds // 60
seconds = total_seconds % 60
```

---

# 17. 🎯 Quick Revision Capsule

```text
+    → Add
-    → Subtract
*    → Multiply
/    → Normal Division
%    → Remainder
//   → Floor
**   → Power
```

### ⭐ Most Important

```text
/   → Exact/normal division
//  → Complete groups / floor
%   → Remaining items
```

### Example

```text
23 ÷ 5

23 / 5   → 4.6
23 // 5  → 4
23 % 5   → 3
```

---

# 🎤 Teacher's Short Explanation

You can explain the whole topic like this:

> **"Operator ek symbol hai jo Python ko batata hai ki kya operation perform karna hai. Jaise `+` Add karta hai, `-` Subtract karta hai, `*` Multiply karta hai aur `/` normal division karta hai. `%` remainder deta hai, `//` floor value deta hai aur `**` power ke liye use hota hai."**

Then ask:

> **"Agar mere paas 23 students hain aur ek group mein 5 students aa sakte hain, to kitne complete groups banenge aur kitne students bachenge?"**

Students will naturally discover:

```python
23 // 5  # 4 groups
23 % 5   # 3 students left
```

That gives them a practical reason to remember `//` and `%`.

---

# 🚀 Next Topic

After Arithmetic Operators:

```text
Arithmetic
    ↓
Assignment
    ↓
Comparison
    ↓
Logical
    ↓
if / elif / else
```