# 2.13 Continue

## Objective

After completing this topic, you should be able to understand and use:

- Purpose of `continue`
- Skipping iterations
- Conditional skipping

> **Prerequisite:** You should understand variables, arithmetic operators, comparison operators, logical operators, `if` / `else`, `for` loops, `while` loops, `range()`, strings, and `break`.

---

# 1. What Is `continue`?

`continue` is a Python statement used inside a loop to **skip the remaining statements of the current iteration** and move to the next iteration.

The important idea is:

> **`continue` skips the current iteration; it does not stop the entire loop.**

For example:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

When `i` becomes `3`, Python executes:

```python
continue
```

So the `print(i)` statement for that iteration is skipped.

The loop then moves to the next iteration.

---

# 2. Why Do We Need `continue`?

Sometimes a loop needs to process many values, but one or more values should be ignored.

For example, suppose we want to print numbers from `1` to `10`, but we do not want to print `5`.

Without `continue`, we could write the condition differently.

With `continue`, the intention becomes clear:

```python
for i in range(1, 11):

    if i == 5:
        continue

    print(i)
```

Output:

```text
1
2
3
4
6
7
8
9
10
```

The loop continues after skipping `5`.

---

# 3. Basic Syntax

The basic syntax is:

```python
continue
```

It is normally used inside a loop, often with a condition:

```python
for ...:

    if condition:
        continue

    # remaining statements
```

Meaning:

```text
Condition False → execute remaining statements
Condition True  → skip remaining statements and continue the loop
```

---

# 4. How `continue` Works

Consider:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Execution:

```text
i = 1 → condition false → print 1
i = 2 → condition false → print 2
i = 3 → condition true  → continue
i = 4 → condition false → print 4
i = 5 → condition false → print 5
```

Output:

```text
1
2
4
5
```

Notice that the loop does not end at `3`.

---

# 5. `continue` Does Not Stop the Loop

This is the most important difference between `continue` and `break`.

Consider:

```python
for i in range(1, 6):

    if i == 3:
        break

    print(i)
```

Output:

```text
1
2
```

The loop stops.

Now:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

The loop continues.

### Remember

```text
break    → stop the loop
continue → skip this iteration
```

---

# 6. `continue` Means "Go to the Next Iteration"

Think of a loop as a series of iterations:

```text
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

If `continue` occurs during iteration `3`:

```text
Iteration 1 → normal
Iteration 2 → normal
Iteration 3 → skipped
Iteration 4 → normal
Iteration 5 → normal
```

So:

> **`continue` does not remove the loop. It only skips the remaining work of the current iteration.**

---

# 7. Position of `continue` Matters

Consider:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

The `print()` statement is after `continue`, so it is skipped when `i == 3`.

Now consider:

```python
for i in range(1, 6):

    print(i)

    if i == 3:
        continue
```

Output:

```text
1
2
3
4
5
```

Here, `print(i)` happens before `continue`.

Therefore, `3` is printed.

The `continue` affects statements **after it**, not statements that have already executed.

---

# 8. Conditional Skipping

The most common use of `continue` is conditional skipping.

Pattern:

```python
for i in range(...):

    if condition:
        continue

    # process the value
```

Meaning:

> If the condition is true, ignore this value and move to the next iteration.

Example:

```python
for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)
```

Output:

```text
1
3
5
7
9
```

Here, even numbers are skipped.

---

# 9. Skipping Even Numbers

```python
for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)
```

The condition:

```python
i % 2 == 0
```

checks whether `i` is even.

When it is even:

```python
continue
```

skips the remaining statements.

Therefore, only odd numbers are printed.

---

# 10. Skipping Odd Numbers

We can reverse the condition:

```python
for i in range(1, 11):

    if i % 2 != 0:
        continue

    print(i)
```

Output:

```text
2
4
6
8
10
```

The odd numbers are skipped, so only even numbers are processed.

---

# 11. Skipping Multiples of a Number

Suppose we want to print numbers from `1` to `20`, but skip multiples of `3`.

```python
for i in range(1, 21):

    if i % 3 == 0:
        continue

    print(i)
```

Output:

```text
1
2
4
5
7
8
10
11
13
14
16
17
19
20
```

Every multiple of `3` is skipped.

---

# 12. Skipping a Specific Value

```python
for i in range(1, 11):

    if i == 7:
        continue

    print(i)
