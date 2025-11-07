def add_numbers(a, b):
print("Adding numbers")
    return a + b

def divide(a, b):
    if b == 0:
        print("Division durch 0!")
    return a / b

result = add_numbers(5, "3")
print("Result:", result)

print(divide(10, 0))
