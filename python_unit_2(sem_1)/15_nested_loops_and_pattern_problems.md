# 2.15 Nested Loops and Pattern Problems

## Objective

After completing this topic, you should be able to understand and solve:

- Nested loop logic
- Number patterns
- Character patterns
- Row/column problems
- Basic pattern-building

> **Prerequisite:** You should already understand variables, arithmetic operators, comparison operators, logical operators, `if` / `else`, `for` loops, `range()`, strings, `while` loops, `break`, `continue`, and `pass`.

---

# 1. What Is a Nested Loop?

A **nested loop** means putting one loop inside another loop.

Example:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(j)
```

Here:

```python
for i in range(1, 4):
```

is the **outer loop**.

And:

```python
for j in range(1, 4):
```

is the **inner loop**.

So the structure is:

```text
Outer loop
    ↓
    Inner loop
```

---

# 2. Why Do We Need Nested Loops?

A single loop is useful when we want to repeat one task.

For example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

But sometimes we need repetition **inside another repetition**.

For example:

- Multiple rows
- Multiple columns
- Tables
- Patterns
- Row and column calculations

Nested loops help us solve these problems.

---

# 3. The Basic Structure

A nested `for` loop looks like:

```python
for i in range(...):

    for j in range(...):
        # work of inner loop
```

The important point is:

> **For every one iteration of the outer loop, the complete inner loop runs.**

This is the most important idea in nested loops.

---

# 4. Understanding Outer and Inner Loops

Consider:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print("*")
```

The outer loop runs 3 times.

For each outer-loop iteration, the inner loop also runs 3 times.

Therefore:

```text
3 × 3 = 9
```

stars are printed.

But they appear one below another because `print()` moves to the next line.

---

# 5. How the Nested Loop Executes

Consider:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)
```

The execution happens like this:

```text
i = 1
    j = 1
    j = 2
    j = 3

i = 2
    j = 1
    j = 2
    j = 3

i = 3
    j = 1
    j = 2
    j = 3
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

---

# 6. The Inner Loop Finishes First

This is a very important rule.

For:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)
```

When:

```text
i = 1
```

the inner loop completes:

```text
j = 1
j = 2
j = 3
```

Only after that does:

```text
i = 2
```

begin.

So:

> **The inner loop completes all its iterations before the outer loop moves to its next iteration.**

---

# 7. A Simple Trace

Consider:

```python
for i in range(1, 3):

    for j in range(1, 4):
        print(i, j)
```

Trace:

| Outer `i` | Inner `j` | Output |
|---|---:|---|
| 1 | 1 | `1 1` |
| 1 | 2 | `1 2` |
| 1 | 3 | `1 3` |
| 2 | 1 | `2 1` |
| 2 | 2 | `2 2` |
| 2 | 3 | `2 3` |

Total inner-loop executions:

```text
2 × 3 = 6
```

---

# 8. Rows and Columns

Pattern problems become much easier when you think in terms of:

```text
Rows
Columns
```

For example:

```text
* * *
* * *
* * *
```

There are:

```text
3 rows
3 columns
```

We can think:

```text
Outer loop  → rows
Inner loop  → columns
```

This is one of the most useful ideas for pattern problems.

---

# 9. First Pattern: 3 × 3 Square

We want:

```text
* * *
* * *
* * *
```

We need:

- 3 rows
- 3 stars in every row

Code:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print("*", end=" ")

    print()
```

---

# 10. Understanding `end=" "`

Normally:

```python
print("*")
```

prints `*` and moves to the next line.

So:

```python
print("*")
print("*")
```

produces:

```text
*
*
```

But:

```python
print("*", end=" ")
```

keeps the next output on the same line.

Therefore:

```python
print("*", end=" ")
```

is useful when building patterns horizontally.

---

# 11. Why Is `print()` Used After the Inner Loop?

Consider:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print("*", end=" ")

    print()