```

Output:

```text
1
2
3
4
5
6
8
9
10
```

Only `7` is skipped.

---

# 13. Skipping a Range of Values

Suppose we want to skip numbers from `5` through `8`.

```python
for i in range(1, 11):

    if i >= 5 and i <= 8:
        continue

    print(i)
```

Output:

```text
1
2
3
4
9
10
```

The condition identifies the values that should be skipped.

---

# 14. `continue` with Strings

`continue` can also be used while iterating over a string.

For example:

```python
text = "python"

for ch in text:

    if ch == "o":
        continue

    print(ch)
```

Output:

```text
p
y
t
h
n
```

The character `"o"` is skipped.

> **New syntax note:** `for ch in text` means that each character of the string is processed one by one. This is the same string iteration concept introduced earlier.

---

# 15. Skipping a Particular Character

```python
text = "banana"

for ch in text:

    if ch == "a":
        continue

    print(ch)
```

Output:

```text
b
n
n
```

Every occurrence of `"a"` is skipped.

---

# 16. Skipping Spaces in a String

Suppose:

```python
text = "hello world"
```

We want to print every character except spaces.

```python
for ch in text:

    if ch == " ":
        continue

    print(ch)
```

Output:

```text
h
e
l
l
o
w
o
r
l
d
```

The space is skipped.

---

# 17. `continue` with `while`

`continue` can also be used in a `while` loop.

Example:

```python
i = 1

while i <= 5:

    if i == 3:
        i = i + 1
        continue

    print(i)
    i = i + 1
```

Output:

```text
1
2
4
5
```

The value `3` is skipped.

---

# 18. Important: Updating a `while` Loop

Be very careful when using `continue` with `while`.

Consider:

```python
i = 1

while i <= 5:

    if i == 3:
        continue

    print(i)
    i = i + 1
```

This program has a problem.

When:

```text
i = 3
```

the program executes:

```python
continue
```

The statement:

```python
i = i + 1
```

is skipped.

So `i` remains `3`.

The loop checks:

```text
3 <= 5
```

again.

Then `continue` executes again.

This keeps happening.

The loop becomes infinite.

---

# 19. Correct `while` Loop with `continue`

We must update the loop-control variable before `continue`.

```python
i = 1

while i <= 5:

    if i == 3:
        i = i + 1
        continue

    print(i)
    i = i + 1
```

Now:

```text
i = 1 → print
i = 2 → print
i = 3 → update to 4 → continue
i = 4 → print
i = 5 → print
```

Output:

```text
1
2
4
5
```

### Important Rule

> **In a `while` loop, make sure the loop-control variable can still change when `continue` is executed.**

---

# 20. Another Safe Pattern for `while`

Sometimes we can update the variable before checking the condition.

For example:

```python
i = 0

while i < 5:

    i = i + 1

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

Here, `i` is updated before the `continue` can happen.

This makes the loop progress safely.

---

# 21. `continue` with Input

Suppose we want to keep asking for numbers and ignore negative numbers.

```python
count = 1

while count <= 5:

    number = int(input("Enter number: "))

    if number < 0:
        count = count + 1
        continue

    print("Accepted:", number)
    count = count + 1
```

Negative numbers are skipped.

The loop still continues to process the remaining attempts.

---

# 22. Skipping Invalid Values

Suppose we want to process only positive numbers.

```python
for i in range(-3, 6):

    if i <= 0:
        continue

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

The values that do not satisfy our requirement are skipped.

---

# 23. `continue` in Number Processing

Suppose we want to print numbers from `1` to `20` but skip numbers divisible by both `2` and `3`.

```python
for i in range(1, 21):

    if i % 2 == 0 and i % 3 == 0:
        continue

    print(i)
```

Numbers such as:

```text
6
12
18
```

are skipped.

---

# 24. `continue` for Filtering

A useful way to think about `continue` is:

> **Process only the values that are relevant.**

Example:

```python
for i in range(1, 11):

    if i < 5:
        continue

    print(i)
```

Output:

```text
5
6
7
8
9
10
```

Values below `5` are ignored.

---

# 25. `continue` vs `break`

This difference must be clear.

### `continue`

Skips the current iteration.

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

### `break`

Stops the loop.

```python
for i in range(1, 6):

    if i == 3:
        break

    print(i)
