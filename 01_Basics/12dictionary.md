# 12 - Dictionary

A dictionary stores data as key-value pairs.

## Creating a Dictionary
```python
student = {
    "name": "Tarun",
    "age": 20,
    "course": "CSE"
}
```

## Access Values
```python
print(student["name"])
print(student.get("age"))
```

## Modify and Add
```python
student["age"] = 21
student["city"] = "Shivamogga"
```

## Common Methods
```python
student.keys()
student.values()
student.items()
student.pop("age")
```

## Key Point
Dictionary keys must be hashable and are unique.
