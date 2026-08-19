# 2.11 While Loops

## Objective

After completing this topic, you should be able to understand and use:

- Need for `while`
- Loop conditions
- Counter-controlled loops
- Input-controlled loops
- Infinite loops
- Nested `while` loops

> **Prerequisite:** You should understand variables, data types, arithmetic operators, comparison operators, logical operators, input/output, conditional statements, `for` loops, `range()`, strings, and basic number-based problem solving.

---

# 1. What Is a `while` Loop?

A `while` loop is used when we want to **repeat a block of code as long as a condition is `True`**.

Basic syntax:

```python
while condition:
    statement
```

The basic flow is:

```text
Check condition
      ↓
   True?
   /   \
 Yes    No
  ↓      ↓
Run     Stop
block
  ↓
Check condition again
```

The condition is checked **before every iteration**.

---

# 2. Why Do We Need `while`?

Suppose we want to print numbers from `1` to `5`.

Without a loop:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

This works, but it is repetitive.

We can use a loop:

```python
i = 1

while i <= 5:
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

The loop allows Python to repeat the same instructions.

---

# 3. When Is a `while` Loop Useful?

A `while` loop is especially useful when we do not know exactly how many times the loop should run in advance.

For example:

- Keep asking for a password until it is correct.
- Keep asking for a number until the user enters `0`.
- Continue processing digits until no digits remain.
- Repeat an operation while a condition remains true.
- Keep taking values until a special value is entered.

The important idea is:

> **A `while` loop is controlled by a condition.**

---

# 4. Basic `while` Loop Example

```python
i = 1

while i <= 5:
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

Let's understand each part.

```python
i = 1
```

This gives the variable its starting value.

```python
while i <= 5:
```

This asks:

> Is `i` less than or equal to `5`?

If the answer is `True`, the loop body runs.

```python
print(i)
```

prints the current value.

```python
i = i + 1
```

changes the value so that the loop can eventually stop.

---

# 5. Condition Checking

Consider:

```python
i = 1

while i <= 3:
    print(i)
    i = i + 1
```

### First check

```text
i = 1
1 <= 3 → True
```

Run the loop.

```text
Print 1
i becomes 2
```

### Second check

```text
2 <= 3 → True
```

Run the loop.

```text
Print 2
i becomes 3
```

### Third check

```text
3 <= 3 → True
```

Run the loop.

```text
Print 3
i becomes 4
```

### Fourth check

```text
4 <= 3 → False
```

The loop stops.

---

# 6. The Three Important Parts of a `while` Loop

Most simple `while` loops have three important parts:

```text
1. Initialization
2. Condition
3. Update
```

Example:

```python
i = 1              # Initialization

while i <= 5:      # Condition
    print(i)
    i = i + 1      # Update
```

### Initialization

Sets the starting value:

```python
i = 1
```

### Condition

Controls whether the loop continues:

```python
i <= 5
```

### Update

Changes the controlling variable:

```python
i = i + 1
```

Remember this pattern:

```text
Start → Check → Execute → Update → Check again
```

---

# 7. Counter-Controlled Loops

A **counter-controlled loop** is a loop where a variable acts as a counter.

For example:

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

Here:

```text
count = 1
```

is the starting value.

The condition:

```python
count <= 5
```

determines when to stop.

The update:

```python
count = count + 1
```

moves the counter forward.

---

# 8. Counter Increasing by 1

The most common pattern is:

```python
count = 1

while count <= 10:
    print(count)
    count = count + 1
```

Output:

```text
1
2
3
4
5
6
7
8
9
10
```

---

# 9. Counter Increasing by 2

The counter does not have to increase by `1`.

Example:

```python
count = 2

while count <= 10:
    print(count)
    count = count + 2
```

Output:

```text
2
4
6
8
10
```

This is useful for generating even numbers.

---

# 10. Counter Decreasing

A counter can also decrease.

Example:

```python
count = 5

while count >= 1:
    print(count)
    count = count - 1
```

Output:

```text
5
4
3
2
1
```

Notice the condition and update work together:

```python
count >= 1
```

and:

```python
count = count - 1
```

---

# 11. Important Relationship Between Condition and Update

The update should move the variable toward the point where the condition becomes false.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

