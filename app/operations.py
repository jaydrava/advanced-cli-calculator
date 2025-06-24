# app/operations.py

class Add:
    @staticmethod
    def execute(a, b):
        return a + b

class Subtract:
    @staticmethod
    def execute(a, b):
        return a - b
    
class Multiply:
    @staticmethod
    def execute(a, b):
        return a * b
    
class Divide:
    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
class Power:
    @staticmethod
    def execute(a, b):
        return a ** b
    
class Root:
    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ValueError("Cannot take the root with zero degree.")
        return a ** (1 / b)