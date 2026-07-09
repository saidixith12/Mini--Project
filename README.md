**Project Overview**

This project is a console-based Python application designed to demonstrate the practical implementation of Object-Oriented Programming (OOP) concepts. 
The application manages different categories of items through a hierarchical class structure, supports dynamic object creation, 
maintains collections of objects, and provides a menu-driven interface for user interaction.

Below are the concepts that are been used in the mini projects

1) **Base Class**

The Product class serves as the parent class and contains attributes and behaviors common to all item types.

**Key attributes:**

Unique identifier
Name
Price

2) **Inheritance**
   
    Product
│
├── Electronics
│
└── Clothing
  
3)  **Encapsulation**

   self.__price = price

   Note : The double underscore (__) restricts direct access to the attribute from outside the class.

4) **Static Methods**

   @staticmethod
def generate_product_id():

Purpose:
Generate unique IDs for newly created objects.

6) **Class Variables**

   product_counter = 1000

   Purpose:
   Used for sequential ID generation.

7) **Method Overriding**

   def __str__(self):

   The derived classes extend the parent class output by including additional attributes such as warranty or size information.

8) **Polymorphism**

    items = []

   Objects of different subclasses can be treated uniformly through their common parent class.

9) **Magic Methods**

    __str__()


Purpose:

  Defines how objects are represented as strings.
  Improves readability when printing objects.

Without this method:

  <__main__.Product object at 0x...>

With this method:

  [1001] Item Name - ₹1000


**Technical Summary**

This project demonstrates a structured object-oriented design using Python's built-in capabilities. It showcases key OOP principles such as encapsulation, 
inheritance, polymorphism, abstraction, method overriding, static methods, and class variables while maintaining a modular and maintainable codebase. 
The implementation avoids external dependencies and relies solely on Python's core language features, making it lightweight, portable, and 
suitable for learning and demonstrating object-oriented programming concepts.
   
   


























































   
