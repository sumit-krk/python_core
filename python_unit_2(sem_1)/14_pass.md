# 2.14 Pass

## Objective

After completing this topic, you should be able to understand and use:

- Purpose of `pass`
- Empty blocks
- Basic use cases of `pass`

> **Prerequisite:** You should understand variables, arithmetic operators, comparison operators, logical operators, `if` / `else`, `for` loops, `while` loops, `range()`, strings, `break`, and `continue`.

---

# 1. What Is `pass`?

`pass` is a Python statement that **does nothing**.

It is mainly used when Python requires a statement inside a block, but we do not want to write the actual code yet.

Example:

```python
if True:
    pass
```

The program runs without performing any action inside the `if` block.

The important idea is:

> **`pass` means "do nothing for now."**

---

# 2. Why Do We Need `pass`?

Python uses indentation to define blocks.

For example:

```python
if age >= 18:
    print("Adult")
```

There is a statement inside the `if` block.

But suppose we have not decided what should happen yet:

```python
if age >= 18:
```

An `if` block cannot simply be left empty.

We can temporarily write:

```python
if age >= 18:
    pass
```

Now Python has a valid statement inside the block.

---

# 3. Empty Blocks

An **empty block** means a block where we currently do not want to perform any action.

For example:

```python
if True:
    pass
```

Here:

```python
if True:
```

starts the block.

```python
pass
```

provides a statement inside the block.

The program does nothing when this block runs.

---

# 4. Basic Syntax

The basic syntax is simply:

```python
pass
```

It is normally placed inside a block:

```python
if condition:
    pass
```

or:

```python
for i in range(5):
    pass
```

or:

```python
while condition:
    pass
```

---

# 5. `pass` Does Not Stop the Program

Consider:

```python
print("Start")

if True:
    pass

print("End")
```

Output:

```text
Start
End
```

When Python reaches `pass`, it simply does nothing and then continues with the next statement.

---

# 6. `pass` Means "Do Nothing"

Consider:

```python
for i in range(1, 6):

    if i == 3:
        pass

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

Notice that `3` is still printed.

Why?

Because:

```python
pass
```

does not skip the iteration.

It does not stop the loop.

It simply does nothing.

---

# 7. `pass` vs `continue`

This is a very important difference.

### Using `pass`

```python
for i in range(1, 6):

    if i == 3:
        pass

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

`pass` does nothing, so `print(i)` still executes.

### Using `continue`

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

`continue` skips the remaining statements of the current iteration.

### Remember

```text
pass     → do nothing
continue → skip current iteration
```

---

# 8. `pass` vs `break`

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

`break` stops the loop.

Now:

```python
for i in range(1, 6):

    if i == 3:
        pass

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

`pass` does not stop anything.

### Remember

```text
pass     → do nothing
continue → skip current iteration
break    → stop the loop
```

---

# 9. `pass` Does Not Mean "Skip"

Beginners often think:

```python
pass
```

means:

> Skip this part.

That is not correct.

`pass` means:

> **Execute nothing here and then continue normally.**

For example:

```python
for i in range(1, 4):

    if i == 2:
        pass

    print(i)
```

Output:

```text
1
2
3
```

The number `2` is not skipped.

---

# 10. `pass` in an `if` Block

Suppose we want to write an `if` condition now but decide the action later.

```python
number = 10

if number > 5:
    pass
```

The condition is checked.

Since it is true, Python enters the block.

Then it executes `pass`.

Nothing happens.

The program continues.

---

# 11. `pass` with `if-else`

We can also use `pass` in one branch.

```python
number = 10

if number > 5:
    pass
else:
    print("Small number")
```

Since `number > 5` is true, the `pass` statement executes.

No output is produced.

---

# 12. `pass` in the `else` Block

We can also do:

```python
number = 3

if number > 5:
    print("Large number")
else:
    pass
```

Since the condition is false, the `else` block runs.

`pass` does nothing.

The program finishes without printing anything.

---

# 13. Why Not Just Leave the Block Empty?

Consider:

```python
number = 10

if number > 5:
```

This is incomplete.

Python expects an indented statement after the colon.

We can provide one:

```python
number = 10

if number > 5:
    pass