```

Output:

```text
1
2
```

### Simple memory trick

```text
continue → "Skip this one"
break    → "Stop everything in this loop"
```

---

# 26. `continue` vs `if-else`

Sometimes we can solve a problem using `if-else`.

For example:

```python
for i in range(1, 6):

    if i != 3:
        print(i)
```

This prints:

```text
1
2
4
5
```

The same basic idea can be expressed with `continue`:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

The second version can be useful when there are many statements that should be skipped.

Example:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print("Number:", i)
    print("Square:", i * i)
```

When `i == 3`, both statements are skipped.

---

# 27. Skipping Multiple Statements

Consider:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print("Number:", i)
    print("Double:", i * 2)
```

Output:

```text
Number: 1
Double: 2
Number: 2
Double: 4
Number: 4
Double: 8
Number: 5
Double: 10
```

For `i == 3`, both `print()` statements are skipped.

This is one reason `continue` can make loop logic easier to read.

---

# 28. Nested Loops and `continue`

Like `break`, `continue` affects the nearest loop containing it.

Example:

```python
for i in range(3):

    for j in range(5):

        if j == 2:
            continue

        print(i, j)
```

When `j == 2`, the current iteration of the **inner loop** is skipped.

The outer loop continues normally.

Output:

```text
0 0
0 1
0 3
0 4
1 0
1 1
1 3
1 4
2 0
2 1
2 3
2 4
```

---

# 29. `continue` in Nested Loops

Remember:

> **`continue` skips the current iteration of the nearest loop in which it appears.**

It does not automatically skip the outer loop.

Example:

```python
for row in range(3):

    for column in range(5):

        if column == 2:
            continue

        print("*", end="")

    print()
```

Output:

```text
****
****
****
```

Each row skips the iteration where `column == 2`.

---

# 30. Dry Run of Nested `continue`

For:

```python
for i in range(2):

    for j in range(4):

        if j == 1:
            continue

        print(i, j)
```

First outer iteration:

```text
i = 0

j = 0 → print
j = 1 → continue
j = 2 → print
j = 3 → print
```

Second outer iteration:

```text
i = 1

j = 0 → print
j = 1 → continue
j = 2 → print
j = 3 → print
```

Output:

```text
0 0
0 2
0 3
1 0
1 2
1 3
```

---

# 31. Common Beginner Mistake: Thinking `continue` Stops the Loop

Incorrect understanding:

```text
continue = stop
```

Correct understanding:

```text
continue = skip current iteration and move to next iteration
```

Example:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

The values `4` and `5` are still processed.

---

# 32. Common Beginner Mistake: Putting `continue` Before the Loop Update

This is especially dangerous with `while`.

Problem:

```python
i = 1

while i <= 5:

    if i == 3:
        continue

    i = i + 1
```

When `i == 3`, the update never happens.

The loop can never move beyond `3`.

Correct approach:

```python
i = 1

while i <= 5:

    if i == 3:
        i = i + 1
        continue

    i = i + 1
```

Now the loop progresses.

---

# 33. Common Beginner Mistake: Expecting Code After `continue` to Run

Consider:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

When `i == 3`, this:

```python
print(i)
```

does not run.

The loop immediately moves to its next iteration.

---

# 34. Common Beginner Mistake: Confusing `continue` with `break`

Compare:

```python
if i == 3:
    continue
```

with:

```python
if i == 3:
    break
```

First:

```text
skip 3 → continue with 4, 5, ...
```

Second:

```text
stop at 3 → loop ends
```

---

# 35. Common Beginner Mistake: Wrong Condition

Suppose we want to skip even numbers.

Correct:

```python
if i % 2 == 0:
    continue
```

If we write:

```python
if i % 2 != 0:
    continue
```

we skip odd numbers instead.

Always identify exactly which values should be skipped before writing the condition.

---

# 36. A Simple Decision Method

Before using `continue`, ask:

1. What values should be processed?
2. What values should be skipped?
3. What condition identifies the values to skip?
4. What statements should not execute for those values?
5. Is the `continue` inside the correct loop?
6. If it is a `while` loop, will the loop-control variable still change?

Example:

> Print positive numbers only.

Think:

```text
Values to process → positive
Values to skip    → zero and negative
Skip condition    → number <= 0
```

Code:

```python
for number in range(-3, 4):

    if number <= 0:
        continue

    print(number)