```

The inner loop prints all columns on one line.

Then:

```python
print()
```

moves to the next line.

So:

```text
Inner loop → print columns
print()     → move to next row
```

This is the basic pattern-building structure.

---

# 12. Pattern Thinking

Before writing pattern code, ask:

### Question 1
How many rows?

### Question 2
How many items in each row?

### Question 3
What should be printed?

### Question 4
Does the number of items change from row to row?

This simple process makes pattern problems much easier.

---

# 13. Square Pattern

Required:

```text
* * * *
* * * *
* * * *
* * * *
```

There are:

```text
4 rows
4 columns
```

Code:

```python
for i in range(1, 5):

    for j in range(1, 5):
        print("*", end=" ")

    print()
```

---

# 14. Rectangle Pattern

Required:

```text
* * * * *
* * * * *
* * * * *
```

There are:

```text
3 rows
5 columns
```

Code:

```python
for i in range(1, 4):

    for j in range(1, 6):
        print("*", end=" ")

    print()
```

Notice:

```text
Outer loop  → 3 rows
Inner loop  → 5 columns
```

---

# 15. General Rule for Rectangle Patterns

For:

```text
rows × columns
```

use:

```python
for i in range(1, rows + 1):

    for j in range(1, columns + 1):
        print("*", end=" ")

    print()
```

For example:

```text
4 × 6
```

means:

```text
4 rows
6 columns
```

---

# 16. Number Square Pattern

Required:

```text
1 1 1
1 1 1
1 1 1
```

Code:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(1, end=" ")

    print()
```

Here the value printed by the inner loop is always `1`.

---

# 17. Repeating Row Number

Required:

```text
1 1 1
2 2 2
3 3 3
```

Code:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(i, end=" ")

    print()
```

The important observation is:

> The value from the outer loop is printed by the inner loop.

---

# 18. Repeating Column Number

Required:

```text
1 2 3
1 2 3
1 2 3
```

Code:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(j, end=" ")

    print()
```

Here:

> The value from the inner loop is printed.

---

# 19. Row Number vs Column Number

Compare:

### Print `i`

```python
print(i, end=" ")
```

Pattern:

```text
1 1 1
2 2 2
3 3 3
```

### Print `j`

```python
print(j, end=" ")
```

Pattern:

```text
1 2 3
1 2 3
1 2 3
```

This distinction is extremely important.

---

# 20. Increasing Number Pattern

Required:

```text
1
1 2
1 2 3
1 2 3 4
```

Notice the number of columns changes:

```text
Row 1 → 1 column
Row 2 → 2 columns
Row 3 → 3 columns
Row 4 → 4 columns
```

So the inner loop depends on the outer loop.

Code:

```python
for i in range(1, 5):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()
```

---

# 21. Understanding `range(1, i + 1)`

Suppose:

```text
i = 1
```

Then:

```python
range(1, 2)
```

gives:

```text
1
```

For:

```text
i = 2
```

we get:

```python
range(1, 3)
```

giving:

```text
1 2
```

For:

```text
i = 3
```

we get:

```text
1 2 3
```

So the inner loop gets longer as the row number increases.

---

# 22. Increasing Star Pattern

Required:

```text
*
* *
* * *
* * * *
```

Code:

```python
for i in range(1, 5):

    for j in range(1, i + 1):
        print("*", end=" ")

    print()
```

The pattern works because:

```text
row 1 → 1 star
row 2 → 2 stars
row 3 → 3 stars
row 4 → 4 stars
```

---

# 23. Decreasing Star Pattern

Required:

```text
* * * *
* * *
* *
*
```

Code:

```python
for i in range(4, 0, -1):

    for j in range(1, i + 1):
        print("*", end=" ")

    print()
```

The outer loop moves:

```text
4 → 3 → 2 → 1
```

Therefore the number of stars decreases.

---

# 24. Decreasing Number Pattern

Required:

```text
1 2 3 4
1 2 3
1 2
1
```

Code:

```python
for i in range(4, 0, -1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()
```

---

# 25. Row Number Triangle

Required:

```text
1
2 2
3 3 3
4 4 4 4
```

Code:

```python
for i in range(1, 5):

    for j in range(1, i + 1):
        print(i, end=" ")

    print()
```

The outer-loop value decides what is printed.

The inner loop decides how many times it is printed.

---

# 26. Same Number in Each Row

Required:

```text
5
6 6
7 7 7
8 8 8 8
```

