# Session 2: Python Basics II

You have learned some of the basics of Python in the first session:
- Variables
- Data types
- Operators
- Lists/Tuples
- Dictionaries

In this session you will learn more about Python and its possibilities. You will learn about:
- **Flow Control**: If-Elif-Else Statements, While Loops, For Loops
- **Strings**: How to work with strings in Python
- **Working with files**: How to read from and write to files
- **Functions**: How to define and use functions
- **Classes and Objects**: How to define and use classes and objects

These topics are very important to structure your code and to make it more readable and reusable. You can find this concepts in nearly every programming language, so take your time to understand them.

## Flow Control

Flow control statements are used to control the flow of execution in a program. At many points in your program, you may want to make a decision about which block of code to execute next. You can do this with flow control statements. For this you need comparison operators and especially boolean values.

### Comparison Operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal                    |
| !=       | Not equal                |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or equal to |
| <=       | Less than or equal to    |

### Boolean operators

| Operator | Meaning                   |
| -------- | ------------------------  |
| and      | Logical and               |
| or       | Logical or                |
| not      | Logical not               |

**The and operator's truth table:**

| Expression | Evaluates to |
| ---------- | ------------ |
| True and True | True |
| True and False | False |
| False and True | False |
| False and False | False |

**The or operator's truth table:**

| Expression | Evaluates to |
| ---------- | ------------ |
| True or True | True |
| True or False | True |
| False or True | True |
| False or False | False |

**The not operator's truth table:**

| Expression | Evaluates to |
| ---------- | ------------ |
| not True | False |
| not False | True |



### If-Elif-Else Statements
**if-statement**: The `if` statement is used to check a condition. If the condition is true, a block of code will be executed. If the condition is false, the block of code will be skipped.

```python
if 5 > 2:
  print("Five is greater than two!")
```

**else-statement**: The `else` statement is used to execute a block of code if the condition is false.

```python
if 5 < 2:
  print("Five is less than two!")
else:
  print("Five is not less than two!")
```

**elif-statement**: The `elif` statement is used to check multiple conditions. If the condition is true, the block of code will be executed. If the condition is false, the next condition will be checked.

```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```

### While Loops
A `while` loop is used to execute a block of code as long as a condition is true.

```python
i = 1
while i < 6:
  print(i)
  i += 1
```

### For Loops
A `for` loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).

```python
for i in range(6): 
  print(i)

# range() is a built-in function that returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
```

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(x)
```

## Strings

Strings are sequences of characters. You can use strings to represent text data. Strings in Python are surrounded by either single quotation marks, or double quotation marks.

```python
# Single quotation marks
print('Hello')

# Double quotation marks
print("Hello")
```

You have many possibilities to work with strings. You can add, remove, or change elements. 

```python
# String
a = "Hello, World!"

# Get the character at position 1
print(a[1]) # Output: e

# Substring. Get the characters from position 2 to position 5 (not included)
print(a[2:5]) # Output: llo

# The strip() method removes any whitespace from the beginning or the end
b = " Hello, World! "
print(b.strip()) # Output: Hello, World!
print(b.lstrip()) # Output: Hello, World!
print(b.rstrip()) # Output:  Hello, World!

# The lower() method returns the string in lower case
print(a.lower()) # Output: hello, world!

# The upper() method returns the string in upper case
print(a.upper()) # Output: HELLO, WORLD!

# The replace() method replaces a string with another string
print(a.replace("H", "J")) # Output: Jello, World!

# The split() method splits the string into substrings if it finds instances of the separator
print(a.split(",")) # Output: ['Hello', ' World!']

# The len() method returns the length of a string
print(len(a)) # Output: 13

# The in operator checks if a substring is present in a string
print("Hello" in a) # Output: True

# The not in operator checks if a substring is not present in a string
print("Hello" not in a) # Output: False

# You can use the + operator to concatenate two strings
a = "Hello"
b = "World"
c = a + b
print(c) # Output: HelloWorld

# You can also use the string interpolation to concatenate two strings
c = "%s to the %s" % (a, b) 
print(c) # Output: Hello to the World

# You can also use f-strings to concatenate two strings. This is the most modern way to do it.
c = f"{a} to the {b}"
print(c) # Output: Hello to the World

