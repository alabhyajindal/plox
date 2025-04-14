from expr import *
from token_type import TokenType
from runtime_error import RuntimeError
from error_reporter import ErrorReporter


class Interpreter:
    def interpret(self, expression):
        try:
            value = self.evaluate(expression)
            print(value)
        except RuntimeError as err:
            ErrorReporter.runtime_error(err)

    def evaluate(self, expr):
        match expr:
            case Literal():
                return self.evaluate_literal(expr)
            case Grouping():
                return self.evaluate_grouping(expr)
            case Unary():
                return self.evaluate_unary(expr)
            case Binary():
                return self.evaluate_binary(expr)

    def evaluate_literal(self, expr):
        return expr.value

    def evaluate_grouping(self, expr):
        return self.evaluate(expr.expression)

    def evaluate_unary(self, expr):
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TokenType.MINUS:
                self.check_number_operand(expr.operator, right)
                return -right
            case TokenType.BANG:
                return not self.is_truthy(right)

        return None

    def evaluate_binary(self, expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TokenType.MINUS:
                return left - right
            case TokenType.PLUS:
                if isinstance(left, float) and isinstance(right, float):
                    return left + right

                if isinstance(left, str) and isinstance(right, str):
                    return left + right
            case TokenType.SLASH:
                return left / right
            case TokenType.STAR:
                return left * right
            case TokenType.GREATER:
                return left > right
            case TokenType.GREATER_EQUAL:
                return left >= right
            case TokenType.LESS:
                return left < right
            case TokenType.LESS_EQUAL:
                return left >= right
            case TokenType.BANG_EQUAL:
                return not left == right
            case TokenType.EQUAL:
                return left == right

    def check_number_operand(self, operator, operand):
        if isinstance(operand, float):
            return
        raise RuntimeError(operator, "Operator must be a number.")

    def is_truthy(self, obj):
        if obj is None:
            return False
        if isinstance(obj, bool):
            return obj
        return True