Code:

```python
number = 5

for i in range(1, 5):

    for j in range(1, i + 1):
        print(number + i - 1, end=" ")

    print()
```

The expression:

```python
number + i - 1
```

changes with the row.

---

# 27. Character Patterns

Pattern problems are not limited to `*` and numbers.

We can also print characters.

For example:

```text
A
A A
A A A
A A A A
```

Code:

```python
for i in range(1, 5):

    for j in range(1, i + 1):
        print("A", end=" ")

    print()
```

---

# 28. Repeating Character Rows

Required:

```text
A A A
B B B
C C C
```

Code:

```python
for i in range(1, 4):

    if i == 1:
        ch = "A"
    elif i == 2:
        ch = "B"
    else:
        ch = "C"

    for j in range(1, 4):
        print(ch, end=" ")

    print()
```

Here we use only concepts already learned.

The outer loop selects the row.

The inner loop repeats the selected character.

---

# 29. Character Sequence Without New Functions

We can also manually define the required characters using conditions.

For:

```text
A B C
A B C
A B C
```

we can write:

```python
for i in range(1, 4):

    for j in range(1, 4):

        if j == 1:
            print("A", end=" ")
        elif j == 2:
            print("B", end=" ")
        else:
            print("C", end=" ")

    print()
```

This keeps the problem within the concepts already learned.

---

# 30. Row/Column Thinking

Suppose we need:

```text
1 2 3
1 2 3
1 2 3
```

Ask:

```text
Rows = 3
Columns = 3
```

The column value changes:

```text
1 → 2 → 3
```

Therefore `j` is useful.

Code:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(j, end=" ")

    print()
```

---

# 31. Diagonal Pattern

Required:

```text
* 
  *
    *
      *
```

For a diagonal, the position of the star changes with the row.

One simple way to understand the idea is:

```text
row 1 → star at column 1
row 2 → star at column 2
row 3 → star at column 3
row 4 → star at column 4
```

Code:

```python
for i in range(1, 5):

    for j in range(1, 5):

        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
```

The condition:

```python
i == j
```

selects the diagonal positions.

---

# 32. Understanding the Diagonal

For:

```python
if i == j:
```

the star is printed only when row and column numbers are equal.

Positions:

```text
(1, 1)
(2, 2)
(3, 3)
(4, 4)
```

These positions form the diagonal.

---

# 33. Basic Row/Column Condition

We can use conditions inside nested loops.

Example:

```python
for i in range(1, 5):

    for j in range(1, 5):

        if j == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
```

This prints a star in the first column of every row.

---

# 34. First-Column Pattern

The idea is:

```text
*      
*      
*      
*      
```

The condition is:

```python
j == 1
```

because column `1` is the first column.

---

# 35. Last-Column Pattern

For a 4-column pattern:

```text
      *
      *
      *
      *
```

we can check:

```python
j == 4
```

Example:

```python
for i in range(1, 5):

    for j in range(1, 5):

        if j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
```

---

# 36. First and Last Column

Required:

```text
* * * *
*     *
*     *
* * * *
```

A beginner-friendly way is to check whether we are on the first/last row or first/last column.

```python
for i in range(1, 5):

    for j in range(1, 5):

        if i == 1 or i == 4 or j == 1 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
```

This introduces an important pattern idea:

> **Use the row and column numbers to decide what should be printed at each position.**

---

# 37. Basic Pattern-Building Strategy

For almost every beginner pattern, follow these steps.

### Step 1: Draw the expected pattern

Example:

```text
*
* *
* * *
* * * *
```

### Step 2: Count the rows

```text
4 rows
```

### Step 3: Identify columns per row

```text
1
2
3
4
```

### Step 4: Decide what is printed

Here:

```text
*
```

### Step 5: Write the outer loop

```python
for i in range(1, 5):
```

### Step 6: Write the inner loop

```python
for j in range(1, i + 1):
```

### Step 7: Print without moving to a new line

```python
print("*", end=" ")
```

### Step 8: Move to the next row

```python
print()
```

---

# 38. The Most Important Pattern Formula

For an increasing pattern:

```text
row 1 → 1 item
row 2 → 2 items
row 3 → 3 items
...
```

a common structure is:

```python
for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(..., end=" ")

    print()