The condition wants:

```text
count > 5
```

to eventually become true.

The update:

```text
1 → 2 → 3 → 4 → 5 → 6
```

moves in that direction.

This is an important rule:

> **Always make sure the loop's update can eventually make the condition false.**

---

# 12. Input-Controlled Loops

Sometimes we do not know beforehand how many times the user will provide input.

For example:

> Keep asking the user for a number until the user enters `0`.

This is called an **input-controlled loop**.

The input controls when the loop stops.

---

# 13. Sentinel Value

A special value used to stop an input-controlled loop is often called a **sentinel value**.

For example:

```text
0
```

can be the sentinel value.

The idea is:

```text
Enter number
     ↓
Is it 0?
 /      \
Yes      No
 ↓        ↓
Stop     Process
          ↓
       Ask again
```

---

# 14. Basic Input-Controlled Example

```python
number = int(input("Enter a number: "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter a number: "))

print("Loop ended")
```

Suppose the user enters:

```text
5
8
3
0
```

The program processes:

```text
5
8
3
```

When the user enters:

```text
0
```

the condition:

```python
number != 0
```

becomes false.

The loop stops.

---

# 15. Why Is the Input Written Twice?

You may notice:

```python
number = int(input("Enter a number: "))
```

before the loop and again inside the loop.

This is because the program needs a value **before it can check the condition**.

Then, after processing the current value, it needs to get the next value.

The pattern is:

```text
Get input
   ↓
Check condition
   ↓
Process input
   ↓
Get next input
   ↓
Check again
```

---

# 16. Input-Controlled Sum

Suppose we want to keep taking numbers and calculate their sum until the user enters `0`.

```python
number = int(input("Enter a number: "))

total = 0

while number != 0:
    total = total + number
    number = int(input("Enter a number: "))

print("Sum:", total)
```

Input:

```text
10
20
5
0
```

Output:

```text
Sum: 35
```

The `0` is used only to stop the loop. It is not added to the total.

---

# 17. Input-Controlled Count

We can also count how many numbers were entered before `0`.

```python
number = int(input("Enter a number: "))

count = 0

while number != 0:
    count = count + 1
    number = int(input("Enter a number: "))

print("Numbers entered:", count)
```

For input:

```text
7
9
4
2
0
```

Output:

```text
Numbers entered: 4
```

---

# 18. Positive Number Input

Suppose we want the user to enter a positive number.

We can keep asking until the number is positive.

```python
number = int(input("Enter a positive number: "))

while number <= 0:
    print("Invalid input")
    number = int(input("Enter a positive number: "))

print("Accepted:", number)
```

If the user enters:

```text
-5
```

the condition is true, so the program asks again.

If the user eventually enters:

```text
10
```

the condition becomes false and the loop ends.

---

# 19. Input Validation

The previous example demonstrates **input validation**.

Input validation means checking whether the user's input satisfies a required condition.

Example:

```python
age = int(input("Enter age: "))

while age < 0:
    print("Age cannot be negative.")
    age = int(input("Enter age: "))

print("Accepted age:", age)
```

The loop continues until a valid value is entered.

---

# 20. `while` Loop and Number Processing

The `while` loop is very useful for processing the digits of a number.

For example:

```python
number = 472

while number > 0:
    digit = number % 10
    print(digit)
    number = number // 10
```

Output:

```text
2
7
4
```

The loop continues while:

```python
number > 0
```

Each iteration:

1. Extracts the last digit.
2. Processes the digit.
3. Removes the last digit.

---

# 21. Sum of Digits Using `while`

```python
number = int(input("Enter a number: "))

total = 0

while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("Sum:", total)
```

For:

```text
472
```

the result is:

```text
13
```

This is an example of a **data-controlled loop**: the changing number determines when the loop ends.

---

# 22. Reverse a Number Using `while`

```python
number = int(input("Enter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse:", reverse)
```

For:

```text
1234
```

output:

```text
4321
```

---

# 23. Infinite Loops

An **infinite loop** is a loop that never stops because its condition never becomes false.

Example:

```python
i = 1

while i <= 5:
    print(i)
```

This is a problem.

Why?

Because `i` never changes.

The value remains:

```text
1
```

So:

```text
1 <= 5
```

always remains true.

---

# 24. Correcting the Infinite Loop

Add an update:

```python
i = 1

while i <= 5:
    print(i)
    i = i + 1
```

Now:

```text
1 → 2 → 3 → 4 → 5 → 6
```

When:

```text
6 <= 5
```

is false, the loop stops.

---

# 25. Another Infinite Loop Example

Consider:

```python
i = 10

while i > 0:
    print(i)
    i = i + 1
```

This is also an infinite loop.

The condition requires:

```text
i <= 0
```

eventually.

But the update does:

```text
10 → 11 → 12 → 13 → ...
```

The value moves in the wrong direction.

The correct version is:

```python
i = 10

while i > 0:
    print(i)
    i = i - 1
```

---

# 26. How to Identify an Infinite Loop

Before running a `while` loop, ask:

### Question 1

What is the initial value?

### Question 2

What is the condition?

### Question 3

Which variable controls the condition?

### Question 4

Does that variable change inside the loop?

### Question 5

Does it move toward making the condition false?

For example:

```python
i = 1

while i <= 10:
    print(i)
    i = i + 1
```

Analysis:

```text
Start: 1
Condition: i <= 10
Update: i + 1
Direction: upward
Stop point: i becomes 11
```

So it terminates.

---

# 27. Common Causes of Infinite Loops

## Cause 1: No update

```python
i = 1

while i <= 5:
    print(i)
```

---

## Cause 2: Wrong update direction

```python
i = 10

while i > 0:
    print(i)
    i = i + 1
```

---

## Cause 3: Updating the wrong variable

```python
i = 1
j = 0

while i <= 5:
    print(i)
    j = j + 1
```

The condition depends on `i`, but only `j` changes.

---

## Cause 4: Condition that is always true

```python
while True:
    print("Hello")
```

This deliberately creates an infinite loop.

In beginner programs, avoid such loops unless you have a clear reason and a safe stopping mechanism.

---

# 28. Nested `while` Loops

A **nested `while` loop** means a `while` loop inside another `while` loop.

Example:

```python
row = 1

while row <= 3:
    column = 1

    while column <= 4:
        print("*", end="")
        column = column + 1

    print()
    row = row + 1
```

Output:

```text
****
****
****
```

---

# 29. Understanding the Nested Loop

There are two counters:

```text
row
column
```

The outer loop controls:

```text
rows
```

The inner loop controls:

```text
columns
```

For every value of `row`, the complete inner loop runs.

---

# 30. Nested `while` Dry Run

Consider:

```python
row = 1

while row <= 2:
    column = 1

    while column <= 3:
        print("*", end="")
        column = column + 1

    print()
    row = row + 1
```

### First outer iteration

```text
row = 1
```

Set:

```text
column = 1
```

Inner loop:

```text
column = 1 → *
column = 2 → *
column = 3 → *
```

Then:

```text
***
```

Move to next row.

### Second outer iteration

```text
row = 2
```

Again:

```text
column = 1 → *
column = 2 → *
column = 3 → *
```

Final output:

```text
***
***
```

---

# 31. Important Rule for Nested `while`

The inner loop must normally have its own initialization and update.

Correct:

```python
row = 1

while row <= 3:
    column = 1

    while column <= 4:
        print("*", end="")
        column = column + 1

    print()
    row = row + 1
```

Notice:

```python
column = 1
```

is inside the outer loop.

Why?

Because we want the inner loop to start from `1` again for every new row.

---

# 32. What Happens If We Put `column = 1` Outside?

Consider:

```python
row = 1
column = 1

while row <= 3:

    while column <= 4:
        print("*", end="")
        column = column + 1

    print()
    row = row + 1
```

After the first inner loop:

```text
column = 5
```

For the next outer iteration:

```text
column <= 4
```

is already false.

So the inner loop does not run again.

This is a common nested-loop mistake.

---

# 33. Nested `while` for Number Patterns

We can print:

```text
1
12
123
1234
```

using nested `while` loops.

```python
row = 1

while row <= 4:
    column = 1

    while column <= row:
        print(column, end="")
        column = column + 1

    print()
    row = row + 1
```

Output:

```text
1
12
123
1234
```

The important relationship is:

```python
column <= row
```

The number of columns depends on the current row.

---

# 34. `while` Loop with `if`

A condition can be used inside a loop.

Example:

```python
i = 1

while i <= 10:
    if i % 2 == 0:
        print(i)

    i = i + 1
```

Output:

```text
2
4
6
8
10
```

The loop visits all numbers from `1` to `10`, while the `if` statement selects only even numbers.

---

# 35. Counter-Controlled vs Input-Controlled

These are two important forms of `while` loops.

| Counter-Controlled | Input-Controlled |
|---|---|
| A counter controls the loop | User input controls the loop |
| Usually has a known stopping range | Number of iterations may not be known |
| Example: print `1` to `10` | Example: keep reading until `0` |
| Uses initialization, condition, update | Uses input, condition, and new input |

### Counter-controlled example

```python
i = 1

while i <= 10:
    print(i)
    i = i + 1
```

### Input-controlled example

```python
number = int(input("Enter number: "))

while number != 0:
    print(number)
    number = int(input("Enter number: "))
```

---

# 36. `for` vs `while`

| `for` | `while` |
|---|---|
| Good for known sequences/ranges | Good for condition-controlled repetition |
| Commonly used with `range()` | Uses a Boolean condition |
| Loop variable changes automatically | Programmer usually controls the update |
| Convenient for strings | Useful for repeated input |
| Convenient for known iteration counts | Useful when stopping depends on changing input/data |

Example:

```python
for i in range(1, 6):
    print(i)
```

Equivalent basic `while` version:

```python
i = 1

while i <= 5:
    print(i)
    i = i + 1
```

---

# 37. Common Beginner Mistakes

## Mistake 1: Forgetting the Update

Wrong:

```python
i = 1

while i <= 5:
    print(i)
```

Correct:

```python
i = 1

while i <= 5:
    print(i)
    i = i + 1
```

---

## Mistake 2: Updating in the Wrong Direction

Wrong:

```python
i = 10

while i > 0:
    print(i)
    i = i + 1
```

Correct:

```python
i = 10

while i > 0:
    print(i)
    i = i - 1
```

---

## Mistake 3: Using the Wrong Variable

Wrong:

```python
i = 1
j = 0

while i <= 5:
    print(i)
    j = j + 1
```

`i` controls the condition, so `i` must eventually change.

---

## Mistake 4: Forgetting to Take New Input

Wrong:

```python
number = int(input("Enter number: "))

while number != 0:
    print(number)
```

The value never changes.

Correct:

```python
number = int(input("Enter number: "))

while number != 0:
    print(number)
    number = int(input("Enter number: "))
```

---

## Mistake 5: Forgetting the Special Case `0`

If a number-processing loop uses:

```python
while number > 0:
```

remember that input `0` causes the loop to execute zero times.

If your problem requires `0` to be treated as a one-digit number or as a special input, handle it separately.

---

## Mistake 6: Not Resetting the Inner Counter

For nested loops, initialize the inner counter again inside the outer loop.

Correct:

```python
while row <= 3:
    column = 1

    while column <= 4:
        ...
        column = column + 1

    row = row + 1
```

---

# 38. Dry-Run Checklist

Whenever you see a `while` loop, trace it using these questions:

1. What is the initial value?
2. What is the loop condition?
3. Is the condition `True` or `False`?
4. What statements execute?
5. Which variable changes?
6. What is its new value?
7. What is the condition now?
8. When will the condition become `False`?

For example:

```python
i = 2

while i <= 8:
    print(i)
    i = i + 2
```

Dry run:

```text
i = 2  → True  → print 2 → i = 4
i = 4  → True  → print 4 → i = 6
i = 6  → True  → print 6 → i = 8
i = 8  → True  → print 8 → i = 10
i = 10 → False → stop
```

---

# 39. Important `while` Loop Patterns

### Count upward

```python
i = 1

while i <= n:
    print(i)
    i = i + 1
```

### Count downward

```python
i = n

while i >= 1:
    print(i)
    i = i - 1
```

### Even numbers

```python
i = 2

while i <= n:
    print(i)
    i = i + 2
```

### Process digits