```

---

# 37. When Should You Use `continue`?

`continue` is useful when:

- Some values should be ignored.
- Some inputs are not relevant.
- You want to skip special cases.
- You want to process only values satisfying a condition.
- You want to skip multiple statements for particular iterations.
- You want to filter values while looping.
- A nested loop needs to skip selected iterations.

---

# 38. When Is `continue` Not Necessary?

Do not use `continue` just because it is available.

For a simple problem:

```python
for i in range(1, 6):

    if i > 3:
        print(i)
```

you may not need `continue`.

But when the unwanted case occurs early and there is substantial processing afterward, `continue` can make the logic clearer:

```python
for i in range(1, 6):

    if i <= 3:
        continue

    print("Number:", i)
    print("Square:", i * i)
```

---

# 39. Important Execution Rule

When Python reaches:

```python
continue
```

inside a loop:

1. Remaining statements in the current iteration are skipped.
2. The current iteration ends.
3. The loop moves toward its next iteration.
4. For a `for` loop, the next value is taken.
5. For a `while` loop, the condition is checked again.

This is why `while` loops require special care.

---

# 40. `continue` and `while` Execution Flow

Consider:

```python
i = 1

while i <= 5:

    if i == 3:
        i = i + 1
        continue

    print(i)
    i = i + 1
```

When `i == 3`:

```text
condition is true
      ↓
i = i + 1
      ↓
continue
      ↓
current iteration ends
      ↓
while condition checked again
      ↓
i = 4
```

This is safe because the loop-control variable changed.

---

# 41. `continue` and `for` Execution Flow

Consider:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

When `i == 3`:

```text
condition is true
      ↓
continue
      ↓
current iteration ends
      ↓
next value from range
      ↓
i = 4
```

The `for` loop automatically moves to the next value.

---

# 42. Useful Patterns

### Skip one value

```python
for i in range(1, 11):

    if i == 5:
        continue

    print(i)
```

### Skip even values

```python
for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)
```

### Skip odd values

```python
for i in range(1, 11):

    if i % 2 != 0:
        continue

    print(i)
```

### Skip non-positive values

```python
for i in range(-5, 6):

    if i <= 0:
        continue

    print(i)
```

### Skip a character

```python
text = "python"

for ch in text:

    if ch == "o":
        continue

    print(ch)
```

---

# 43. Key Points to Remember

1. `continue` is used inside a loop.
2. It skips the remaining statements of the current iteration.
3. It does not stop the loop.
4. The loop continues with its next iteration.
5. `continue` is commonly used with `if`.
6. The condition tells Python which iterations to skip.
7. Statements before `continue` can still execute.
8. Statements after `continue` in that iteration are skipped.
9. `continue` can be used with `for`.
10. `continue` can be used with `while`.
11. In a `while` loop, be careful that the loop-control variable still changes.
12. Otherwise, `continue` can cause an infinite loop.
13. In nested loops, `continue` affects the nearest loop.
14. `break` stops a loop.
15. `continue` skips one iteration.
16. `continue` does not terminate the entire program.
17. `continue` is useful for filtering values.
18. `continue` can skip multiple statements at once.
19. The position of `continue` affects which statements execute.
20. Always dry-run the loop when the placement of `continue` is confusing.

---

# Practice Problems

> **Note:** Solve these problems using only concepts covered so far: variables, arithmetic, comparisons, logical operators, `if` / `else`, `for`, `while`, `range()`, strings, `break`, and `continue`. Do not use lists, tuples, dictionaries, functions, recursion, comprehensions, classes, or exception handling.

## A. Basic Understanding of `continue`

### 1.
Write a `for` loop from `1` to `10` that skips `5`.

### 2.
Write a `for` loop from `1` to `20` that skips `10`.

### 3.
Print numbers from `1` to `10`, but skip `3` and `7`.

### 4.
Print numbers from `10` down to `1`, but skip `5`.

### 5.
Predict the output:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### 6.
Predict the output:

```python
for i in range(1, 6):
    print(i)
    if i == 3:
        continue
