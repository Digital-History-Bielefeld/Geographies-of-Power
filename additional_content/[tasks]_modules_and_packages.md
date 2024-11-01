## Modules

In Python, a module is a file containing Python definitions and statements. It allows you to organize code logically. You can use modules to break down large programs into smaller, more manageable parts. A module can define functions, classes, and variables. A module can also include runnable code.

**Creating a Module**

a) Create a new file with a `.py` extension in the "Session 3"-folder. You can name it "my_module.py" for example.

b) Define a function in the module, which is called `lowercase_and_without_whitespaces`. The function should take a string as an argument and return the string in lowercase and without whitespaces.

c) Save the file.

d) In "module_example.py", import the module you just created with the `import` statement: `import my_module`.

e) Create a variable called `text` and assign a string to it: "   HELLO   ! ".

f) Call the `lowercase_and_without_whitespaces` function from the module and pass the `text` variable as an argument: `my_module.lowercase_and_without_whitespaces(text)` and save its return value in a new variable called `lowercase_text_without_whitespaces`.

g) Print it.

h) Because you don't want to write `my_module` every time you call a function from the module, you can use the `from` keyword to import the function directly: `from my_module import lowercase_and_without_whitespaces`.

i) Call the function again without the module prefix: `lowercase_and_without_whitespaces(text)`.

## Packages

A package is a collection of modules. It allows you to organize your modules in a hierarchical manner. A package is a directory that contains a special file called `__init__.py`, which can be empty. This file tells Python that the directory should be considered a package.

**Creating a Package**
a) Create a new directory in the "Session 3"-folder. You can name it "my_package" for example.

b) Inside the package directory, create a new file with a `.py` extension. You can name it "my_module_2.py" for example.

c) Define a function in the module, which is called `remove_vowels`. The function should take a string as an argument and return the string without vowels.

d) Save the file.

e) Create a __init__.py file in the package directory. The file can be empty.

f) In "module_example.py", import the package you just created with the `import` statement: `import my_package.my_module_2`.

g) Create a variable called `text2` and assign a string to it: "I want to remove all vowels from this text!".