```

Now the block is valid.

So one basic purpose of `pass` is:

> **To create a syntactically valid block that intentionally does nothing.**

---

# 14. `pass` as a Placeholder

A placeholder is something we put temporarily until the real code is ready.

For example:

```python
number = 10

if number > 0:
    pass
```

Later, we may replace it with:

```python
number = 10

if number > 0:
    print("Positive")
```

So:

```python
pass
```

can communicate:

> "This part will be implemented later."

---

# 15. Placeholder Example

Suppose we are planning a program:

```python
number = 25

if number > 0:
    pass

if number < 0:
    pass
```

We have created the structure first.

Later, we can decide what each condition should do.

---

# 16. `pass` with `for`

`pass` can be used inside a `for` loop.

```python
for i in range(1, 6):
    pass
```

The loop runs through its values, but nothing is printed or changed inside the loop.

There is no visible output.

The loop still executes its iterations.

---

# 17. Does the Loop Run with `pass`?

Yes.

Consider:

```python
for i in range(1, 6):

    pass

print("Done")
```

Output:

```text
Done
```

The loop goes through the values, but `pass` performs no visible action.

After the loop finishes, `"Done"` is printed.

---

# 18. `pass` with `while`

`pass` can also be used in a `while` loop.

Example:

```python
i = 1

while i <= 5:

    pass

    i = i + 1
```

Here, the loop still needs:

```python
i = i + 1
```

to make progress.

The `pass` itself does not change `i`.

---

# 19. Important `while` Loop Warning

Consider:

```python
i = 1

while i <= 5:

    pass
```

This creates an infinite loop.

Why?

Because:

```python
i
```

never changes.

The condition remains:

```text
1 <= 5
```

forever.

So remember:

> **`pass` does not update variables or change the loop condition.**

---

# 20. Correct `while` Example

```python
i = 1

while i <= 5:

    pass

    i = i + 1
```

Now:

```text
i = 1
i = 2
i = 3
i = 4
i = 5
i = 6
```

When `i` becomes `6`, the condition:

```python
i <= 5
```

becomes false.

The loop stops.

---

# 21. `pass` with Conditional Logic

Suppose we want to ignore a particular condition for now.

```python
for i in range(1, 6):

    if i == 3:
        pass
    else:
        print(i)
```

Output:

```text
1
2
4
5
```

Here, the `else` branch is not executed when `i == 3`.

The `pass` branch simply does nothing.

---

# 22. `pass` Does Not Automatically Continue

Consider:

```python
for i in range(1, 6):

    if i == 3:
        pass

    print("Hello")
```

Output:

```text
Hello
Hello
Hello
Hello
Hello
```

`Hello` is printed five times.

If we wanted to skip the `print()` when `i == 3`, we would need `continue`:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print("Hello")
```

Output:

```text
Hello
Hello
Hello
Hello
```

---

# 23. `pass` Does Not Affect the Next Statement

Example:

```python
x = 10

if x == 10:
    pass

print(x)
```

Output:

```text
10
```

The `print()` statement executes normally.

---

# 24. `pass` with Nested Conditions

`pass` can be used in nested blocks.

```python
number = 10

if number > 0:

    if number > 5:
        pass

    print("Number is positive")
```

Output:

```text
Number is positive
```

The inner `pass` does nothing.

The outer block continues normally.

---

# 25. `pass` with Nested Loops

Example:

```python
for i in range(1, 4):

    for j in range(1, 4):

        if j == 2:
            pass

        print(i, j)
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

The values are not skipped.

The inner `pass` simply does nothing.

---

# 26. `pass` and Indentation

Because Python uses indentation, `pass` is often useful when a block needs a statement.

Correct:

```python
if True:
    pass
```

Incorrect:

```python
if True:
pass
```

The second example does not provide an indented statement for the `if` block.

---

# 27. `pass` Is a Real Python Statement

`pass` is not a comment.

Compare:

```python
# do something later
```

and:

```python
pass
```

A comment is ignored by Python.

`pass` is actually a Python statement that executes and intentionally performs no operation.

---

# 28. `pass` vs Comment

A comment:

```python
# This code will be added later
```

is useful for explaining something to a human.

`pass`:

```python
pass
```

is useful when Python needs an actual statement.

For example:

```python
if number > 10:
    pass
```

This creates a valid empty block.

A comment alone may not provide the required statement.

---

# 29. Basic Use Case: Planning Code

Suppose you are designing a program and have not decided what should happen for certain conditions.

You can temporarily write:

```python
if number > 100:
    pass
