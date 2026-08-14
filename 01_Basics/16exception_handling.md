# 16 - Exception Handling

Exception handling prevents a program from crashing unexpectedly when an error occurs.

## Basic Syntax
```python
try:
    # risky code
except:
    # error handling
```

## Example
```python
try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## finally
```python
try:
    print("Working")
except Exception:
    print("Error")
finally:
    print("This always runs")
```

## Key Point
Prefer catching specific exceptions instead of using a bare `except`.