```

The `...` represents whatever we want to print.

---

# 39. Decreasing Pattern Formula

For:

```text
row 1 → n items
row 2 → n-1 items
row 3 → n-2 items
...
```

a common structure is:

```python
for i in range(n, 0, -1):

    for j in range(1, i + 1):
        print(..., end=" ")

    print()
```

---

# 40. Fixed-Size Pattern Formula

For the same number of items in every row:

```python
for i in range(1, rows + 1):

    for j in range(1, columns + 1):
        print(..., end=" ")

    print()
```

This is the basic structure for squares and rectangles.

---

# 41. Why `print()` Matters in Patterns

Consider:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print("*", end=" ")

    print()
```

The inner loop creates:

```text
* * *
```

Then:

```python
print()
```

moves to the next line.

Without the final `print()`:

```text
* * * * * * * * *
```

would appear on one line.

So:

> **`end=" "` controls horizontal printing, while `print()` after the inner loop starts the next row.**

---

# 42. Common Mistake: Forgetting `end=" "`

Wrong for a horizontal row:

```python
for j in range(1, 4):
    print("*")
```

Output:

```text
*
*
*
```

If we want:

```text
* * *
```

use:

```python
for j in range(1, 4):
    print("*", end=" ")
```

---

# 43. Common Mistake: Forgetting the Final `print()`

Code:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print("*", end=" ")
```

Output:

```text
* * * * * * * * *
```

The rows do not appear separately.

Add:

```python
print()
```

after the inner loop.

---

# 44. Common Mistake: Mixing Up `i` and `j`

For:

```text
1 1 1
2 2 2
3 3 3
```

we need:

```python
print(i, end=" ")
```

For:

```text
1 2 3
1 2 3
1 2 3
```

we need:

```python
print(j, end=" ")
```

Always ask:

> Is the value changing by row or by column?

---

# 45. Common Mistake: Wrong Inner Range

Suppose we want:

```text
1
1 2
1 2 3
```

Wrong:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(j, end=" ")

    print()
```

This gives the same number of columns in every row.

We need:

```python
for j in range(1, i + 1):
```

because the number of columns depends on the row.

---

# 46. Common Mistake: Wrong Indentation

Correct:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print("*", end=" ")

    print()
```

Notice that:

```python
print("*", end=" ")
```

belongs to the inner loop.

But:

```python
print()
```

belongs to the outer loop.

This difference is very important.

---

# 47. Which `print()` Belongs to Which Loop?

Consider:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print("*", end=" ")

    print()
```

The inner-loop `print()`:

```python
print("*", end=" ")
```

runs once for every column.

The outer-loop `print()`:

```python
print()
```

runs once for every row.

So:

```text
Inner print  → columns
Outer print  → rows
```

---

# 48. Dry Run of a Square Pattern

Code:

```python
for i in range(1, 3):

    for j in range(1, 4):
        print("*", end=" ")

    print()
```

### First outer iteration

```text
i = 1
```

Inner loop:

```text
j = 1
j = 2
j = 3
```

Prints:

```text
* * *
```

Then:

```python
print()
```

moves to the next line.

### Second outer iteration

```text
i = 2
```

Again:

```text
j = 1
j = 2
j = 3
```

Prints:

```text
* * *
```

Final output:

```text
* * *
* * *
```

---

# 49. Dry Run of an Increasing Pattern

Code:

```python
for i in range(1, 4):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()
```

### `i = 1`

```text
j = 1
```

Output:

```text
1
```

### `i = 2`

```text
j = 1
j = 2
```

Output:

```text
1 2
```

### `i = 3`

```text
j = 1
j = 2
j = 3
```

Output:

```text
1 2 3
```

Final:

```text
1
1 2
1 2 3
```

---

# 50. Pattern Classification

Before coding, identify which type of pattern you have.

### Type 1: Fixed columns

```text
* * *
* * *
* * *
```

### Type 2: Increasing columns

```text
*
* *
* * *
```

### Type 3: Decreasing columns

```text
* * *
* *
*
```

### Type 4: Row-dependent value

