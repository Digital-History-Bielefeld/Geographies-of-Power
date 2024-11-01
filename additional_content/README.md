# Additional Content

This section covers some important concepts and features of programming (in Python) for which we did not have enough time to cover in the main course. These topics are useful for further learning and understanding of programming concepts.

## Classes and Objects

Python is an object-oriented programming language. Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor, or a "blueprint" for creating objects. You 
can compare it with a cookie cutter. You have a form and you can create as many cookies as you like. An object is an instance of a class. 

A class has the following elements:
- The class keyword
- The class name
- A docstring to explain your class (optional)
- The class body
- The __init__ method
- Attributes
- Methods

The class then looks like this:

```python
class Person:
  """
  This class creates a person.
  """
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hello, my name is {self.name} and I am {self.age} years old.")
```

You would use this class like this:

```python
person1 = Person("Alice", 30)
person1.greet() # Output: Hello, my name is Alice and I am 30 years old.
```

So, you have a class `Person` with the attributes `name` and `age`. You can create an instance of this class with the `Person` class and pass the arguments `name` and `age`. The `__init__` method is a special method in Python. It is called a constructor and is always executed when the class is being initiated. The `self` parameter is a reference to the current instance of the class. It is used to access variables that belong to the class. You should always start with the `self` parameter when you define a method in a class.
You can also define other methods in a class. In this case the method `greet` prints a greeting with the name and age of the person. You can access specific attributes of an object by calling the object name and then the attribute name: `object.attribute`.

## Modules and Packages
**Modules** and **Packages** are ways to organize Python code for reusability and structure. A **module** is a single `.py` file containing Python code, which can include functions, variables, and classes. You can create and import modules to use their code in other Python files. For example, if you save the following code as `calculator.py`, it becomes a module:

```python
# calculator.py
def add(a, b):
    return a + b
```

You can import and use this module in another file like this:

```python
import calculator

result = calculator.add(3, 5)
print(result)  # Output: 8
```

A **package** is a collection of related modules stored in a directory with an `__init__.py` file. Packages are used to group similar modules together. It is a good way to organize your code if your project grows larger.
For example, if you create a folder named `utilities` and place `calculator.py` in it, along with an `__init__.py` file, you can import it as a package:

```python	
# utilities/calculator.py
def add(a, b):
    return a + b
```

```python
from utilities import calculator

result = calculator.add(3, 5)
print(result)  # Output: 8
```