elif number > 50:
    print("Medium")
else:
    print("Small")
```

This allows you to keep working on the rest of the program.

Later, you can replace `pass` with the required code.

---

# 30. Basic Use Case: Testing Structure

Sometimes you first want to check whether your conditions and indentation are correct.

Example:

```python
number = 25

if number > 50:
    pass
elif number > 20:
    print("Between 21 and 50")
else:
    print("20 or below")
```

Output:

```text
Between 21 and 50
```

The first branch intentionally has no action.

---

# 31. Basic Use Case: Temporarily Ignoring a Case

Suppose:

```python
number = 10

if number == 10:
    pass
else:
    print("Different number")
```

For now, the `10` case has no action.

This can be useful while developing the program.

---

# 32. Replacing `pass` Later

Start with:

```python
if number > 0:
    pass
```

Later:

```python
if number > 0:
    print("Positive")
```

The `pass` is normally removed when actual behavior is added.

---

# 33. What `pass` Does Not Do

`pass` does **not**:

- stop a loop
- skip an iteration
- change a variable
- print anything
- return a value
- change a condition
- move to the next iteration by itself
- terminate the program

It simply does nothing.

---

# 34. `pass` vs `continue` vs `break`

| Statement | What it does |
|---|---|
| `pass` | Does nothing |
| `continue` | Skips the current iteration |
| `break` | Stops the loop |

Example:

```python
for i in range(1, 6):

    if i == 3:
        pass

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

With `continue`:

```text
1
2
4
5
```

With `break`:

```text
1
2
```

---

# 35. Easy Memory Trick

Remember:

```text
pass     → "Do nothing."
continue → "Skip this iteration."
break    → "Stop the loop."
```

This simple distinction is extremely important.

---

# 36. Common Beginner Mistake: Thinking `pass` Skips Code

Wrong:

> `pass` means skip this iteration.

Correct:

> `continue` skips the current iteration.

`pass` only does nothing at the location where it appears.

---

# 37. Common Beginner Mistake: Expecting Output

Consider:

```python
if True:
    pass
```

There is no output.

Why?

Because `pass` does not display anything.

It simply allows the block to contain a valid statement.

---

# 38. Common Beginner Mistake: Expecting `pass` to Change a Variable

Consider:

```python
x = 10

pass

print(x)
```

Output:

```text
10
```

`pass` does not change `x`.

---

# 39. Common Beginner Mistake: Infinite `while` Loop

Problem:

```python
i = 1

while i <= 5:
    pass
```

This does not automatically increase `i`.

Therefore, the condition remains true.

To make progress:

```python
i = 1

while i <= 5:

    pass
    i = i + 1
```

---

# 40. Common Beginner Mistake: Using `pass` Instead of `continue`

Suppose the requirement is:

> Skip `5`.

This is incorrect:

```python
for i in range(1, 11):

    if i == 5:
        pass

    print(i)
```

It prints `5`.

Correct:

```python
for i in range(1, 11):

    if i == 5:
        continue

    print(i)
```

---

# 41. Common Beginner Mistake: Using `break` Instead of `pass`

Suppose the requirement is:

> Do nothing when the value is `5`, but keep the loop running.

Do not use:

```python
if i == 5:
    break
```

because that stops the loop.

Use:

```python
if i == 5:
    pass
```

if you truly want no action for that condition.

---

# 42. Reading a `pass` Program

Consider:

```python
for i in range(1, 6):

    if i == 3:
        pass

    print(i * 2)
```

Dry run:

```text
i = 1 → pass condition false → print 2
i = 2 → pass condition false → print 4
i = 3 → pass executes → print 6
i = 4 → condition false → print 8
i = 5 → condition false → print 10
```

Output:

```text
2
4
6
8
10
```

---

# 43. Another Dry Run

Consider:

```python
for i in range(1, 5):

    if i == 2:
        pass
        print("Special")

    print(i)
```

When `i == 2`, both:

```python
pass
```

and:

```python
print("Special")
```

are reached.

Output:

```text
1
Special
2
3
4
```

This shows again that `pass` does not skip the next statement.

---

# 44. A Useful Way to Think About `pass`

Think of:

```python
pass
```