```text
1
2 2
3 3 3
```

### Type 5: Column-dependent value

```text
1 2 3
1 2 3
1 2 3
```

### Type 6: Position-dependent pattern

```text
*
  *
    *
```

Once the pattern type is identified, writing the loops becomes much easier.

---

# 51. Pattern Building with a Variable

Instead of hard-coding the number of rows:

```python
n = 5

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print("*", end=" ")

    print()
```

Changing:

```python
n = 5
```

to:

```python
n = 8
```

creates a larger pattern.

This is why variables are useful in pattern programs.

---

# 52. User-Controlled Pattern Size

We can also take the size from the user:

```python
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print("*", end=" ")

    print()
```

For:

```text
n = 4
```

output:

```text
*
* *
* * *
* * * *
```

The important new idea here is not the input itself; the nested-loop logic remains the same.

---

# 53. Number Pattern with User-Controlled Size

```python
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()
```

If:

```text
n = 5
```

output:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

# 54. A Simple Pattern Problem-Solving Checklist

When you receive a pattern problem, ask:

1. How many rows are there?
2. How many columns are there?
3. Is the number of columns fixed?
4. Does the number of columns increase?
5. Does the number of columns decrease?
6. What value should be printed?
7. Does the printed value depend on the row?
8. Does it depend on the column?
9. Do I need a condition for a particular position?
10. Where should `print()` be placed?

---

# 55. Basic Pattern Formula Summary

### Fixed rectangle

```python
for i in range(1, rows + 1):

    for j in range(1, columns + 1):
        print(..., end=" ")

    print()
```

### Increasing

```python
for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(..., end=" ")

    print()
```

### Decreasing

```python
for i in range(n, 0, -1):

    for j in range(1, i + 1):
        print(..., end=" ")

    print()
```

These three structures solve a large number of beginner pattern problems.

---

# 56. Important Takeaways About Nested Loops

Remember:

```text
Outer loop → controls rows
Inner loop → controls columns/items inside a row
```

And:

```text
One outer iteration
        ↓
Complete inner loop
        ↓
Next outer iteration
```

This is the foundation of pattern problems.

---

# Practice Problems

> **Important:** Solve these using only concepts already covered. If a problem introduces a new pattern idea, first study the examples above.

## A. Nested Loop Fundamentals

### 1.
Write a nested loop where the outer loop runs 3 times and the inner loop runs 2 times.

### 2.
Predict the output:

```python
for i in range(1, 3):

    for j in range(1, 4):
        print(i, j)
```

### 3.
How many times does the inner loop execute?

```python
for i in range(1, 5):

    for j in range(1, 6):
        print(j)
```

### 4.
Write a nested loop that executes the inner loop 4 times for each of 3 rows.

### 5.
Predict the output:

```python
for i in range(1, 3):

    for j in range(1, 3):
        print("*", end=" ")

    print()
```

### 6.
Explain which loop controls rows in a basic pattern.

### 7.
Explain which loop controls columns in a basic pattern.

### 8.
Create a trace table for:

```python
for i in range(1, 4):

    for j in range(1, 3):
        print(i, j)
```

### 9.
How many total times will the inner statement execute for 5 outer iterations and 4 inner iterations?

### 10.
Explain why the inner loop completes before the outer loop changes.

---

## B. Square and Rectangle Patterns

### 11.
Print a `3 × 3` square of stars.

### 12.
Print a `4 × 4` square of stars.

### 13.
Print a rectangle with 3 rows and 5 columns.

### 14.
Print a rectangle with 5 rows and 3 columns.

### 15.
Print a `6 × 4` star rectangle.

### 16.
Print a square of the number `1`.

### 17.
Print a `4 × 4` square of the number `5`.

### 18.
Print a `3 × 6` rectangle containing `0`.

### 19.
Create a square where each row contains the same number.

### 20.
Create a rectangle where every position contains `*`.

---

## C. Row Number Patterns

### 21.
Print:

```text
1
2
3
4
```

using a loop.

### 22.
Print:

```text
1 1
2 2
3 3
4 4
```

### 23.
Print:

```text
1 1 1
2 2 2
3 3 3
```

