# This program demonstrates Arithmetic, Comparison, and Logical operators.
# These operators are used to perform calculations, compare values, and evaluate logical conditions.

a = 20
b = 10

print("===== Arithmetic Operators =====")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

print("\n===== Comparison Operators =====")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("\n===== Logical Operators =====")
x = True
y = False

print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)
print("not y   :", not y)

# Operators with higher precedence are evaluated before operators with lower precedence.

print("===== Python Operator Precedence =====")

print("\n1. Parentheses ()")
print("(10 + 5) * 2 =", (10 + 5) * 2)

print("\n2. Exponentiation (**)")
print("2 ** 3 =", 2 ** 3)

print("\n3. Unary Operators (+, -, ~)")
print("-10 =", -10)
print("+10 =", +10)
print("~5 =", ~5)

print("\n4. Multiplication, Division, Floor Division, Modulus")
print("10 * 2 =", 10 * 2)
print("10 / 2 =", 10 / 2)
print("10 // 3 =", 10 // 3)
print("10 % 3 =", 10 % 3)

print("\n5. Addition and Subtraction")
print("10 + 5 =", 10 + 5)
print("10 - 5 =", 10 - 5)

print("\n6. Bitwise Shift")
print("8 << 1 =", 8 << 1)
print("8 >> 1 =", 8 >> 1)

print("\n7. Bitwise AND (&)")
print("5 & 3 =", 5 & 3)

print("\n8. Bitwise XOR (^)")
print("5 ^ 3 =", 5 ^ 3)

print("\n9. Bitwise OR (|)")
print("5 | 3 =", 5 | 3)

print("\n10. Comparison Operators")
print("10 > 5 =", 10 > 5)
print("10 == 5 =", 10 == 5)
print("10 != 5 =", 10 != 5)

print("\n11. Logical NOT")
print("not True =", not True)

print("\n12. Logical AND")
print("True and False =", True and False)

print("\n13. Logical OR")
print("True or False =", True or False)

print("\n14. Assignment Operator")
x = 10
print("x =", x)
x += 5
print("After x += 5, x =", x)

print("\n===== Example of Operator Precedence =====")

result1 = 10 + 5 * 2
print("10 + 5 * 2 =", result1)

result2 = (10 + 5) * 2
print("(10 + 5) * 2 =", result2)