as an empty action.

For example:

```text
Condition is true
       ↓
    pass
       ↓
Nothing happens here
       ↓
Continue normal execution
```

It does not control the loop like `break` or `continue`.

---

# 45. When Should You Use `pass`?

Use `pass` when:

- A block must contain a statement.
- You intentionally want the block to do nothing.
- You are creating a placeholder.
- You are writing the structure of a program before implementing every part.
- You want to temporarily leave a case without an action.
- You need an empty block while developing code.

---

# 46. When Should You NOT Use `pass`?

Do not use `pass` when your actual intention is:

### Skip the current loop iteration

Use:

```python
continue
```

### Stop the loop

Use:

```python
break
```

### Explain something to the programmer

Use a comment:

```python
# explanation
```

### Perform an actual action

Write the required statement instead of leaving `pass`.

---

# 47. Important Execution Rule

When Python reaches:

```python
pass
```

inside a block:

1. Python executes `pass`.
2. Nothing happens.
3. Python continues with the next statement normally.

For example:

```python
print("A")

pass

print("B")
```

Output:

```text
A
B
```

---

# 48. `pass` in a Loop: Complete Example

```python
for i in range(1, 6):

    if i == 3:
        pass

    print("Value:", i)
```

Output:

```text
Value: 1
Value: 2
Value: 3
Value: 4
Value: 5
```

The loop is not interrupted.

The value is not skipped.

The loop completes normally.

---

# 49. `pass` in a `while`: Complete Example

```python
i = 1

while i <= 5:

    if i == 3:
        pass

    print(i)
    i = i + 1
```

Output:

```text
1
2
3
4
5
```

Again, `pass` has no effect on the loop's progression.

---

# 50. Final Comparison Example

Consider the same loop with three different statements.

### `pass`

```python
for i in range(1, 6):

    if i == 3:
        pass

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

### `continue`

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

### Final Memory Table

| Statement | Current iteration | Remaining iterations | Loop |
|---|---|---|---|
| `pass` | Continues normally | Continue | Keeps running |
| `continue` | Skipped from that point | Continue | Keeps running |
| `break` | Stops | Do not run | Ends |

---

# Key Takeaways

1. `pass` is a Python statement.
2. `pass` intentionally does nothing.
3. It is useful for empty blocks.
4. It is commonly used as a placeholder.
5. `pass` does not skip a loop iteration.
6. `pass` does not stop a loop.
7. `pass` does not change variables.
8. `pass` does not print anything.
9. `pass` can be used inside `if`.
10. `pass` can be used inside `for`.
11. `pass` can be used inside `while`.
12. In a `while` loop, `pass` does not update the loop-control variable.
13. An empty `while` loop with only `pass` can become infinite.
14. `continue` skips the current iteration.
15. `break` stops the loop.
16. A comment explains something but does not replace a required block statement.
17. `pass` is useful while planning or developing code.
18. The code after `pass` normally executes.
19. The main idea is: **`pass` = do nothing for now.**

---

# Practice Problems

> **Important:** Solve these using only concepts already covered: variables, arithmetic, comparisons, logical operators, `if` / `else`, `for`, `while`, `range()`, strings, `break`, `continue`, and `pass`.

## A. Basic Understanding

### 1.
Write a program containing an `if` block that uses `pass`.

### 2.
Write a program where an `else` block contains `pass`.

### 3.
Predict the output:

```python
if True:
    pass

print("Hello")
```

### 4.
Predict the output:

```python
x = 10

if x > 5:
    pass

print(x)
```

### 5.
Does `pass` print anything? Explain with an example.

### 6.
Does `pass` stop a program? Explain with an example.

### 7.
Does `pass` change a variable? Explain with an example.

### 8.
Write an empty `if` block correctly using `pass`.

### 9.
Explain why an empty block cannot simply be left without a statement.

### 10.
Write a program that contains two separate `if` blocks, both temporarily using `pass`.

---

## B. `pass` with `if` / `else`

### 11.
Write a program that checks whether a number is positive. If it is positive, use `pass`; otherwise print `"Not positive"`.

### 12.
Write a program that checks whether a number is even. Use `pass` for the even case and print `"Odd"` for the other case.

### 13.
Write a program that uses `pass` in the `else` branch.

### 14.
Predict the output:

```python
number = 10

