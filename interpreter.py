from expr import *
from stmt import *
from environment import Environment
from token_type import TokenType
from runtime_error import RuntimeError
from error_reporter import ErrorReporter


class Interpreter:
    def __init__(self):
        self.environment = Environment()

    def interpret(self, statements):
        try:
            for statement in statements:
                self.execute(statement)
        except RuntimeError as err:
            ErrorReporter.runtime_error(err)

    def execute(self, stmt):
        match stmt:
            case ExpressionStmt():
                self.evaluate(stmt.expression)
                return None
            case PrintStmt():
                value = self.evaluate(stmt.expression)
                print(self.stringify(value))
                return None
            case VariableStmt():
                value = None
                if stmt.initializer != None:
                    value = self.evaluate(stmt.initializer)

                self.environment.define(stmt.name.lexeme, value)
                return None
            case WhileStmt():
                while self.is_truthy(self.evaluate(stmt.condition)):
                    self.execute(stmt.body)
                return None
            case BlockStmt():
                self.execute_block(
                    stmt.statements, Environment(self.environment))
                return None
            case IfStmt():
                if self.is_truthy(self.evaluate(stmt.condition)):
                    self.execute(stmt.then_branch)
                elif stmt.else_branch is not None:
                    self.execute(stmt.else_branch)

                return None

    def execute_block(self, statements, environment):
        previous = self.environment
        try:
            self.environment = environment
            for statement in statements:
                self.execute(statement)
        finally:
            self.environment = previous

    def evaluate(self, expr):
        match expr:
            case LiteralExpr():
                return self.evaluate_literal(expr)
            case GroupingExpr():
                return self.evaluate_grouping(expr)
            case UnaryExpr():
                return self.evaluate_unary(expr)
            case BinaryExpr():
                return self.evaluate_binary(expr)
            case VariableExpr():
                return self.environment.get(expr.name)
            case AssignExpr():
                value = self.evaluate(expr.value)
                self.environment.assign(expr.name, value)
                return value
            case LogicalExpr():
                left = self.evaluate(expr.left)

                if expr.operator.type is TokenType.OR:
                    if self.is_truthy(left):
                        return left
                else:
                    if not self.is_truthy(left):
                        return left

                return self.evaluate(right)

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
            case TokenType.GREATER:
                self.check_number_operands(expr.operator, left, right)
                return left > right
            case TokenType.GREATER_EQUAL:
                self.check_number_operands(expr.operator, left, right)
                return left >= right
            case TokenType.LESS:
                self.check_number_operands(expr.operator, left, right)
                return left < right
            case TokenType.LESS_EQUAL:
                self.check_number_operands(expr.operator, left, right)
                return left >= right
            case TokenType.MINUS:
                self.check_number_operands(expr.operator, left, right)
                return left - right
            case TokenType.PLUS:
                if isinstance(left, float) and isinstance(right, float):
                    return left + right
                if isinstance(left, str) and isinstance(right, str):
                    return left + right

                raise RuntimeError(
                    expr.operator, "Operands must be two numbers or two strings.")

            case TokenType.SLASH:
                self.check_number_operands(expr.operator, left, right)
                return left / right
            case TokenType.STAR:
                self.check_number_operands(expr.operator, left, right)
                return left * right
            case TokenType.BANG_EQUAL:
                return not left == right
            case TokenType.EQUAL:
                return left == right

    def check_number_operand(self, operator, operand):
        if isinstance(operand, float):
            return
        raise RuntimeError(operator, "Operator must be a number.")

    def check_number_operands(self, operator, left, right):
        if isinstance(left, float) and isinstance(right, float):
            return
        raise RuntimeError(operator, "Operands must be numbers.")

    def is_truthy(self, obj):
        if obj is None:
            return False
        if isinstance(obj, bool):
            return obj
        return True

    def stringify(self, obj):
        if obj is None:
            return "nil"

        if isinstance(obj, float) and obj.is_integer:
            return str(int(obj))

        if isinstance(obj, bool):
            return str(obj).lower()

        return str(obj)
