"""
Multi-Functional Interactive Calculator

Description:
    A self-contained Python terminal application translated from standard C source,
    supporting arithmetic operations, sequential calculations, modular math, 
    factorials, and power functions via a loop system.

Controls:
    - + : Addition (supports multiple numbers)
    - - : Subtraction (takes two numbers)
    - * : Multiplication (supports multiple numbers)
    - / : Division (handles floating-point outputs)
    - ? : Modulus (remainder calculation)
    - ^ : Power (base and exponent calculation)
    - ! : Factorial (combinatorial logic)
    - x : Exit program cleanly

How to Run:
    $ python calculator.py
"""

import sys

def addition():
    """Asks for a specific count of elements and calculates their cumulative sum."""
    try:
        count = int(input("enter how many numbers to add: "))
        if count <= 0:
            print("Please enter a number greater than 0.")
            return
    except ValueError:
        print("Invalid input. Count must be an integer.")
        return

    total = 0
    print(f"enter {count} numbers to add:")
    for _ in range(count):
        while True:
            try:
                num = int(input())
                total += num
                break
            except ValueError:
                print("Invalid format. Please supply a valid integer:")

    print(f"\nthe total = {total}")


def subtraction():
    """Computes the difference between two integers."""
    try:
        num1 = int(input("\nPlease enter first number  : "))
        num2 = int(input("Please enter second number : "))
        print(f"\n{num1} - {num2} = {num1 - num2}")
    except ValueError:
        print("Invalid input. Please enter valid whole integers.")


def multiplication():
    """Asks for a count of elements and computes their total product."""
    try:
        count = int(input("enter number of elements to multiply: "))
        if count <= 0:
            print("Please enter a number greater than 0.")
            return
    except ValueError:
        print("Invalid input. Count must be an integer.")
        return

    total = 1
    print(f"enter {count} numbers to Multiply:")
    for _ in range(count):
        while True:
            try:
                num = int(input())
                total *= num
                break
            except ValueError:
                print("Invalid format. Please supply a valid integer:")

    print(f"\nthe total = {total}")


def division():
    """Divides two numbers with fractional accuracy and safeguards against zero divisions."""
    try:
        num1 = int(input("\nPlease enter first number  : "))
        num2 = int(input("Please enter second number : "))
        
        if num2 == 0:
            print("\nError: Mathematical failure! Division by zero is undefined.")
            return
            
        # Using standard division '/' for floating point precision
        print(f"\n{num1} / {num2} = {num1 / num2}")
    except ValueError:
        print("Invalid input. Please enter valid whole integers.")


def modulus():
    """Calculates the remainder of integer division."""
    try:
        num1 = int(input("\nPlease enter first number   : "))
        num2 = int(input("Please enter second number  : "))
        
        if num2 == 0:
            print("\nError: Modulus by zero is undefined.")
            return
            
        print(f"\n{num1} Modulas {num2} = {num1 % num2}")
    except ValueError:
        print("Invalid input. Please enter valid whole integers.")


def factorial():
    """Computes the product of all positive integers up to a chosen boundary."""
    try:
        number = int(input("\nEnter a number to find factorial : "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return
    except ValueError:
        print("Invalid input. Factorial requires a positive integer.")
        return

    fact = 1
    for temp in range(1, number + 1):
        fact *= temp

    print(f"Factorial of {number} = {fact}")


def power():
    """Calculates exponents, managing negative and positive cases cleanly."""
    try:
        base = int(input("Enter a base number: "))
        expo = int(input("Enter an exponent: "))
    except ValueError:
        print("Invalid input. Base and exponent must be integers.")
        return

    # Using Python's optimized built-in exponentiation operator
    result = base ** expo
    print(f"Answer = {result}")


def main():
    """Runs a switch-case simulator driven by a persistent terminal interface loop."""
    while True:
        print("\nenter \n+ for Addition\n- for Subtraction\n* for Multiplication\n/ for Division"
              "\n? for Modulas\n^ for Power\n! for Factorial\nx for exit")
        
        operation = input("Select operation: ").strip()

        if not operation:
            continue

        if operation == '+':
            addition()
        elif operation == '-':
            subtraction()
        elif operation == '*':
            multiplication()
        elif operation == '/':
            division()
        elif operation == '?':
            modulus()
        elif operation == '^':
            power()
        elif operation == '!':
            factorial()
        elif operation == 'x':
            print("Exiting...")
            sys.exit(0)
        else:
            print("\nenter valid choice")


if __name__ == "__main__":
    main()
