# 15 - Type Casting

Type casting means converting a value from one data type to another.

## Common Functions
```python
int()
float()
str()
bool()
list()
tuple()
set()
```

## Example
```python
x = "100"

number = int(x)
print(number + 50)
```

## Example with Input
```python
age = int(input("Enter age: "))
```

## Important
Conversion must be valid. For example:
```python
int("hello")
```
will raise a `ValueError`.