if number == 10:
    pass
else:
    print("Different")
```

### 15.
Predict the output:

```python
number = 5

if number > 10:
    print("Large")
else:
    pass

print("Done")
```

### 16.
Write a program where a number greater than `100` does nothing, while other numbers are printed.

### 17.
Write a program where a number equal to `0` does nothing, while other numbers are printed.

### 18.
Write an `if-elif-else` structure where one branch contains `pass`.

### 19.
Explain what happens when Python enters a branch containing only `pass`.

### 20.
Replace the `pass` in a simple condition with a meaningful `print()` statement.

---

## C. `pass` with `for`

### 21.
Write a `for` loop from `1` to `10` containing only `pass`.

### 22.
Predict the output:

```python
for i in range(1, 6):
    pass

print("Finished")
```

### 23.
Write a loop where `pass` executes only when `i == 5`.

### 24.
Predict the output:

```python
for i in range(1, 6):

    if i == 3:
        pass

    print(i)
```

### 25.
Explain why `3` is printed in Problem 24.

### 26.
Write a loop where `pass` is used for even numbers and odd numbers are printed.

### 27.
Write a loop where `pass` is used for odd numbers and even numbers are printed.

### 28.
Write a loop from `1` to `20` where multiples of `5` use `pass`.

### 29.
Predict the output:

```python
for i in range(1, 5):

    if i == 2:
        pass
        print("Special")

    print(i)
```

### 30.
Explain why `"Special"` is printed when `i == 2`.

---

## D. `pass` with `while`

### 31.
Write a `while` loop from `1` to `5` containing `pass`.

### 32.
Predict whether this program terminates:

```python
i = 1

while i <= 5:
    pass
```

Explain your answer.

### 33.
Correct Problem 32 so that the loop terminates.

### 34.
Write a `while` loop that uses `pass` when `i == 3`.

### 35.
Write a `while` loop that uses `pass` for even values.

### 36.
Write a `while` loop that uses `pass` for odd values.

### 37.
Explain why `pass` does not update the loop-control variable.

### 38.
Predict the output:

```python
i = 1

while i <= 5:

    if i == 3:
        pass

    print(i)
    i = i + 1
```

### 39.
Explain how Problem 38 is different from a `while` loop containing only `pass`.

### 40.
Write a `while` loop that contains `pass` but still safely reaches its stopping condition.

---

## E. `pass` vs `continue`

### 41.
Predict the output:

```python
for i in range(1, 6):

    if i == 3:
        pass

    print(i)
```

### 42.
Predict the output:

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

### 43.
Explain the difference between the outputs of Problems 41 and 42.

### 44.
Write a program using `pass` where the number `5` is still printed.

### 45.
Write a program using `continue` where the number `5` is skipped.

### 46.
Replace `pass` with `continue` in a given loop and explain the output change.

### 47.
Write an example where using `pass` would be wrong because the requirement is to skip an iteration.

### 48.
Write an example where `pass` is appropriate because no action is required.

---

## F. `pass` vs `break`

### 49.
Predict the output:

```python
for i in range(1, 6):

    if i == 3:
        pass

    print(i)
```

### 50.
Predict the output:

```python
for i in range(1, 6):

    if i == 3:
        break

    print(i)
```

### 51.
Explain why the first program prints `3` but the second does not.

### 52.
Write a program where `5` causes no action but the loop continues.

### 53.
Write a program where `5` causes the loop to stop completely.

### 54.
Explain in one sentence the difference between `pass` and `break`.

---

## G. Placeholder Problems

### 55.
Create an `if` block for positive numbers but use `pass` because the actual action will be added later.

### 56.
Create an `if-else` structure where one branch is intentionally left without an action using `pass`.

### 57.
Create a loop structure where a special case is temporarily left unfinished using `pass`.

### 58.
Write a small program containing three conditions, where one condition uses `pass` as a placeholder.

### 59.
Take a number from the user and create a condition for numbers greater than `50`. Use `pass` for now.

### 60.
Take a number from the user and use `pass` when the number is `0`.

---

## H. Debugging Problems

### 61.
Find the problem:

```python
if True:
```

How can `pass` make the block valid?

### 62.
Find the problem:

```python
if True:
    pass
    print("Hello")