```

### 7.
Explain why `3` is printed in Problem 6 but not in Problem 5.

### 8.
Write a program that skips the number `8` while printing `1` to `15`.

### 9.
Write a program that skips every number divisible by `5` from `1` to `30`.

### 10.
Write a program that skips all numbers greater than `7` while printing `1` to `10`.

---

## B. Even and Odd Number Skipping

### 11.
Print only odd numbers from `1` to `20` using `continue`.

### 12.
Print only even numbers from `1` to `20` using `continue`.

### 13.
Print numbers from `1` to `50` but skip all even numbers.

### 14.
Print numbers from `1` to `50` but skip all odd numbers.

### 15.
Print numbers from `1` to `30` but skip multiples of `3`.

### 16.
Print numbers from `1` to `50` but skip multiples of `4`.

### 17.
Print numbers from `1` to `100` but skip numbers divisible by both `2` and `5`.

### 18.
Print numbers from `1` to `100` but skip numbers divisible by `3` or `7`.

### 19.
Print only numbers between `1` and `50` that are not divisible by `2`.

### 20.
Print only numbers between `1` and `50` that are not divisible by `3`.

---

## C. Conditional Skipping

### 21.
Print numbers from `1` to `20` but skip numbers less than `5`.

### 22.
Print numbers from `1` to `20` but skip numbers greater than `15`.

### 23.
Print numbers from `1` to `50` but skip numbers between `20` and `30`.

### 24.
Print numbers from `1` to `50` but skip numbers between `10` and `20`.

### 25.
Print numbers from `1` to `100` but skip numbers divisible by both `3` and `5`.

### 26.
Print numbers from `1` to `100` but skip numbers whose square is greater than `500`.

### 27.
Print numbers from `1` to `50` but skip numbers that are less than `10` or greater than `40`.

### 28.
Print numbers from `1` to `50` but skip numbers divisible by `2` and greater than `20`.

### 29.
Print numbers from `1` to `100` but skip numbers that are divisible by `4` or `6`.

### 30.
Print numbers from `1` to `100` but skip numbers whose remainder after division by `7` is `0`.

---

## D. Strings

### 31.
Print every character of `"python"` except `"o"`.

### 32.
Print every character of `"banana"` except `"a"`.

### 33.
Print every character of `"hello world"` except spaces.

### 34.
Print every character of `"programming"` except `"m"`.

### 35.
Print every character of `"education"` except vowels.

### 36.
Print every character of a string except the character `"a"`.

### 37.
Take a string from the user and print all characters except spaces.

### 38.
Take a string from the user and skip every occurrence of `"e"`.

### 39.
Take a string from the user and print only characters that are not spaces.

### 40.
Take a string from the user and skip a character entered by the user.

---

## E. `while` Loops

### 41.
Use a `while` loop to print numbers from `1` to `10`, skipping `5`.

### 42.
Use a `while` loop to print even numbers from `1` to `20` by skipping odd numbers.

### 43.
Use a `while` loop to print odd numbers from `1` to `20` by skipping even numbers.

### 44.
Use a `while` loop to print numbers from `1` to `20`, skipping multiples of `3`.

### 45.
Predict whether this program terminates. Explain why:

```python
i = 1

while i <= 5:

    if i == 3:
        continue

    print(i)
    i = i + 1
```

### 46.
Correct the program in Problem 45 so that it skips `3` without becoming an infinite loop.

### 47.
Write a `while` loop that counts from `1` to `20` and skips numbers divisible by `4`.

### 48.
Write a `while` loop that counts from `20` down to `1` and skips `10`.

### 49.
Write a `while` loop that processes five user-entered numbers but skips negative numbers.

### 50.
Write a `while` loop that processes ten attempts and skips any input equal to `0`.

---

## F. Input-Based Problems

### 51.
Take five numbers from the user and print only positive numbers. Use `continue` to skip zero and negative values.

### 52.
Take five numbers from the user and print only even numbers.

### 53.
Take ten numbers from the user and skip all numbers divisible by `3`.

### 54.
Take five numbers from the user. Calculate the sum of only positive numbers using `continue` to ignore non-positive values.

### 55.
Take ten numbers from the user and count only odd numbers.

### 56.
Take ten numbers from the user and skip numbers equal to `0`.

### 57.
Take five numbers from the user and print their squares, but skip negative numbers.

### 58.
Take five numbers from the user and print their doubles, but skip numbers greater than `50`.

### 59.
Take ten numbers from the user and process only numbers divisible by `5`.

### 60.
Take numbers from the user for exactly `5` attempts. Skip negative numbers and calculate the sum of the remaining values.

---

## G. Number-Based Problems

### 61.
Print numbers from `1` to `100` but skip all numbers containing a condition you define, such as being divisible by `10`.

### 62.
Print only numbers from `1` to `100` that are not divisible by `2`, `3`, or `5`.

### 63.
Print numbers from `1` to `100` but skip perfect-square values that you can identify using the concepts already covered.

### 64.
Take a number and process its digits from right to left. Skip digit `0`.

### 65.
Take a number and process its digits from right to left. Skip digit `5`.

### 66.
Take a number and count only its odd digits.

### 67.
Take a number and calculate the sum of only its even digits.

### 68.
Take a number and print only digits greater than `5`.

### 69.
Take a number and print only digits less than `5`.

### 70.
Take a number and skip all occurrences of digit `0` while processing its digits.

---

## H. Nested Loops

### 71.
Use nested loops to print three rows of five positions, but skip column `3`.

### 72.
Use nested loops to print a pattern where the inner loop skips `j == 2`.

### 73.
Predict the output:

```python
for i in range(2):
    for j in range(4):
        if j == 1:
            continue
        print(i, j)