# If you have a list of strings, you can concatenate them with the join() method
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits)) # Output: apple, banana, cherry

# To escape a character, you can use the backslash
print("We are the so-called \"Vikings\" from the north.") # Output: We are the so-called "Vikings" from the north.

```
## Working with files

In Python, you can easily work with text files to read from or write to them.

### The `with` Statement

The `with` statement in Python is used to open files safely and automatically handle closing them, even if an error occurs. This helps avoid leaving files open, which can cause issues, especially with large numbers of files. 

```python
# Open a file for reading
with open("example.txt", "r") as file:
    content = file.read() # Reads the entire file content
```

In this example:
- `open("example.txt", "r")` opens the file in read mode (`"r"`).
- The `with` statement ensures the file is automatically closed after the block.

### Reading from a File

You can read a file in various ways, depending on your needs:

- **Read the whole file at once**:

  ```python
  with open("example.txt", "r") as file:
      content = file.read()
      print(content)
  ```

- **Read line by line**:

  ```python
  with open("example.txt", "r") as file:
      for line in file:
          print(line.strip())  # strip() removes newline characters
  ```

### Writing to a File

To write data to a file, use the write mode (`"w"`) or append mode (`"a"` if you want to add to an existing file without overwriting it):

- **Overwrite or create a file**:

  ```python
  with open("example.txt", "w") as file:
      file.write("Hello, world!\n")
      file.write("Writing to a file is easy in Python.")
  ```

- **Append to an existing file**:

  ```python
  with open("example.txt", "a") as file:
      file.write("\nAdding a new line to the file.")
  ```

> **Note**: Using `"w"` will overwrite the file if it exists, while `"a"` will add to it without overwriting.
s

## Functions

Functions are a block of code that only runs when it is called. You can pass data, known as parameters or arguments, into a function and the function can return data as a result. You can compare it with a recipe. You have a set of instructions and you can use it whenever you want. You already used some functions, like `print()` or `len()`. 
Functions are part of every programming language and are very important to structure your code. They make your code more readable and reusable, because you can use the same code multiple times and you don't have to write it again.

A function has the following elements:
- The def keyword
- A function name
- Argument(s) (optional)
- A docstring to explain your function (optional)
- Function body
- A return statement (optional)

The function then looks like this:

```python
def my_function(name):
  """
  This function prints the name.
  """
  greeting = f"Hello, {name}!"
  return greeting
```

This function is called `my_function`. In Python you start with the keyword `def`, which means you define a function. Then you write the function name. After the function name you can define arguments in parentheses. In this case the function takes one argument, `name`, and returns a greeting. You can call this function with the following code:

```python
print(my_function("Alice")) # Output: Hello, Alice!
```

You can also define a function without arguments and without a return statement:

```python
def my_function():
  """
  This function prints a greeting.
  """
  print("Hello, World!")
```

It would look like this:

```python
my_function() # Output: Hello, World!
```

Of course you can also define a function with multiple arguments:

```python

def add_numbers(number1, number2):
  """
  This function adds two numbers.
  """
  return number1 + number2
```

The function `add_numbers` takes two arguments, `number1` and `number2`, and returns the sum of these two numbers. The arguments are separated by a comma. You can name them as you like. They are just placeholders for the values you pass to the function, you could also name them `a` and `b` for example. To call this function you can use the following code:

```python
print(add_numbers(5, 3)) # Output: 8
```

Sometimes it should be optional to pass an argument to a function. You can define a default value for an argument. If you don't pass a value to the function, the default value will be used. 

```python
def my_function(name="World"):
  """
  This function prints a greeting.
  """
  print(f"Hello, {name}!")
```
The result would be:

```python
my_function() # Output: Hello, World!
my_function("Alice") # Output: Hello, Alice!
```

An argument doesn't have to be a string. It can be any data type, like a number, a list, a dictionary, or a boolean. You can also pass a function as an argument to another function. This is called a higher-order function. 

```python
def my_function(names):
  """
  This function prints a list of names.
  """
  for name in names:
    print(name)
```

You can call this function with a list of names:

```python
names = ["Alice", "Bob", "Charlie"]
my_function(names)
```