```

Does the `print()` statement execute? Explain.

### 63.
Find the problem:

```python
for i in range(1, 6):

    if i == 3:
        pass

    print(i)
```

Does this skip `3`? If not, what should be used to skip it?

### 64.
Find the problem:

```python
i = 1

while i <= 5:
    pass
```

Why does the loop not finish?

### 65.
Correct Problem 64.

### 66.
A student says:

> "`pass` and `continue` are the same."

Give a code example proving that the statement is incorrect.

### 67.
A student says:

> "`pass` stops the loop."

Give a code example proving that the statement is incorrect.

### 68.
A student says:

> "`pass` automatically increases the variable in a `while` loop."

Give a code example proving that the statement is incorrect.

### 69.
Find which statement should be used:

> "Do nothing here, but continue normal execution."

### 70.
Find which statement should be used:

> "Skip this iteration."

### 71.
Find which statement should be used:

> "Stop the loop completely."

---

## I. Nested Blocks and Loops

### 72.
Write nested `if` statements where the inner block contains `pass`.

### 73.
Write nested loops where the inner loop contains `pass`.

### 74.
Predict the output:

```python
for i in range(2):

    for j in range(3):

        if j == 1:
            pass

        print(i, j)
```

### 75.
Explain why `j == 1` is still printed in Problem 74.

### 76.
Write nested loops where `pass` is used for a selected inner-loop value.

### 77.
Rewrite the previous problem using `continue` and explain the difference.

---

## J. Final Practice

### 78.
Write a program that checks numbers from `1` to `20`. For multiples of `5`, do nothing using `pass`. Print all numbers.

### 79.
Write a program that checks numbers from `1` to `20`. Skip multiples of `5` using `continue`.

### 80.
Write a program that checks numbers from `1` to `20`. Stop at the first multiple of `5` using `break`.

### 81.
Compare the outputs of Problems 78, 79, and 80.

### 82.
Write a program using `pass` as a temporary placeholder, then replace it with actual code.

### 83.
Write a program where `pass` is used in an `else` branch.

### 84.
Write a program where `pass` is used inside a nested condition.

### 85.
Write a program where `pass` is used inside a `for` loop and the loop still completes normally.

### 86.
Write a program where `pass` is used inside a `while` loop and the loop still terminates correctly.

### 87.
Write one example each for:

```text
pass
continue
break
```

and explain the purpose of each.

### 88.
Write a short program that demonstrates why `pass` is useful as a placeholder.

---

# Final Challenge 1: Three Different Behaviors

Write three versions of a loop from `1` to `10`.

### Version 1

When `i == 5`, use `pass`.

### Version 2

When `i == 5`, use `continue`.

### Version 3

When `i == 5`, use `break`.

Then write the output of all three programs.

---

# Final Challenge 2: Empty Conditions

Create a program that checks a number.

Rules:

- If the number is greater than `100`, temporarily do nothing.
- If the number is between `50` and `100`, print `"Medium"`.
- Otherwise, print `"Small"`.

Use `pass` for the first condition.

---

# Final Challenge 3: Safe `while` Loop

Write a `while` loop from `1` to `10`.

Rules:

- When `i == 5`, use `pass`.
- Continue counting normally.
- Make sure the loop terminates.

Then explain why `pass` does not interfere with the loop's progress.

---

# Final Challenge 4: Choose the Correct Statement

For each situation, choose `pass`, `continue`, or `break`.

### A.
"I don't want to perform any action here, but normal execution should continue."

### B.
"I don't want to execute the remaining statements for this iteration."

### C.
"I want to stop the loop completely."

### D.
"I have not written the actual code for this block yet."

Explain each answer.

---

# Final Revision

Before moving to the next topic, make sure you understand this program:

```python
for i in range(1, 6):

    if i == 3:
        pass

    print(i)
```

You should be able to answer:

1. What does `pass` do?
2. Is `3` printed?
3. Does the loop stop?
4. Does the loop skip `3`?
5. What happens after `pass`?
6. What would happen if `pass` were replaced by `continue`?
7. What would happen if `pass` were replaced by `break`?

Also understand:

```python
i = 1

while i <= 5:

    pass

    i = i + 1
```

The key idea is:

> **`pass` is used when Python needs a statement, but we intentionally want no action at that point.**

And remember:

```text
pass     → do nothing
continue → skip the current iteration
break    → stop the loop
```