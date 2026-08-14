# 09 - Functions

A function is a reusable block of code designed to perform a specific task.

## Define a Function
```python
def greet():
    print("Hello!")
```

## Call a Function
```python
greet()
```

## Parameters
```python
def greet(name):
    print("Hello", name)

greet("Tarun")
```

## Return Value
```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

## Key Points
- `def` defines a function.
- Parameters receive values.
- `return` sends a value back to the caller.
