a = int(input("enter first number: "))
b = int(input("enter second number: "))

print("Select operation:")
print(" + for addition")
print(" - for subtraction")
print(" * for multiplication")
print(" / for division")

c = input("Enter your choice (+, -, *, /): ")

if c == "+":
    result = (a+b)
    print(result)
elif c == "-":
    result = (a-b)
    print(f"Result: {result}")
elif c == "*":
    result = (a*b)
    print(f"Result: {result}")
elif c == "/":
    if b != 0:
        result = a / b
        print(f"Result: {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("input error, please enter a valid operator")