```python
while number > 0:
    digit = number % 10
    # process digit
    number = number // 10
```

### Input until sentinel

```python
number = int(input("Enter number: "))

while number != 0:
    # process number
    number = int(input("Enter number: "))
```

### Nested loop

```python
row = 1

while row <= rows:
    column = 1

    while column <= columns:
        # process
        column = column + 1

    row = row + 1
```

---

# 40. Key Points to Remember

1. A `while` loop repeats code while a condition is `True`.
2. The condition is checked before every iteration.
3. A simple `while` loop usually has initialization, condition, and update.
4. The update must eventually make the condition false.
5. A counter-controlled loop uses a counter variable.
6. A counter can increase or decrease.
7. An input-controlled loop uses user input to determine when to stop.
8. A sentinel value is a special input used to end a loop.
9. `0` is a common sentinel value in simple examples.
10. Input validation can be implemented using a `while` loop.
11. `while` loops are useful for number digit processing.
12. Forgetting to update a controlling variable can create an infinite loop.
13. Updating in the wrong direction can also create an infinite loop.
14. The variable controlling the condition must actually change.
15. Nested `while` loops contain one `while` loop inside another.
16. The inner loop should usually reset its counter for every outer iteration.
17. Nested loops are useful for rows, columns, and patterns.
18. `while` is often preferred when the number of iterations depends on a condition or input.
19. `for` is often more convenient for known ranges or sequences.
20. Always dry-run a `while` loop when you are unsure how it will execute.

---

# Practice Problems

> **Note:** These problems use only concepts covered in the current and previous topics. Do not use lists, tuples, dictionaries, functions, recursion, comprehensions, classes, or exception handling.

## A. Basic `while` Loop

### 1.
Print the numbers from `1` to `10` using a `while` loop.

### 2.
Print the numbers from `10` to `1` in reverse order.

### 3.
Print all even numbers from `2` to `20`.

### 4.
Print all odd numbers from `1` to `19`.

### 5.
Print multiples of `5` from `5` to `50`.

### 6.
Take `n` from the user and print numbers from `1` to `n`.

### 7.
Take `n` from the user and print numbers from `n` down to `1`.

### 8.
Take `n` from the user and print all even numbers from `1` to `n`.

### 9.
Take `n` from the user and print all odd numbers from `1` to `n`.

### 10.
Print the first `n` multiples of a number entered by the user.

---

## B. Counter-Controlled Problems

### 11.
Take `n` from the user and calculate:

```text
1 + 2 + 3 + ... + n
```

### 12.
Calculate the sum of all even numbers from `1` to `n`.

### 13.
Calculate the sum of all odd numbers from `1` to `n`.

### 14.
Calculate:

```text
1 × 2 × 3 × ... × n
```

### 15.
Print the multiplication table of a number from `1` to `10`.

### 16.
Count how many numbers from `1` to `n` are divisible by `3`.

### 17.
Count how many numbers from `1` to `n` are divisible by both `2` and `3`.

### 18.
Find the largest number among the numbers from `1` to `n` that are divisible by `3`.

### 19.
Calculate the sum of numbers from `1` to `n` that are divisible by `5`.

### 20.
Calculate the sum of the squares of numbers from `1` to `n`.

For example, for `n = 3`:

```text
1² + 2² + 3² = 14
```

---

## C. Input-Controlled Loops

### 21.
Keep asking the user for numbers until the user enters `0`.

Print every entered number except `0`.

### 22.
Keep taking numbers until `0` is entered and calculate their sum.

### 23.
Keep taking numbers until `0` is entered and count how many numbers were entered.

### 24.
Keep taking numbers until `0` is entered and count how many were positive.

### 25.
Keep taking numbers until `0` is entered and count how many were negative.

### 26.
Keep taking numbers until `0` is entered and calculate the sum of only the positive numbers.

### 27.
Keep taking numbers until `0` is entered and calculate the sum of only the even numbers.

### 28.
Keep taking numbers until `0` is entered and calculate the sum of only the odd numbers.

### 29.
Keep asking the user for a positive number until a positive number is entered.

### 30.
Keep asking the user to enter a number between `1` and `100` until a valid number is entered.

---

## D. Infinite Loop Understanding

