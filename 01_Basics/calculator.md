# Calculator Project

A simple calculator is a good beginner Python project for practicing:
- User input
- Type casting
- Operators
- `if-elif-else`
- Functions

## Basic Version
```python
a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
```

## Practice Improvements
- Convert the operations into functions.
- Add `%` and `**`.
- Add a loop so the calculator can be used repeatedly.
- Add exception handling for invalid input.
