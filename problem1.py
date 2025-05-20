class Calculator:
    def __init__(self):
        self.operation = input("Select the operation name you want to perform (Addition, Subtraction, Multiplication, Division): ")
        self.a = float(input("Enter the first value: "))
        self.b = float(input("Enter the second value: "))

    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        if self.b == 0:
            return "Error: Division by zero is not allowed."
        return self.a / self.b

    def calculate(self):
        if self.operation == "Addition":
            return self.addition()
        elif self.operation == "Subtraction":
            return self.subtraction()
        elif self.operation == "Multiplication":
            return self.multiplication()
        elif self.operation == "Division":
            return self.division()
        else:
            return "Error: Invalid operation. Choose from Addition, Subtraction, Multiplication, or Division."

# Create a Calculator instance and perform the calculation.
c = Calculator()
result = c.calculate()
print(f"Result: {result}")
