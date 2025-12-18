a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
operation = input("Enter operation (+/-/*//): ")

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Division by zero is not allowed"
        return self.a / self.b

calc = Calculator(a, b)

if operation == "+":
    print(calc.add())
elif operation == "-":
    print(calc.subtract())
elif operation == "*":
    print(calc.multiply())
elif operation == "/":
    print(calc.divide())
else:
    print("Invalid operation")