### 31.
Identify why the following loop is infinite:

```python
i = 1

while i <= 10:
    print(i)
```

Write the corrected version.

### 32.
Identify why the following loop is infinite:

```python
i = 10

while i > 0:
    print(i)
    i = i + 1
```

Correct it.

### 33.
Find the problem in:

```python
i = 1
j = 0

while i <= 5:
    print(i)
    j = j + 1
```

Correct the program.

### 34.
Predict whether this loop terminates:

```python
i = 10

while i >= 1:
    print(i)
    i = i - 2
```

If it terminates, write its output.

### 35.
Predict the output:

```python
i = 2

while i <= 10:
    print(i)
    i = i + 3
```

---

## E. Number-Based Problems

### 36.
Take a number and count its digits using a `while` loop.

### 37.
Take a number and calculate the sum of its digits.

### 38.
Take a number and reverse it.

### 39.
Check whether a number is a palindrome.

### 40.
Find the largest digit in a number.

### 41.
Find the smallest digit in a number.

### 42.
Count the number of even digits in a number.

### 43.
Count the number of odd digits in a number.

### 44.
Calculate the product of all digits of a number.

### 45.
Check whether a number is prime using a `while` loop.

---

## F. Factors, GCD, and LCM

### 46.
Print all factors of a number using a `while` loop.

### 47.
Count the number of factors of a number.

### 48.
Check whether a number is prime by counting its factors.

### 49.
Find the GCD/HCF of two numbers using a `while` loop.

### 50.
Find the LCM of two numbers using a `while` loop.

---

## G. Fibonacci Problems

### 51.
Print the first `n` Fibonacci terms.

### 52.
Print the first `10` Fibonacci terms.

### 53.
Calculate the sum of the first `n` Fibonacci terms.

### 54.
Take `n` and print Fibonacci terms until the value becomes greater than `n`.

---

## H. Nested `while` Loops

### 55.
Use nested `while` loops to print:

```text
****
****
****
```

### 56.
Print:

```text
*****
*****
*****
*****
```

### 57.
Print:

```text
*
**
***
****
*****
```

### 58.
Print:

```text
1
12
123
1234
12345
```

### 59.
Print:

```text
12345
1234
123
12
1
```

### 60.
Create a multiplication-table grid using nested `while` loops for numbers `1` to `5`.

---

# Final Challenge 1: Number Analysis

Take a positive integer from the user and use `while` loops to display:

```text
Number of digits
Sum of digits
Reverse
Largest digit
Smallest digit
```

Then check whether it is:

```text
Palindrome
Prime
```

Try to solve each part using a separate logical step.

---

# Final Challenge 2: Input-Controlled Number Analyzer

Keep taking positive numbers from the user until `0` is entered.

At the end, display:

```text
Total numbers entered
Sum of numbers
Count of even numbers
Count of odd numbers
```

Do not count the terminating `0` as an entered data value.

---

# Final Challenge 3: Nested Pattern

Take `n` from the user and print:

```text
1
12
123
1234
...
```

until the last row contains `n` numbers.

For:

```text
n = 5
```

output:

```text
1
12
123
1234
12345
```

### Think Before Coding

Ask:

1. Which `while` controls the rows?
2. Which `while` controls the columns?
3. Where should the inner counter start?
4. When should the inner counter stop?
5. Why must the inner counter be reset for every new row?
6. Where should the outer counter be updated?

If you can answer these questions, you understand the core idea of **nested `while` loops**.

---

# Final Revision

Before moving to the next topic, make sure you can explain this pattern:

```python
i = 1

while i <= n:
    # work
    i = i + 1
```

You should be able to identify:

```text
i = 1
   ↓
Initialization

i <= n
   ↓
Condition

# work
   ↓
Loop body

i = i + 1
   ↓
Update
```

And for an input-controlled loop:

```python
value = int(input("Enter value: "))

while value != 0:
    # process value
    value = int(input("Enter value: "))
```

You should understand:

```text
Input → Check → Process → Input again → Check → ...
```

Finally, remember:

> **A `while` loop is not difficult because of its syntax. The important part is designing the correct condition, deciding what changes inside the loop, and knowing why the loop will eventually stop.**