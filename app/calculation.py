# app/calculation.py

import re
from app.operations import Add, Subtract, Multiply, Divide, Power, Root


class CalculationFactory:

    observers = []

    @staticmethod
    def register_observer(observer):
        CalculationFactory.observers.append(observer)

    @staticmethod
    def notify_observers(expression, result):
        for observer in CalculationFactory.observers:
            observer.update(expression, result)

    @staticmethod
    def process(expression):
        # Normalize input: insert spaces around operators
        expression = re.sub(r'(\d)([+\-*/^])(\d)', r'\1 \2 \3', expression)
        tokens = expression.strip().split()

        if len(tokens) != 3:
            raise ValueError(
                "Expression must be in the format: <num1> <operator> <num2>")

        a, operator, b = tokens
        a, b = float(a), float(b)

        strategy = CalculationFactory.get_strategy(operator)
        result = strategy.execute(a, b)

        # 🔧 FIX: Notify observers AFTER calculation to update history
        CalculationFactory.notify_observers(expression, result)

        return result

    @staticmethod
    def get_strategy(op):
        return {
            '+': Add,
            '-': Subtract,
            '*': Multiply,
            '/': Divide,
            '^': Power,
            'root': Root
        }.get(op) or CalculationFactory.raise_invalid_op(op)

    @staticmethod
    def raise_invalid_op(op):
        raise ValueError(
            f"Invalid operator: {op}. Supported operators are: +, -, *, /, ^, root.")