### 24.
Print:

```text
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

### 25.
Print:

```text
5 5
6 6
7 7
8 8
```

### 26.
Print:

```text
2 2 2
3 3 3
4 4 4
5 5 5
```

### 27.
Write a pattern where the outer-loop value is printed 5 times per row.

### 28.
Explain why `i` is used instead of `j` for row-number patterns.

---

## D. Column Number Patterns

### 29.
Print:

```text
1 2 3
1 2 3
1 2 3
```

### 30.
Print:

```text
1 2 3 4
1 2 3 4
1 2 3 4
```

### 31.
Print:

```text
1 2
1 2
1 2
1 2
```

### 32.
Print:

```text
5 6 7
5 6 7
5 6 7
```

### 33.
Print:

```text
2 3 4 5
2 3 4 5
2 3 4 5
```

### 34.
Explain why `j` is useful for column-number patterns.

---

## E. Increasing Patterns

### 35.
Print:

```text
*
* *
* * *
* * * *
```

### 36.
Print:

```text
1
1 2
1 2 3
1 2 3 4
```

### 37.
Print:

```text
1
2 2
3 3 3
4 4 4 4
```

### 38.
Print:

```text
1
2 3
4 5 6
```

Use only arithmetic and loops.

### 39.
Print:

```text
A
A A
A A A
A A A A
```

### 40.
Print:

```text
X
X X
X X X
X X X X
X X X X X
```

### 41.
Print an increasing triangle of `0`.

### 42.
Print an increasing triangle of `5`.

### 43.
Create an increasing pattern where each row contains its row number.

### 44.
Create an increasing pattern where each row contains numbers starting from `1`.

---

## F. Decreasing Patterns

### 45.
Print:

```text
* * * *
* * *
* *
*
```

### 46.
Print:

```text
1 2 3 4
1 2 3
1 2
1
```

### 47.
Print:

```text
4 4 4 4
3 3 3
2 2
1
```

### 48.
Print a decreasing triangle of `#`.

### 49.
Print a decreasing triangle of `7`.

### 50.
Explain how the outer loop changes in a decreasing pattern.

### 51.
Convert an increasing star triangle into a decreasing star triangle.

### 52.
Convert an increasing number triangle into a decreasing number triangle.

---

## G. Character Patterns

### 53.
Print:

```text
A A A
A A A
A A A
```

### 54.
Print:

```text
A
A A
A A A
A A A A
```

### 55.
Print:

```text
B
B B
B B B
```

### 56.
Print:

```text
X X X X
X X X X
X X X X
```

### 57.
Create:

```text
A A A
B B B
C C C
```

using conditions.

### 58.
Create:

```text
A
B B
C C C
```

using conditions.

### 59.
Create:

```text
A B C
A B C
A B C
```

using conditions.

### 60.
Create:

```text
A
A B
A B C
```

using conditions.

---

## H. Row and Column Problems

### 61.
Print a `4 × 4` square with `*` only on the first column.

### 62.
Print a `4 × 4` square with `*` only on the last column.

### 63.
Print a `4 × 4` square with `*` only on the first row.

### 64.
Print a `4 × 4` square with `*` only on the last row.

### 65.
Print stars on the main diagonal:

```text
*      
  *
    *
      *
```

### 66.
Create a `5 × 5` pattern with stars on the main diagonal.

### 67.
Create a `4 × 4` border pattern:

```text
* * * *
*     *
*     *
* * * *
```

### 68.
Explain how `i` and `j` can be used to identify a position in a pattern.

---

## I. Pattern Debugging

### 69.
Find the mistake:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print("*")
```

Why does it not make a square?

### 70.
Correct the previous program.

### 71.
Find the mistake:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
print()
```

Why does the row structure not work correctly?

### 72.
Correct the indentation in:

```python
for i in range(1, 4):

    for j in range(1, 4):
        print("*", end=" ")

        print()
```

### 73.
Find the problem:

```python
for i in range(1, 5):

    for j in range(1, 5):
        print(i, end=" ")

    print()
```

What pattern does it actually produce?

### 74.
Modify Problem 73 so that it prints the column number instead.

### 75.
Find the problem:

```python
for i in range(1, 5):

    for j in range(1, 5):
        print("*", end=" ")

    print("*")
```

What is different from a normal row-ending `print()`?

---

## J. Pattern Conversion

### 76.
Convert:

```text
* * *
* * *
* * *
```

into:

```text
*
* *
* * *
```

### 77.
Convert:

```text
*
* *
* * *
```

into a decreasing pattern.

### 78.
Convert:

```text
1 1 1
2 2 2
3 3 3
```

into:

```text
1 2 3
1 2 3
1 2 3
```

### 79.
Convert a row-number pattern into a column-number pattern.

### 80.
Convert a fixed square into an increasing triangle.

### 81.
Convert an increasing triangle into a decreasing triangle.

---

## K. Challenge Problems

### 82.
Print:

```text
1
12
123
1234
12345
```

### 83.
Print:

```text
12345
1234
123
12
1
```

### 84.
Print:

```text
1
22
333
4444
55555
```

### 85.
Print:

```text
11111
2222
333
44
5
```

### 86.
Print:

```text
A
BB
CCC
DDDD
```

using conditions.

### 87.
Print:

```text
AAAA
BBB
CC
D
```

using conditions.

### 88.
Print:

```text
1 2 3 4
1 2 3
1 2
1
```

### 89.
Print:

```text
4 3 2 1
4 3 2
4 3
4
```

### 90.
Create a `5 × 5` pattern where the diagonal contains `1` and all other positions contain `0`.

---

# Final Challenges

## Final Challenge 1: Build a Square

Take `n` from the user and print an `n × n` square of stars.

For example, if:

```text
n = 4
```

output:

```text
* * * *
* * * *
* * * *
* * * *
```

---

## Final Challenge 2: Build an Increasing Triangle

Take `n` from the user and print:

```text
*
* *
* * *
...
```

up to `n` rows.

---

## Final Challenge 3: Build a Number Triangle

For:

```text
n = 5
```

print:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

## Final Challenge 4: Row and Column Pattern

Create:

```text
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
```

Think carefully about how both `i` and `j` affect the printed value.

---

## Final Challenge 5: Border Pattern

For `n = 5`, create:

```text
* * * * *
*       *
*       *
*       *
* * * * *
```

Use row and column conditions.

---

## Final Challenge 6: Diagonal Pattern

For `n = 5`, create a pattern where the star appears when the row number and column number are equal.

---

# Final Revision

Before moving forward, make sure you can explain:

### 1. What is a nested loop?

A loop inside another loop.

### 2. Which loop usually controls rows?

The outer loop.

### 3. Which loop usually controls columns?

The inner loop.

### 4. What happens to the inner loop for each outer-loop iteration?

The complete inner loop runs.

### 5. Why do we use `end=" "`?

To keep output on the same line.

### 6. Why do we use `print()` after the inner loop?

To move to the next row.

### 7. How do we create an increasing pattern?

Make the inner-loop range depend on the outer-loop value.

### 8. How do we create a decreasing pattern?

Decrease the outer-loop value or make the number of inner iterations decrease.

### 9. How do we identify a position?

Use the row value `i` and column value `j`.

### 10. What is the basic mental model?

```text
Outer loop
    ↓
Select a row
    ↓
Inner loop
    ↓
Build that row
    ↓
print()
    ↓
Next row
```

---

# Key Takeaways

- A nested loop is a loop inside another loop.
- The outer loop commonly represents rows.
- The inner loop commonly represents columns or items in a row.
- The inner loop completes before the outer loop moves to its next iteration.
- `print(..., end=" ")` is useful for horizontal pattern output.
- `print()` after the inner loop starts a new row.
- Fixed inner ranges create squares and rectangles.
- An inner range based on `i` can create increasing or decreasing patterns.
- `i` is useful for row-based values.
- `j` is useful for column-based values.
- Conditions involving `i` and `j` can control specific positions.
- Pattern problems become easier when you first identify rows, columns, values, and changing parts.
- Always trace a small example before attempting a large pattern.
- Indentation determines which loop a statement belongs to.
- The most important pattern-building idea is:

```text
Outer loop → row
Inner loop → columns/items
```