```

### 74.
Explain which loop is affected by the `continue` in Problem 73.

### 75.
Write nested loops where the inner loop skips even values of `j`.

---

## I. `break` vs `continue`

### 76.
Write two programs:
- One using `break` to stop at `5`.
- One using `continue` to skip `5`.

### 77.
Explain the output difference between:

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

and:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### 78.
Write a program that skips `5` and continues processing.

### 79.
Write a program that stops completely at `5`.

### 80.
Give one real programming situation where `continue` is better than `break`.

---

## J. Debugging Problems

### 81.
Find the problem:

```python
i = 1

while i <= 10:

    if i == 5:
        continue

    print(i)
    i = i + 1
```

Explain why it may not terminate.

### 82.
Correct Problem 81.

### 83.
Find the problem:

```python
for i in range(1, 10):

    if i == 5:
        continue
        print(i)
```

Explain why `print(i)` does not execute for `i == 5`.

### 84.
Correct this logic so that only odd numbers are printed:

```python
for i in range(1, 11):

    if i % 2 != 0:
        continue

    print(i)
```

### 85.
Write a dry run for:

```python
for i in range(1, 7):

    if i == 2 or i == 5:
        continue

    print(i)
```

---

# Final Challenge 1: Positive Numbers Only

Take `10` numbers from the user.

Rules:

- Negative numbers should be skipped.
- Zero should be skipped.
- Positive numbers should be processed.
- Calculate the sum of positive numbers.
- Use `continue` for the skipped cases.

At the end, display the sum.

---

# Final Challenge 2: Odd Digit Sum

Take an integer from the user.

Process its digits from right to left.

Rules:

- If a digit is even, skip it using `continue`.
- Add only odd digits to the sum.
- Display the final sum.

Example:

```text
Input: 123456
Odd digits: 5, 3, 1
Sum: 9
```

---

# Final Challenge 3: Filter Numbers

Take `20` numbers from the user.

For each number:

- Skip negative numbers.
- Skip zero.
- Skip numbers divisible by `5`.
- Print all remaining numbers.

Use `continue` for every case that should be ignored.

---

# Final Challenge 4: Compare `break` and `continue`

Write two separate programs using numbers from `1` to `20`.

### Program 1

Stop completely when the number becomes `10`.

Use:

```python
break
```

### Program 2

Skip only the number `10` and continue until `20`.

Use:

```python
continue
```

Then explain the difference in your own words.

---

# Final Revision

Before moving to the next topic, make sure you can explain:

```python
for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)
```

You should be able to answer:

1. Which values are skipped?
2. Why are those values skipped?
3. Does the loop stop?
4. What happens after `continue`?
5. Which statement is skipped?
6. Why are odd numbers printed?
7. How would the output change if `continue` were replaced by `break`?

Also understand this important `while` pattern:

```python
i = 1

while i <= 10:

    if i == 5:
        i = i + 1
        continue

    print(i)
    i = i + 1
```

The core idea is:

> **`continue` skips the remaining work of the current iteration and moves the loop toward its next iteration.**

And remember:

```text
break    → stop the nearest loop
continue → skip the current iteration
```